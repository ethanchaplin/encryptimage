"""
Visual Data Encrypter
Copyright (C) 2019 Ethan Chaplin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PIL import Image


class EncryptEngine:

    def __init__(self):
        self.numPrimes = 1000  # Default number of primes to load, in case user does not supply a number

    def setPrimes(self, n):
        self.numPrimes = n

    def colorify(self, hex):
        # Takes a hexadecimal number of arbitrary length and splits it into groups of 6
        # Pads any remaining strings with a length less than 6 with 0s to the left

        _hex = str(hex)
        return [_hex[i:i + 6].zfill(6) for i in range(0, len(_hex), 6)]

    def locate(
        self,
        height,
        width,
        position,
        ):
        # Creates a coordinate system to efficiently find a pixels location

        rw = 0
        for x in range(height + 1):
            """
            Any pixels location can be described as a single number which is correlated to the rows and columns of an image
            For example, an image of 5 pixels by 3 pixels will look like
            
               0   1   2   3   4
             +---+---+---+---+---+
           0 | 0 | 1 | 2 | 3 | 4 |
             +---+---+---+---+---+
           1 | 5 | 6 | 7 | 8 | 9 |
             +---+---+---+---+---+
           2 | 10| 11| 12| 13| 14|
             +---+---+---+---+---+
            
            Each pixels location can be described as the (row number) * (number of columns) + (column number).
            For example, the pixel at (1, 2) in the example image will go into the algorithm.
            
            (2) * (    5    ) + (1) = 11, which corresponds to the table above. 
            row   num of rows   col
            
            This will work for any image of any size. 
            """
            if x * width > position:
                rw = x - 1
                break

            if height * width <= position:
                #
                raise Exception('The given position is out of bounds.')
        if rw == 0:
            return [position, 0]  # if the inputs equal zero, then the output will be zero as well
        else:
            return [position - rw * width, rw]  # uses the algorithm as described above.

    def hexToRGB(self, hex):
        # takes in a 6-byte hexadecimal number and converts it to its corresponding RGB tuple

        _hex = str(hex)
        if len(_hex) > 6:
            # if input is larger than 6 bytes, throw the error
            raise Exception('The given value needs to be a valid 6-byte hex value'
                            )
        else:
            # return the hex as a tuple
            rslt = [_hex[i:i + 2] for i in range(0, len(_hex), 2)]
            return [int(rslt[0], 16), int(rslt[1], 16), int(rslt[2],
                    16)]

    def rgbToHex(self, colorArray):
        # takes an RGB tuple and returns the corresponding hex value
        return '%02x%02x%02x' % (colorArray[0], colorArray[1],
                                 colorArray[2])

    def prime(self, num):
        # the order in which the pixels are scattered are dependent on the prime series. Primes are located at a
        # seemingly random order, so scattering the pixels according to the primes might avoid detection
        # this function is essentially the Sieve of Eratosthenes
        num = int(num)
        lst = []

        if num < 2:
            return lst

        if num >= 2:
            lst.append(2)

        for i in range(3, num + 1):
            if i % 2 == 1:
                switch = True
                for n in range(3, int(i ** 0.5) + 1, 2):
                    if i % n == 0:
                        switch = False
                        break
                if switch:
                    lst.append(i)

        return lst

    def encrypt(
        self,
        data,
        image,
        output,
        ):
        dataPoint = 0
        greenDataPoint = 0
        redDataPoint = 0
        prevLocation = 0
        s = data.encode('utf-8')
        c = self.colorify(s.hex())  # takes the encoded string and converts it to hex, and then splices it into sections of six

        img = Image.open(image)  # open Image through PIL library

        primes = self.prime(self.numPrimes)  # generates list of primes

        pixels = img.load()  # creates the pixel map


        for x in c:
            location = primes[dataPoint] + prevLocation  # sets location of next data point

            pixels[self.locate(img.size[1], img.size[0], location)[0],
                   self.locate(img.size[1], img.size[0],
                   location)[1]] = (self.hexToRGB(c[dataPoint])[0],
                                    self.hexToRGB(c[dataPoint])[1],
                                    self.hexToRGB(c[dataPoint])[2])  # changes color of selected pixel to corresponding colorified hex value
            prevLocation = location  # sets previous location for reference
            dataPoint = 1 + dataPoint
        if dataPoint > 255:
            dataPoint = 255
            greenDataPoint = dataPoint // 255
        else:
            dataPoint = dataPoint

        pixels[0, 0] = (redDataPoint, greenDataPoint, dataPoint)  # sets top left pixel to number of data points
        img.save(output, 'BMP')  # saves the image in the same directory as a bitmap image

    def decode(self, image):
        dataPoint = 0
        prevLocation = 0
        img = Image.open(image)
        primes = self.prime(self.numPrimes)
        pixels = img.load()  # create the pixel map
        final = []
        output = ''
        numIterations = pixels[0, 0][2]  # reads top left pixel to see how many data points to read
        for x in range(numIterations):
            location = primes[dataPoint] + prevLocation
            final.append(self.rgbToHex(pixels[self.locate(img.size[1],
                         img.size[0], location)[0],
                         self.locate(img.size[1], img.size[0],
                         location)[1]]))  # appends all data points gathered into one hexadecimal number
            prevLocation = location
            dataPoint = 1 + dataPoint
        for y in final:
            strip = y.lstrip('0')  # removes all leading 0s
            output = output + strip
        return bytearray.fromhex(output).decode()  # returns final decoded string

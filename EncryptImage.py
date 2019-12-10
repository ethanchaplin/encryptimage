from PIL import Image

numPrimes = 1

def setPrimes(n):
    global numPrimes
    numPrimes = n
def colorify(hex):
    _hex=str(hex)
    return [_hex[i:i + 6].zfill(6) for i in range(0, len(_hex), 6)]
def locate(height, width, position):
    rw=0
    for x in range(height + 1):
        if x * (width) > position:
            rw=x-1
            break

        if height * width <= position:
            raise Exception("The given position is out of bounds.")
    if rw==0:
        return [position,0]
    else:
        return [position-(rw*width),rw]


def hexToRGB(hex):
    _hex=str(hex)
    if len(_hex) > 6:
        raise Exception("The given value needs to be a valid 6-byte hex value")
    else:
        rslt = [_hex[i:i + 2] for i in range(0, len(_hex), 2)]
        return [int(rslt[0], 16), int(rslt[1], 16), int(rslt[2], 16)]
def rgbToHex(colorArray):
    return '%02x%02x%02x' % (colorArray[0], colorArray[1], colorArray[2])
def prime(num):
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
def encrypt(data, image, output):
    dataPoint = 0
    prevLocation = 0
    s = data.encode('utf-8')
    c = colorify(s.hex())
    img = Image.open(image)
    primes = prime(numPrimes)
    pixels = img.load()
    # create the pixel map

    for x in c:
        location = primes[dataPoint] + prevLocation
        pixels[locate(img.size[1], img.size[0], location)[0], locate(img.size[1], img.size[0], location)[1]] = (
        hexToRGB(c[dataPoint])[0], hexToRGB(c[dataPoint])[1], hexToRGB(c[dataPoint])[2])
        prevLocation = location
        dataPoint = 1 + dataPoint
    pixels[0, 0] = (0, 0, dataPoint)
    img.save(output, "BMP")
def decode(image):
    dataPoint = 0
    prevLocation = 0
    img = Image.open(image)
    primes = prime(numPrimes)
    pixels = img.load()  # create the pixel map
    final = []
    output = ""
    numIterations = pixels[0, 0][2]
    for x in range(numIterations):
        location = primes[dataPoint] + prevLocation
        final.append(rgbToHex(pixels[locate(img.size[1], img.size[0], location)[0], locate(img.size[1], img.size[0], location)[1]]))
        prevLocation = location
        dataPoint = 1 + dataPoint
    for y in final:
        strip = y.lstrip("0")
        output = output + strip
    return bytearray.fromhex(output).decode()
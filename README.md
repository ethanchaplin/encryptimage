# Visual Data Encrypter

This application was designed to secretly encode data into an image, but in a more unorthadox way than is typically used. Instead of conventional stegonography techinques, this program encodes the data individually into distinct pixels. The pixels are then scattered arbitrarily across the given image. Depending on the size of the given image, the encoded pixels will be almost impossible to distinguish from the naked eye.

## About

This project has two parts to it:

* The Engine

* The GUI

### The Engine

The [engine](/src/EncryptEngine.py) can be used standalone in projects. Just import it like you would any other local modules, and it can be easily integrated into your project.

It works in the following steps:

#### Encrypting
1. The user inputs a string of text and an image to manipulate
1. The text is converted to hexadecimal
1. The resulting hexadecimal is chunked into sections of six, and if one of the chunks is too small, it is padded with zeroes to the left.
1. The chunks of six are turned into RGB tuples. *E.G. FFFFFF would become (255, 255, 255), or A5DF2C would become (165,223,44).*
1. Specific pixels are selected across the image, and their color is changed to the RGB tuple of the corresponding data.
1. The color of the pixel in the top left corner is changed to match how many points of data were encoded. *E.G. if three pixels are encoded in the image, the value of the corner pixel will be (0, 0, 3).*

#### Decrypting
1. The user inputs an encoded image
1. Specific pixels are selected across the image, and the color data of each pixel is read.
1. The hexadecimal data from each pixel is concatenated, with leading zeroes erased.
1. The resulting hexadecimal code is converted to ASCII, and is returned.

### The GUI

The GUI is the main focus of this repository, as it allows for more easy interaction with the engine.

## Getting Started

### Prerequisites

For this project you will need

```
Python 3.8
PyQt5
PILlow
```

### Installing

You will need to set up a pipenv enviroment to build this project.

#### Installing pipenv

First, you need to install pipenv through pip:

```
pip install pipenv
```

Ta-da!

#### Initializing pipenv

In your project folder, run:

```
pipenv sync
```

This will sync the required modules with your project. Next, start a pipenv shell within your project. This is done by:

```
pipenv shell
```

#### Running the project

Now that you have a pipenv shell running, all you have to do is run the file like you would any other python script:

```
python main.py
```

## Authors

* **Ethan Chaplin** - *Initial work* - [Ethan Chaplin](https://github.com/EthanChaplin)

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details




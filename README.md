# Visual Data Encrypter

This application was designed to secretly encode data into an image, but in a more unorthadox way. Instead of conventional stegonography techinques, this program encodes the data individually into distinct pixels. The pixels are then scattered arbitrarily across the given image. Depending on the size of the given image, the encoded pixels will be almost impossible to distinguish from the naked eye.

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

First, you need to install pipenv through pip

```
pip install pipenv
```

Ta-da!

#### Initializing pipenv

In your project folder, run

```
pipenv sync
```

This will sync the required modules with your project. Next, start a pipenv shell within your project. This is done by

```
pipenv shell
```

#### Running the project

Now that you have a pipenv shell running, all you have to do is run the file like you would any other python script

```
python main.py
```

## Authors

* **Ethan Chaplin** - *Initial work* - [Ethan Chaplin](https://github.com/EthanChaplin)

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE.md) file for details




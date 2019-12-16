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

import sys
from src import EncryptImage
from PyQt5 import QtWidgets

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)  # initializes PyQt Window
    MainWindow = QtWidgets.QMainWindow()  # Loads main window
    ui = EncryptImage.EngineUI()
    ui.setupUi(MainWindow)  # Assigns the EncryptImage UI to the main window
    MainWindow.show()  # Shows the window
    sys.exit(app.exec_())

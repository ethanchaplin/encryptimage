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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, \
    QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from . import EncryptEngine


class EngineUI(object):

    currentImage = ''
    currentImageDec = ''

    def setupUi(self, MainWindow):
        # UI creation
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-6, -1, 801, 551))
        self.tabWidget.setObjectName('tabWidget')
        self.encrypt = QtWidgets.QWidget()
        self.encrypt.setObjectName('encrypt')
        self.chooseImage = QtWidgets.QPushButton(self.encrypt)
        self.chooseImage.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.chooseImage.setObjectName('chooseImage')
        self.chooseImage.clicked.connect(lambda : self.setImage())
        self.label = QtWidgets.QLabel(self.encrypt)
        self.label.setGeometry(QtCore.QRect(20, 60, 751, 311))
        self.label.setText('')
        self.label.setObjectName('label')
        pixmap = QPixmap('')
        self.label.setPixmap(pixmap)
        self.data = QtWidgets.QTextEdit(self.encrypt)
        self.data.setGeometry(QtCore.QRect(20, 390, 661, 121))
        self.data.setObjectName('data')
        self.encrypt_2 = QtWidgets.QPushButton(self.encrypt)
        self.encrypt_2.setGeometry(QtCore.QRect(690, 440, 93, 28))
        self.encrypt_2.setObjectName('encrypt_2')
        self.encrypt_2.clicked.connect(lambda : self.beginEncryption())
        self.label_2 = QtWidgets.QLabel(self.encrypt)
        self.label_2.setGeometry(QtCore.QRect(140, 17, 55, 16))
        self.label_2.setObjectName('label_2')
        self.primesEnter = QtWidgets.QLineEdit(self.encrypt)
        self.primesEnter.setGeometry(QtCore.QRect(190, 16, 131, 22))
        self.primesEnter.setObjectName('primesEnter')
        self.tabWidget.addTab(self.encrypt, '')
        self.decrypt = QtWidgets.QWidget()
        self.decrypt.setObjectName('decrypt')
        self.primes_Decrypt = QtWidgets.QLineEdit(self.decrypt)
        self.primes_Decrypt.setGeometry(QtCore.QRect(190, 16, 131, 22))
        self.primes_Decrypt.setObjectName('primes_Decrypt')
        self.label_3 = QtWidgets.QLabel(self.decrypt)
        self.label_3.setGeometry(QtCore.QRect(140, 17, 55, 16))
        self.label_3.setObjectName('label_3')
        self.chooseImage_dec = QtWidgets.QPushButton(self.decrypt)
        self.chooseImage_dec.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.chooseImage_dec.setObjectName('chooseImage_dec')
        self.chooseImage_dec.clicked.connect(lambda : \
                self.setImageForDecrypt())
        self.output = QtWidgets.QTextEdit(self.decrypt)
        self.output.setGeometry(QtCore.QRect(10, 70, 781, 451))
        self.output.setObjectName('output')
        self.decrypt_2 = QtWidgets.QPushButton(self.decrypt)
        self.decrypt_2.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.decrypt_2.setObjectName('decrypt_2')
        self.decrypt_2.clicked.connect(lambda : self.beginDecryption())
        self.tabWidget.addTab(self.decrypt, '')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName('menubar')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow',
                                  'Visual Data Encrypter'))
        self.chooseImage.setText(_translate('MainWindow', 'Choose Image'
                                 ))
        self.encrypt_2.setText(_translate('MainWindow', 'Encrypt Data'))
        self.label_2.setText(_translate('MainWindow', 'Primes:'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encrypt),
                                  _translate('MainWindow', 'Encrypt'))
        self.label_3.setText(_translate('MainWindow', 'Primes:'))
        self.chooseImage_dec.setText(_translate('MainWindow',
                'Choose Image'))
        self.decrypt_2.setText(_translate('MainWindow', 'Decrypt'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decrypt),
                                  _translate('MainWindow', 'Decrypt'))

    def openFileNameDialog(self):
        # opens file dialog to choose which image is being manipulated
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        (fileName, _) = QFileDialog.getOpenFileName(QWidget(),
                'Choose File', '', 'Image Files (*.png *.jpg *.bmp)',
                options=options)
        if fileName:
            return fileName

    def setImage(self):
        # sets current image for reference
        QtCore.QCoreApplication.processEvents()
        image = self.openFileNameDialog()
        self.currentImage = image
        pixmap = QPixmap(image)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        QtCore.QCoreApplication.processEvents()

    def setImageForDecrypt(self):
        # sets the decrypting image for reference
        QtCore.QCoreApplication.processEvents()
        image = self.openFileNameDialog()
        self.currentImageDec = image
        QtCore.QCoreApplication.processEvents()

    def beginEncryption(self):
        # uses the EncryptEngine encrypt() function to encrypt the data into an image
        QtCore.QCoreApplication.processEvents()
        e = EncryptEngine.EncryptEngine()

        if self.currentImage == "":
            print("Image needed!")
        else:
            if self.primesEnter.text() == "":
                e.encrypt(self.data.toPlainText(), self.currentImage,
                          self.currentImage + '.bmp')
            else:
                e.setPrimes(int(self.primesEnter.text()))
                e.encrypt(self.data.toPlainText(), self.currentImage,
                          self.currentImage + '.bmp')

    def beginDecryption(self):
        # uses the EncryptEngine decode() function to decrypt the image into a string of text
        QtCore.QCoreApplication.processEvents()
        e = EncryptEngine.EncryptEngine()
        if self.currentImageDec == "":
            print("Image needed!")
        else:
            if self.primes_Decrypt.text() == '':
                self.output.setText(e.decode(self.currentImageDec))
            else:
                e.setPrimes(int(self.primes_Decrypt.text()))
                self.output.setText(e.decode(self.currentImageDec))

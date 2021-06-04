# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataMahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from EntryForm import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 457)
        self.DataMahasiswa = QtWidgets.QLabel(Form)
        self.DataMahasiswa.setGeometry(QtCore.QRect(150, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        #Komponen Label untuk text Data Mahasiswa
        self.DataMahasiswa.setFont(font)
        self.DataMahasiswa.setObjectName("DataMahasiswa")

        #Komponen ListWidget untuk menampilkan data mahasiswa
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 411, 221))
        self.listWidget.setObjectName("listWidget")

        #Komponen Label untuk text NIM
        self.NIM = QtWidgets.QLabel(Form)
        self.NIM.setGeometry(QtCore.QRect(20, 290, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NIM.setFont(font)
        self.NIM.setObjectName("NIM")

        #Komponen Label untuk text Nama
        self.Nama = QtWidgets.QLabel(Form)
        self.Nama.setGeometry(QtCore.QRect(20, 320, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nama.setFont(font)
        self.Nama.setObjectName("Nama")

        #Komponen Label untuk text Jurusan
        self.Jurusan = QtWidgets.QLabel(Form)
        self.Jurusan.setGeometry(QtCore.QRect(20, 350, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Jurusan.setFont(font)
        self.Jurusan.setObjectName("Jurusan")

        #Komponen Label untuk text NoTelp
        self.NoTelp = QtWidgets.QLabel(Form)
        self.NoTelp.setGeometry(QtCore.QRect(20, 380, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NoTelp.setFont(font)
        self.NoTelp.setObjectName("NoTelp")

        #Komponen line edit untuk Input nama
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 290, 351, 20))
        self.lineEdit.setObjectName("lineEdit")

        #Komponen line edit untuk Input NIM
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 320, 351, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        #Komponen line edit untuk Input Jurusan
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 350, 351, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        #Komponen line edit untuk Input No Telp
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 380, 351, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        #Komponen PushButton untuk tambah
        self.Tambah = QtWidgets.QPushButton(Form)
        self.Tambah.setGeometry(QtCore.QRect(120, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Tambah.setFont(font)
        self.Tambah.setObjectName("Tambah")
        self.Tambah.clicked.connect(self.addButtonClick)

        #Komponen PushButton untuk edit
        self.Edit = QtWidgets.QPushButton(Form)
        self.Edit.setGeometry(QtCore.QRect(200, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")
        self.Edit.clicked.connect(self.editButtonClick)

        #Komponen PushButton untuk Clear
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(280, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.Clear.clicked.connect(self.listWidget.clear)

        #Komponen PushButton untuk Hapus
        self.Hapus = QtWidgets.QPushButton(Form)
        self.Hapus.setGeometry(QtCore.QRect(360, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Hapus.setFont(font)
        self.Hapus.setObjectName("Hapus")
        self.Hapus.clicked.connect(self.deleteButtonClick)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.DataMahasiswa.setText(_translate("Form", "Data Mahasiswa"))
        self.NIM.setText(_translate("Form", "NIM"))
        self.Nama.setText(_translate("Form", "Nama"))
        self.Jurusan.setText(_translate("Form", "Jurusan"))
        self.NoTelp.setText(_translate("Form", "No.Telp"))
        self.Tambah.setText(_translate("Form", "TAMBAH"))
        self.Edit.setText(_translate("Form", "EDIT"))
        self.Clear.setText(_translate("Form", "CLEAR"))
        self.Hapus.setText(_translate("Form", "HAPUS"))

    def addButtonClick(self):
        self.listWidget.addItem(
            self.lineEdit.text() + ' - ' +
            self.lineEdit_2.text() + ' - ' +
            self.lineEdit_3.text() + ' - ' +
            self.lineEdit_4.text())

    def editButtonClick(self):
        if self.listWidget.currentRow() < 0: return
        self.entryForm = EntryForm()
        s = str(self.listWidget.currentItem().text())
        idx = s.index('-')
        self.entryForm.nim.setText(s[:(idx - 1)])
        self.entryForm.nama.setText(s[(idx - 2):])
        self.entryForm.jurusan.setText(s[(idx - 3):])
        self.entryForm.telp.setText(s[(idx - 4):])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.listWidget.currentItem().setText(
                self.entryForm.nim.text() + ' - ' +
                self.entryForm.nama.text() + ' - ' +
                self.entryForm.jurusan.text() + ' - ' +
                self.entryForm.telp.text())

    def deleteButtonClick(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

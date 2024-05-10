import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class SignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(3000, 1000))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color:rgb(223, 223, 223);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setStyleSheet("QGroupBox {\n"
"    border: 2px solid rgb(223, 223, 223);\n"
"    border-radius: 10px; /* Set border radius for rounded corners */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* Position the title at the top center */\n"
"    padding: 0 5px; /* Adjust padding for the title */\n"
"    background-color: #f0f0f0; /* Set background color for the title */\n"
"}\n"
"\n"
"QGroupBox::title:hover {\n"
"    background-color: #e0e0e0; /* Change title background color on hover */\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    width: 16px; /* Set the width of the indicator */\n"
"    height: 16px; /* Set the height of the indicator */\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"    background-color: #555555; /* Set background color for checked indicator */\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover {\n"
"    background-color: #333333; /* Change background color for checked indicator on hover */\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"    background-color: #999999; /* Set background color for disabled checked indicator */\n"
"}\n"
"")
        self.groupbox.setObjectName("groupbox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupbox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupbox1 = QtWidgets.QGroupBox(self.groupbox)
        self.groupbox1.setStyleSheet("border:none;")
        self.groupbox1.setObjectName("groupbox1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupbox1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.groupbox2 = QtWidgets.QGroupBox(self.groupbox1)
        self.groupbox2.setStyleSheet("")
        self.groupbox2.setObjectName("groupbox2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox2)
        self.verticalLayout.setContentsMargins(-1, 27, -1, -1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupbox2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupbox2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 32))
        self.textEdit_3.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.textEdit_3)
        self.verticalLayout_6.addWidget(self.groupbox2)
        self.groupbox3 = QtWidgets.QGroupBox(self.groupbox1)
        self.groupbox3.setStyleSheet("")
        self.groupbox3.setObjectName("groupbox3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupbox3)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupbox3)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupbox3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 28))
        self.textEdit_2.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_4.addWidget(self.textEdit_2)
        self.verticalLayout_6.addWidget(self.groupbox3)
        self.groupbox4 = QtWidgets.QGroupBox(self.groupbox1)
        self.groupbox4.setStyleSheet("")
        self.groupbox4.setObjectName("groupbox4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupbox4)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 22)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupbox4)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.groupbox4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 28))
        self.textEdit.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_6.addWidget(self.groupbox4)
        self.radioButton = QtWidgets.QRadioButton(self.groupbox1)
        self.radioButton.setStyleSheet("color:grey;")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_6.addWidget(self.radioButton)
        self.groupbox5 = QtWidgets.QGroupBox(self.groupbox1)
        self.groupbox5.setStyleSheet("background-color: none;\n"
"border: none;\n"
"\n"
"")
        self.groupbox5.setObjectName("groupbox5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupbox5)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.signup = QtWidgets.QPushButton(self.groupbox5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setAutoFillBackground(False)
        self.signup.setStyleSheet("color: black;\n"
" background-color: transparent;\n"
"border: 2px solid rgb(63, 71, 105);\n"
"border-radius: 10px; /* Set border radius for rounded corners */\n"
"")
        self.signup.setObjectName("signup")
        self.horizontalLayout_2.addWidget(self.signup)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.groupbox5)
        self.groupbox6 = QtWidgets.QGroupBox(self.groupbox1)
        self.groupbox6.setMaximumSize(QtCore.QSize(16777215, 33))
        self.groupbox6.setStyleSheet("")
        self.groupbox6.setObjectName("groupbox6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupbox6)
        self.horizontalLayout.setContentsMargins(21, 0, 60, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupbox6)
        self.label_2.setMaximumSize(QtCore.QSize(269, 45))
        self.label_2.setStyleSheet("color:grey;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.groupbox6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(229, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(0, 85, 255);\n"
"background-color: none;\n"
"Font: 8pt;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_6.addWidget(self.groupbox6)
        self.horizontalLayout_3.addWidget(self.groupbox1)
        self.label_8 = QtWidgets.QLabel(self.groupbox)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("border-radius: 10px; /* Set border radius for rounded corners */\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
"")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(r"Icons\signup-image.jpeg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.gridLayout.addWidget(self.groupbox, 0, 0, 1, 1)
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.signup.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.radioButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        #self.label_5.setBuddy(MainWindow.Confirm_Password)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Create An Account"))
        self.label_3.setText(_translate("MainWindow", "UserName"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Enter UserName"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.label_5.setText(_translate("MainWindow", "Confirm Password"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.radioButton.setText(_translate("MainWindow", "I agree to the Terms of sevices and privacy policy"))
        self.signup.setText(_translate("MainWindow", " Sign Up "))
        self.label_2.setText(_translate("MainWindow", "Aleady have an account?"))
        self.pushButton.setText(_translate("MainWindow", "LogIn"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SignUp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

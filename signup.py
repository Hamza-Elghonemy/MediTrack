import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import resources


class SignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"color:#000000;\n"
"font-family: Arial;\n"
"border:none;\n"
"}\n"
"\n"
"#centralwidget{\n"
"border-radius: 20px;\n"
"background-color:#fefeff;\n"
"}\n"
"#nameBox, #confirmBox,#emailBox, #passwordBox, #ageBox, #sexBox{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 18px;\n"
"font: Segoe Script;\n"
"}\n"
"  #profileButton{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 10pt;\n"
"}\n"
"#topwidget, #widget_2{\n"
"\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 18px Segoe Script;\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius:20px;\n"
"}\n"
"\n"
"#middlewidget{\n"
"border-radius: 20px;\n"
"background-color:#bce1f9;\n"
"}\n"
"\n"
"#label{\n"
"border-radius: 20px;\n"
"background: transparent;\n"
"}\n"
"\n"
"#appheader{\n"
"color:#2596be;\n"
"}\n"
"#vitalsign,#filterflex, #comboBox{\n"
"color:#2596be;\n"
"}\n"
"#EMGlabel{\n"
"color:#2596be;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color: #2596be;\n"
"}\n"
"\n"
"#rightmenu{\n"
"background-color: #bce1f9;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: transparent;\n"
"color:#2596be;\n"
"}\n"
"\n"
"#signupButton, #accountButton, #menuButton, #profileButton, #logoutButton,#lineEdit_3{\n"
"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"}\n"
"\n"
"#label_2{\n"
"color: white;\n"
"}\n"
"#loginButton{\n"
"color: #2596be;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(54, 37, 36, 44)
        self.verticalLayout.setObjectName("verticalLayout")
        self.middlewidget = QtWidgets.QWidget(self.centralwidget)
        self.middlewidget.setMinimumSize(QtCore.QSize(650, 655))
        self.middlewidget.setObjectName("middlewidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.middlewidget)
        self.verticalLayout_10.setContentsMargins(41, 1, 79, 16)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.nameBox = QtWidgets.QWidget(self.middlewidget)
        self.nameBox.setMinimumSize(QtCore.QSize(77, 77))
        self.nameBox.setStyleSheet("")
        self.nameBox.setObjectName("nameBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.nameBox)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.nameBox)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 53))
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_21 = QtWidgets.QLabel(self.frame_2)
        self.label_21.setMinimumSize(QtCore.QSize(40, 40))
        self.label_21.setMaximumSize(QtCore.QSize(40, 40))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/Icons/Icons/user-plus.svg"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_4.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        self.label_22.setMinimumSize(QtCore.QSize(476, 43))
        self.label_22.setMaximumSize(QtCore.QSize(476, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.label_7 = QtWidgets.QLabel(self.nameBox)
        self.label_7.setMinimumSize(QtCore.QSize(0, 31))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.textEdit_4 = QtWidgets.QTextEdit(self.nameBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 35))
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_7.addWidget(self.textEdit_4)
        self.verticalLayout_10.addWidget(self.nameBox)
        self.emailBox = QtWidgets.QWidget(self.middlewidget)
        self.emailBox.setMinimumSize(QtCore.QSize(0, 77))
        self.emailBox.setMaximumSize(QtCore.QSize(16777215, 77))
        self.emailBox.setStyleSheet("")
        self.emailBox.setObjectName("emailBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.emailBox)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.emailBox)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.textEdit_3 = QtWidgets.QTextEdit(self.emailBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMinimumSize(QtCore.QSize(0, 35))
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_8.addWidget(self.textEdit_3)
        self.verticalLayout_10.addWidget(self.emailBox)
        self.ageBox = QtWidgets.QWidget(self.middlewidget)
        self.ageBox.setMinimumSize(QtCore.QSize(0, 74))
        self.ageBox.setMaximumSize(QtCore.QSize(16777215, 77))
        self.ageBox.setStyleSheet("")
        self.ageBox.setObjectName("ageBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ageBox)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.ageBox)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.ageText = QtWidgets.QTextEdit(self.ageBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ageText.sizePolicy().hasHeightForWidth())
        self.ageText.setSizePolicy(sizePolicy)
        self.ageText.setMinimumSize(QtCore.QSize(0, 35))
        self.ageText.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(True)
        font.setWeight(75)
        self.ageText.setFont(font)
        self.ageText.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.ageText.setObjectName("ageText")
        self.verticalLayout_9.addWidget(self.ageText)
        self.verticalLayout_10.addWidget(self.ageBox)
        self.sexBox = QtWidgets.QWidget(self.middlewidget)
        self.sexBox.setStyleSheet("")
        self.sexBox.setObjectName("sexBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.sexBox)
        self.horizontalLayout_6.setContentsMargins(0, 11, 0, 8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.sexBox)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.radioButton_2 = QtWidgets.QRadioButton(self.sexBox)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_6.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.sexBox)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_6.addWidget(self.radioButton_3)
        self.verticalLayout_10.addWidget(self.sexBox)
        self.passwordBox = QtWidgets.QWidget(self.middlewidget)
        self.passwordBox.setMinimumSize(QtCore.QSize(0, 77))
        self.passwordBox.setMaximumSize(QtCore.QSize(16777215, 77))
        self.passwordBox.setStyleSheet("")
        self.passwordBox.setObjectName("passwordBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.passwordBox)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.passwordBox)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.textEdit_2 = QtWidgets.QTextEdit(self.passwordBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_5.addWidget(self.textEdit_2)
        self.verticalLayout_10.addWidget(self.passwordBox)
        self.confirmBox = QtWidgets.QWidget(self.middlewidget)
        self.confirmBox.setMinimumSize(QtCore.QSize(0, 77))
        self.confirmBox.setMaximumSize(QtCore.QSize(16777215, 77))
        self.confirmBox.setStyleSheet("")
        self.confirmBox.setObjectName("confirmBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.confirmBox)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.confirmBox)
        self.label_5.setMinimumSize(QtCore.QSize(0, 22))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 68))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.confirmBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 32))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid  rgb(230, 230, 230); /* Set border width and color */\n"
"    border-radius: 10px; /* Set border radius for rounded corners */")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.verticalLayout_10.addWidget(self.confirmBox)
        self.radioButton = QtWidgets.QRadioButton(self.middlewidget)
        self.radioButton.setMinimumSize(QtCore.QSize(0, 54))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color:grey;")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_10.addWidget(self.radioButton)
        self.widget_3 = QtWidgets.QWidget(self.middlewidget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 46))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 46))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.signupButton = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signupButton.sizePolicy().hasHeightForWidth())
        self.signupButton.setSizePolicy(sizePolicy)
        self.signupButton.setMinimumSize(QtCore.QSize(116, 39))
        self.signupButton.setMaximumSize(QtCore.QSize(16777215, 39))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.signupButton.setFont(font)
        self.signupButton.setAutoFillBackground(False)
        self.signupButton.setObjectName("signupButton")
        self.horizontalLayout_10.addWidget(self.signupButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_10.addWidget(self.widget_3)
        self.loginBox_3 = QtWidgets.QGroupBox(self.middlewidget)
        self.loginBox_3.setMinimumSize(QtCore.QSize(0, 29))
        self.loginBox_3.setMaximumSize(QtCore.QSize(16777215, 33))
        self.loginBox_3.setStyleSheet("")
        self.loginBox_3.setObjectName("loginBox_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.loginBox_3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.loginBox_3)
        self.label_6.setMinimumSize(QtCore.QSize(279, 22))
        self.label_6.setMaximumSize(QtCore.QSize(279, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.loginButton = QtWidgets.QPushButton(self.loginBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QtCore.QSize(123, 36))
        self.loginButton.setMaximumSize(QtCore.QSize(123, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("")
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_11.addWidget(self.loginButton)
        self.verticalLayout_10.addWidget(self.loginBox_3)
        self.verticalLayout.addWidget(self.middlewidget)
        MainWindow.setCentralWidget(self.centralwidget)
        #self.label_5.setBuddy(MainWindow.Confirm Password)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_22.setText(_translate("MainWindow", "Create an account"))
        self.label_7.setText(_translate("MainWindow", "Name"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Enter Name/UserName"))
        self.label_8.setText(_translate("MainWindow", "Email Address"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Enter Email"))
        self.label_10.setText(_translate("MainWindow", "Age"))
        self.ageText.setPlaceholderText(_translate("MainWindow", "Enter Age"))
        self.label_9.setText(_translate("MainWindow", "Gender:"))
        self.radioButton_2.setText(_translate("MainWindow", "Male"))
        self.radioButton_3.setText(_translate("MainWindow", "female"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.label_5.setText(_translate("MainWindow", "Confirm Password"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.radioButton.setText(_translate("MainWindow", "I agree to the Terms of sevices and privacy policy"))
        self.signupButton.setText(_translate("MainWindow", " Sign Up "))
        self.label_6.setText(_translate("MainWindow", "Aleady have an account?"))
        self.loginButton.setText(_translate("MainWindow", "LogIn Here!"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SignUp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DoctorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1221, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("*{\n"
"color:#000;\n"
"border:none;\n"
"}\n"
"\n"
"#ProfileCont{\n"
"border-radius: 20px;\n"
"background-color:#fefeff;\n"
"}\n"
"#recordButton, #reservationbutton,#settingsbutton, #logoutButton, #profileButton, #confirmButton{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 18px;\n"
"}\n"
" #logoutButton, #profileButton{\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 10pt;\n"
"}\n"
"#homebutton{\n"
"background-color: #fefeff;\n"
"padding:10px 5px;\n"
"text-align:left;\n"
"font: 18px;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"#card1,#card2{\n"
"border-radius: 20px;\n"
"background-color:#eff9fe;\n"
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
"#leftmenu{\n"
"background-color: #2596be;\n"
"}\n"
"\n"
"#rightmenu{\n"
"background-color: #eff9fe;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: transparent;\n"
"color:#2596be;\n"
"}\n"
"\n"
"#SearchFrame{\n"
"border-radius: 10px;\n"
"border: 2px solid #2596be;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftmenu = QtWidgets.QWidget(self.centralwidget)
        self.leftmenu.setObjectName("leftmenu")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.leftmenu)
        self.verticalLayout_7.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.leftmenu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setContentsMargins(44, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.verticalLayout_8.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.leftmenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setContentsMargins(18, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 18)
        self.verticalLayout_9.setSpacing(21)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.homebutton = QtWidgets.QPushButton(self.frame_7)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebutton.setIcon(icon)
        self.homebutton.setIconSize(QtCore.QSize(24, 24))
        self.homebutton.setObjectName("homebutton")
        self.verticalLayout_9.addWidget(self.homebutton)
        self.reservationbutton = QtWidgets.QPushButton(self.frame_7)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Icons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reservationbutton.setIcon(icon1)
        self.reservationbutton.setIconSize(QtCore.QSize(24, 24))
        self.reservationbutton.setObjectName("reservationbutton")
        self.verticalLayout_9.addWidget(self.reservationbutton)
        self.recordButton = QtWidgets.QPushButton(self.frame_7)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Icons/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon2)
        self.recordButton.setIconSize(QtCore.QSize(24, 24))
        self.recordButton.setObjectName("recordButton")
        self.verticalLayout_9.addWidget(self.recordButton)
        self.settingsbutton = QtWidgets.QPushButton(self.frame_7)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsbutton.setIcon(icon3)
        self.settingsbutton.setIconSize(QtCore.QSize(24, 24))
        self.settingsbutton.setObjectName("settingsbutton")
        self.verticalLayout_9.addWidget(self.settingsbutton)
        self.verticalLayout_10.addWidget(self.frame_7, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.leftmenu)
        self.rightmenu = QtWidgets.QWidget(self.centralwidget)
        self.rightmenu.setObjectName("rightmenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightmenu)
        self.verticalLayout.setContentsMargins(28, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerframe = QtWidgets.QWidget(self.rightmenu)
        self.headerframe.setObjectName("headerframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerframe)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerframe)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.menuButton.setFont(font)
        self.menuButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon4)
        self.menuButton.setIconSize(QtCore.QSize(24, 24))
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout_3.addWidget(self.menuButton)
        self.appheader = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.appheader.setFont(font)
        self.appheader.setObjectName("appheader")
        self.horizontalLayout_3.addWidget(self.appheader)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_2 = QtWidgets.QWidget(self.headerframe)
        self.widget_2.setMinimumSize(QtCore.QSize(331, 0))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(44, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SearchFrame = QtWidgets.QFrame(self.widget_2)
        self.SearchFrame.setMinimumSize(QtCore.QSize(295, 0))
        self.SearchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchFrame.setObjectName("SearchFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.SearchFrame)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Icons/Icons/search.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.SearchFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_4.addWidget(self.SearchFrame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.confirmButton = QtWidgets.QPushButton(self.headerframe)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_2.addWidget(self.confirmButton)
        self.widget_3 = QtWidgets.QWidget(self.headerframe)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.accountButton = QtWidgets.QPushButton(self.widget_3)
        self.accountButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/Icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountButton.setIcon(icon5)
        self.accountButton.setIconSize(QtCore.QSize(32, 32))
        self.accountButton.setObjectName("accountButton")
        self.horizontalLayout_6.addWidget(self.accountButton)
        self.horizontalLayout_2.addWidget(self.widget_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerframe, 0, QtCore.Qt.AlignTop)
        self.mainframe = QtWidgets.QWidget(self.rightmenu)
        self.mainframe.setObjectName("mainframe")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.mainframe)
        self.horizontalLayout_7.setContentsMargins(72, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.card1 = QtWidgets.QFrame(self.mainframe)
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.card1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(76, 76))
        self.label.setMaximumSize(QtCore.QSize(74, 76))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/bi-without.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.vitalsign = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.vitalsign.setFont(font)
        self.vitalsign.setObjectName("vitalsign")
        self.horizontalLayout_9.addWidget(self.vitalsign, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.vitalLabel = QtWidgets.QLabel(self.card1)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.vitalLabel.setFont(font)
        self.vitalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.vitalLabel.setObjectName("vitalLabel")
        self.verticalLayout_2.addWidget(self.vitalLabel, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.card1)
        self.card2 = QtWidgets.QFrame(self.mainframe)
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.card2)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Icons/stop.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_7.addWidget(self.card2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.mainframe)
        self.cardsframe = QtWidgets.QWidget(self.rightmenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardsframe.sizePolicy().hasHeightForWidth())
        self.cardsframe.setSizePolicy(sizePolicy)
        self.cardsframe.setObjectName("cardsframe")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.cardsframe)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_4 = QtWidgets.QWidget(self.cardsframe)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.widget_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(30, 30))
        self.label_6.setMaximumSize(QtCore.QSize(30, 30))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/Icons/Icons/activity.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.EMGlabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.EMGlabel.setFont(font)
        self.EMGlabel.setObjectName("EMGlabel")
        self.horizontalLayout_12.addWidget(self.EMGlabel)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView = PlotWidget(self.frame_3)
        self.graphicsView.setMinimumSize(QtCore.QSize(400, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_6.addWidget(self.graphicsView)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.horizontalLayout_11.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.cardsframe)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_11 = QtWidgets.QFrame(self.widget_6)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        self.label_8.setMinimumSize(QtCore.QSize(30, 30))
        self.label_8.setMaximumSize(QtCore.QSize(30, 30))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Icons/Icons/filter.svg"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.filterflex = QtWidgets.QLabel(self.frame_11)
        self.filterflex.setMinimumSize(QtCore.QSize(82, 0))
        self.filterflex.setMaximumSize(QtCore.QSize(82, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.filterflex.setFont(font)
        self.filterflex.setScaledContents(False)
        self.filterflex.setObjectName("filterflex")
        self.horizontalLayout_8.addWidget(self.filterflex)
        self.comboBox = QtWidgets.QComboBox(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(44, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(44, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_8.addWidget(self.lineEdit_3)
        self.verticalLayout_13.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.widget_6)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_12)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_17.addWidget(self.tableWidget)
        self.verticalLayout_13.addWidget(self.frame_12)
        self.horizontalLayout_11.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.cardsframe)
        self.horizontalLayout.addWidget(self.rightmenu)
        self.ProfileCont = QtWidgets.QWidget(self.centralwidget)
        self.ProfileCont.setMinimumSize(QtCore.QSize(100, 0))
        self.ProfileCont.setObjectName("ProfileCont")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.ProfileCont)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_8 = QtWidgets.QFrame(self.ProfileCont)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.DrName = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DrName.setFont(font)
        self.DrName.setAlignment(QtCore.Qt.AlignCenter)
        self.DrName.setObjectName("DrName")
        self.verticalLayout_12.addWidget(self.DrName, 0, QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setMaximumSize(QtCore.QSize(50, 50))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Icons/TCCD group.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_12.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.profileButton = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.profileButton.setFont(font)
        self.profileButton.setIcon(icon5)
        self.profileButton.setObjectName("profileButton")
        self.verticalLayout_12.addWidget(self.profileButton)
        self.logoutButton = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logoutButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/Icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutButton.setIcon(icon6)
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout_12.addWidget(self.logoutButton)
        self.verticalLayout_11.addWidget(self.frame_8, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.ProfileCont, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Main Menu"))
        self.homebutton.setText(_translate("MainWindow", "Home"))
        self.reservationbutton.setText(_translate("MainWindow", "Reserve"))
        self.recordButton.setText(_translate("MainWindow", "Records"))
        self.settingsbutton.setText(_translate("MainWindow", "Settings"))
        self.appheader.setText(_translate("MainWindow", " MediTrack"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Name/ ID"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
        self.vitalsign.setText(_translate("MainWindow", "Flexions"))
        self.vitalLabel.setText(_translate("MainWindow", "0"))
        self.EMGlabel.setText(_translate("MainWindow", "EMG Signal"))
        self.filterflex.setText(_translate("MainWindow", "Flexions"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Equal to"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Greater than"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Less than"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.DrName.setText(_translate("MainWindow", "Dr.Ahmed"))
        self.profileButton.setText(_translate("MainWindow", "My Profile"))
        self.logoutButton.setText(_translate("MainWindow", "Logout"))
from pyqtgraph import PlotWidget
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CRMWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CRMWindow(object):
    def setupUi(self, CRMWindow):
        if not CRMWindow.objectName():
            CRMWindow.setObjectName(u"CRMWindow")
        CRMWindow.resize(768, 279)
        self.centralwidget = QWidget(CRMWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 721, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 50, 721, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leBookId = QLineEdit(self.horizontalLayoutWidget_2)
        self.leBookId.setObjectName(u"leBookId")
        self.leBookId.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.leBookId)

        self.leBookName = QLineEdit(self.horizontalLayoutWidget_2)
        self.leBookName.setObjectName(u"leBookName")

        self.horizontalLayout_2.addWidget(self.leBookName)

        self.leAuthor = QLineEdit(self.horizontalLayoutWidget_2)
        self.leAuthor.setObjectName(u"leAuthor")

        self.horizontalLayout_2.addWidget(self.leAuthor)

        self.leYear = QLineEdit(self.horizontalLayoutWidget_2)
        self.leYear.setObjectName(u"leYear")

        self.horizontalLayout_2.addWidget(self.leYear)

        self.leRating = QLineEdit(self.horizontalLayoutWidget_2)
        self.leRating.setObjectName(u"leRating")

        self.horizontalLayout_2.addWidget(self.leRating)

        self.pbAddBook = QPushButton(self.centralwidget)
        self.pbAddBook.setObjectName(u"pbAddBook")
        self.pbAddBook.setEnabled(False)
        self.pbAddBook.setGeometry(QRect(20, 90, 141, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 150, 141, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 150, 141, 16))
        self.leSearchValue = QLineEdit(self.centralwidget)
        self.leSearchValue.setObjectName(u"leSearchValue")
        self.leSearchValue.setGeometry(QRect(20, 170, 139, 22))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 170, 139, 22))
        self.pbSearch = QPushButton(self.centralwidget)
        self.pbSearch.setObjectName(u"pbSearch")
        self.pbSearch.setGeometry(QRect(20, 200, 141, 31))
        CRMWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CRMWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 768, 21))
        CRMWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CRMWindow)
        self.statusbar.setObjectName(u"statusbar")
        CRMWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CRMWindow)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CRMWindow)
    # setupUi

    def retranslateUi(self, CRMWindow):
        CRMWindow.setWindowTitle(QCoreApplication.translate("CRMWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("CRMWindow", u"BookId", None))
        self.label_3.setText(QCoreApplication.translate("CRMWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("CRMWindow", u"Author", None))
        self.label.setText(QCoreApplication.translate("CRMWindow", u"Year", None))
        self.label_5.setText(QCoreApplication.translate("CRMWindow", u"Rating", None))
        self.pbAddBook.setText(QCoreApplication.translate("CRMWindow", u"Add Book", None))
        self.label_6.setText(QCoreApplication.translate("CRMWindow", u"Search Value", None))
        self.label_7.setText(QCoreApplication.translate("CRMWindow", u"Search Field", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CRMWindow", u"Name", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("CRMWindow", u"Author", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("CRMWindow", u"Year", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("CRMWindow", u"Rating", None))

        self.pbSearch.setText(QCoreApplication.translate("CRMWindow", u"Search", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.countrySelect = QtWidgets.QLabel(self.centralwidget)
        self.countrySelect.setGeometry(QtCore.QRect(20, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.countrySelect.setFont(font)
        self.countrySelect.setObjectName("countrySelect")
        self.countryList = QtWidgets.QListWidget(self.centralwidget)
        self.countryList.setGeometry(QtCore.QRect(10, 60, 210, 192))
        self.countryList.setObjectName("countryList")
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(20, 260, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.searchLabel.setFont(font)
        self.searchLabel.setObjectName("searchLabel")
        self.searchCountry = QtWidgets.QTextEdit(self.centralwidget)
        self.searchCountry.setGeometry(QtCore.QRect(10, 290, 210, 41))
        self.searchCountry.setObjectName("searchCountry")
        self.countryLabel = QtWidgets.QLabel(self.centralwidget)
        self.countryLabel.setGeometry(QtCore.QRect(260, 90, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.casesTotalLabel = QtWidgets.QLabel(self.centralwidget)
        self.casesTotalLabel.setGeometry(QtCore.QRect(260, 330, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.casesTotalLabel.setFont(font)
        self.casesTotalLabel.setObjectName("casesTotalLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(260, 60, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.deathTotalLabel = QtWidgets.QLabel(self.centralwidget)
        self.deathTotalLabel.setGeometry(QtCore.QRect(260, 360, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deathTotalLabel.setFont(font)
        self.deathTotalLabel.setObjectName("deathTotalLabel")
        self.firstDeathLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstDeathLabel.setGeometry(QtCore.QRect(260, 120, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.firstDeathLabel.setFont(font)
        self.firstDeathLabel.setObjectName("firstDeathLabel")
        self.generalData = QtWidgets.QLabel(self.centralwidget)
        self.generalData.setGeometry(QtCore.QRect(260, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.generalData.setFont(font)
        self.generalData.setObjectName("generalData")
        self.selectedCountry = QtWidgets.QLabel(self.centralwidget)
        self.selectedCountry.setGeometry(QtCore.QRect(360, 90, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedCountry.setFont(font)
        self.selectedCountry.setObjectName("selectedCountry")
        self.selectedDate = QtWidgets.QLabel(self.centralwidget)
        self.selectedDate.setGeometry(QtCore.QRect(360, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedDate.setFont(font)
        self.selectedDate.setObjectName("selectedDate")
        self.selectedTotalCases = QtWidgets.QLabel(self.centralwidget)
        self.selectedTotalCases.setGeometry(QtCore.QRect(360, 330, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedTotalCases.setFont(font)
        self.selectedTotalCases.setObjectName("selectedTotalCases")
        self.selectedFirstCase = QtWidgets.QLabel(self.centralwidget)
        self.selectedFirstCase.setGeometry(QtCore.QRect(360, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedFirstCase.setFont(font)
        self.selectedFirstCase.setObjectName("selectedFirstCase")
        self.selectedTotalDeaths = QtWidgets.QLabel(self.centralwidget)
        self.selectedTotalDeaths.setGeometry(QtCore.QRect(360, 360, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedTotalDeaths.setFont(font)
        self.selectedTotalDeaths.setObjectName("selectedTotalDeaths")
        self.lastDayDataLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastDayDataLabel.setGeometry(QtCore.QRect(260, 150, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lastDayDataLabel.setFont(font)
        self.lastDayDataLabel.setObjectName("lastDayDataLabel")
        self.casesLabel = QtWidgets.QLabel(self.centralwidget)
        self.casesLabel.setGeometry(QtCore.QRect(260, 180, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.casesLabel.setFont(font)
        self.casesLabel.setObjectName("casesLabel")
        self.deathsLabe = QtWidgets.QLabel(self.centralwidget)
        self.deathsLabe.setGeometry(QtCore.QRect(260, 240, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deathsLabe.setFont(font)
        self.deathsLabe.setObjectName("deathsLabe")
        self.lastDayDataLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.lastDayDataLabel_2.setGeometry(QtCore.QRect(260, 300, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lastDayDataLabel_2.setFont(font)
        self.lastDayDataLabel_2.setObjectName("lastDayDataLabel_2")
        self.selectedLastDayCases = QtWidgets.QLabel(self.centralwidget)
        self.selectedLastDayCases.setGeometry(QtCore.QRect(360, 180, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedLastDayCases.setFont(font)
        self.selectedLastDayCases.setObjectName("selectedLastDayCases")
        self.selectedLastDayDeaths = QtWidgets.QLabel(self.centralwidget)
        self.selectedLastDayDeaths.setGeometry(QtCore.QRect(360, 240, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedLastDayDeaths.setFont(font)
        self.selectedLastDayDeaths.setObjectName("selectedLastDayDeaths")
        self.casesPercentLabel = QtWidgets.QLabel(self.centralwidget)
        self.casesPercentLabel.setGeometry(QtCore.QRect(260, 210, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.casesPercentLabel.setFont(font)
        self.casesPercentLabel.setObjectName("casesPercentLabel")
        self.selectedPercentDayCases = QtWidgets.QLabel(self.centralwidget)
        self.selectedPercentDayCases.setGeometry(QtCore.QRect(360, 210, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedPercentDayCases.setFont(font)
        self.selectedPercentDayCases.setObjectName("selectedPercentDayCases")
        self.deathsPercentLabel = QtWidgets.QLabel(self.centralwidget)
        self.deathsPercentLabel.setGeometry(QtCore.QRect(260, 270, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deathsPercentLabel.setFont(font)
        self.deathsPercentLabel.setObjectName("deathsPercentLabel")
        self.selectedPercentDayDeaths = QtWidgets.QLabel(self.centralwidget)
        self.selectedPercentDayDeaths.setGeometry(QtCore.QRect(360, 270, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectedPercentDayDeaths.setFont(font)
        self.selectedPercentDayDeaths.setObjectName("selectedPercentDayDeaths")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVID-19 report creator"))
        self.countrySelect.setText(_translate("MainWindow", "Select country:"))
        self.searchLabel.setText(_translate("MainWindow", "Search:"))
        self.countryLabel.setText(_translate("MainWindow", "Country:"))
        self.casesTotalLabel.setText(_translate("MainWindow", "Total cases:"))
        self.dateLabel.setText(_translate("MainWindow", "Date:"))
        self.deathTotalLabel.setText(_translate("MainWindow", "Deaths:"))
        self.firstDeathLabel.setText(_translate("MainWindow", "First case:"))
        self.generalData.setText(_translate("MainWindow", "General data:"))
        self.selectedCountry.setText(_translate("MainWindow", "N/A"))
        self.selectedDate.setText(_translate("MainWindow", "N/A"))
        self.selectedTotalCases.setText(_translate("MainWindow", "N/A"))
        self.selectedFirstCase.setText(_translate("MainWindow", "N/A"))
        self.selectedTotalDeaths.setText(_translate("MainWindow", "N/A"))
        self.lastDayDataLabel.setText(_translate("MainWindow", "Last day increase:"))
        self.casesLabel.setText(_translate("MainWindow", "Cases:"))
        self.deathsLabe.setText(_translate("MainWindow", "Deaths:"))
        self.lastDayDataLabel_2.setText(_translate("MainWindow", "Total:"))
        self.selectedLastDayCases.setText(_translate("MainWindow", "N/A"))
        self.selectedLastDayDeaths.setText(_translate("MainWindow", "N/A"))
        self.casesPercentLabel.setText(_translate("MainWindow", "Cases %:"))
        self.selectedPercentDayCases.setText(_translate("MainWindow", "N/A"))
        self.deathsPercentLabel.setText(_translate("MainWindow", "Deaths %:"))
        self.selectedPercentDayDeaths.setText(_translate("MainWindow", "N/A"))
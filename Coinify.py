from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Find_price import get_stuff


class Ui_MainWindow(object):
    def __init__(self):

        self.price_dict = {"Bitcoin": None, "Ethereum": None,
                           "Ripple": None, "Bitcoin Cash": None, "Bitcoin SV": None}

        self.btc_price_change = None
        self.eth_price_change = None
        self.xrp_price_change = None
        self.bch_price_change = None
        self.bsv_price_change = None
        self.icon = r"Coinify\Images\Coinify.png"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 460)
        MainWindow.setMinimumSize(QtCore.QSize(730, 460))
        MainWindow.setMaximumSize(QtCore.QSize(730, 460))
        MainWindow.setWindowIcon(QtGui.QIcon(self.icon))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Logos

        self.BTC = QtWidgets.QLabel(self.centralwidget)
        self.BTC.setGeometry(QtCore.QRect(30, 40, 50, 50))
        self.BTC.setText("")
        self.BTC.setPixmap(QtGui.QPixmap(r"Coinify\Images\btc.png"))
        self.BTC.setWordWrap(True)
        self.BTC.setObjectName("BTC")
        self.ETH = QtWidgets.QLabel(self.centralwidget)
        self.ETH.setGeometry(QtCore.QRect(30, 120, 50, 50))
        self.ETH.setText("")
        self.ETH.setPixmap(QtGui.QPixmap(r"Coinify\Images\eth.png"))
        self.ETH.setScaledContents(True)
        self.ETH.setWordWrap(True)
        self.ETH.setObjectName("ETH")
        self.XRP = QtWidgets.QLabel(self.centralwidget)
        self.XRP.setGeometry(QtCore.QRect(30, 200, 50, 50))
        self.XRP.setText("")
        self.XRP.setPixmap(QtGui.QPixmap(r"Coinify\Images\xrp.png"))
        self.XRP.setScaledContents(True)
        self.XRP.setWordWrap(True)
        self.XRP.setObjectName("XRP")
        self.BCH = QtWidgets.QLabel(self.centralwidget)
        self.BCH.setGeometry(QtCore.QRect(30, 280, 50, 50))
        self.BCH.setText("")
        self.BCH.setPixmap(QtGui.QPixmap(r"Coinify\Images\bch.png"))
        self.BCH.setScaledContents(True)
        self.BCH.setWordWrap(True)
        self.BCH.setObjectName("BCH")
        self.BSV = QtWidgets.QLabel(self.centralwidget)
        self.BSV.setGeometry(QtCore.QRect(30, 360, 50, 50))
        self.BSV.setText("")
        self.BSV.setPixmap(QtGui.QPixmap(r"Coinify\Images\bsv.png"))
        self.BSV.setScaledContents(True)
        self.BSV.setWordWrap(True)
        self.BSV.setObjectName("BSV")

        # Name

        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(108, 10, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.Bitcoin = QtWidgets.QLabel(self.centralwidget)
        self.Bitcoin.setGeometry(QtCore.QRect(101, 57, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Bitcoin.setFont(font)
        self.Bitcoin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bitcoin.setAlignment(QtCore.Qt.AlignCenter)
        self.Bitcoin.setObjectName("Bitcoin")
        self.Ethereum = QtWidgets.QLabel(self.centralwidget)
        self.Ethereum.setGeometry(QtCore.QRect(102, 136, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ethereum.setFont(font)
        self.Ethereum.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Ethereum.setAlignment(QtCore.Qt.AlignCenter)
        self.Ethereum.setObjectName("Ethereum")
        self.Ripple = QtWidgets.QLabel(self.centralwidget)
        self.Ripple.setGeometry(QtCore.QRect(103, 217, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ripple.setFont(font)
        self.Ripple.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Ripple.setAlignment(QtCore.Qt.AlignCenter)
        self.Ripple.setObjectName("Ripple")
        self.BitcoinCash = QtWidgets.QLabel(self.centralwidget)
        self.BitcoinCash.setGeometry(QtCore.QRect(101, 297, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BitcoinCash.setFont(font)
        self.BitcoinCash.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BitcoinCash.setAlignment(QtCore.Qt.AlignCenter)
        self.BitcoinCash.setObjectName("BitcoinCash")
        self.BitcoinSV = QtWidgets.QLabel(self.centralwidget)
        self.BitcoinSV.setGeometry(QtCore.QRect(97, 375, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BitcoinSV.setFont(font)
        self.BitcoinSV.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BitcoinSV.setAlignment(QtCore.Qt.AlignCenter)
        self.BitcoinSV.setObjectName("BitcoinSV")

        # Price

        self.Price = QtWidgets.QLabel(self.centralwidget)
        self.Price.setGeometry(QtCore.QRect(326, 10, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Price.setFont(font)
        self.Price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Price.setAlignment(QtCore.Qt.AlignCenter)
        self.Price.setObjectName("Price")

        self.Percent = QtWidgets.QLabel(self.centralwidget)
        self.Percent.setGeometry(QtCore.QRect(536, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Percent.setFont(font)
        self.Percent.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Percent.setAlignment(QtCore.Qt.AlignCenter)
        self.Percent.setObjectName("Percent")

        self.Bitcoin_price = QtWidgets.QLabel(self.centralwidget)
        self.Bitcoin_price.setGeometry(QtCore.QRect(320, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Bitcoin_price.setFont(font)
        self.Bitcoin_price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bitcoin_price.setText("")
        self.Bitcoin_price.setAlignment(QtCore.Qt.AlignCenter)
        self.Bitcoin_price.setObjectName("Bitcoin_price")

        self.Ethereum_price = QtWidgets.QLabel(self.centralwidget)
        self.Ethereum_price.setGeometry(QtCore.QRect(320, 137, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ethereum_price.setFont(font)
        self.Ethereum_price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Ethereum_price.setText("")
        self.Ethereum_price.setAlignment(QtCore.Qt.AlignCenter)
        self.Ethereum_price.setObjectName("Ethereum_price")

        self.Ripple_price = QtWidgets.QLabel(self.centralwidget)
        self.Ripple_price.setGeometry(QtCore.QRect(320, 215, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ripple_price.setFont(font)
        self.Ripple_price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Ripple_price.setText("")
        self.Ripple_price.setAlignment(QtCore.Qt.AlignCenter)
        self.Ripple_price.setObjectName("Ripple_price")

        self.BitcoinCash_price = QtWidgets.QLabel(self.centralwidget)
        self.BitcoinCash_price.setGeometry(QtCore.QRect(320, 297, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BitcoinCash_price.setFont(font)
        self.BitcoinCash_price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BitcoinCash_price.setText("")
        self.BitcoinCash_price.setAlignment(QtCore.Qt.AlignCenter)
        self.BitcoinCash_price.setObjectName("BitcoinCash_price")

        self.BitcoinSV_price = QtWidgets.QLabel(self.centralwidget)
        self.BitcoinSV_price.setGeometry(QtCore.QRect(320, 374, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BitcoinSV_price.setFont(font)
        self.BitcoinSV_price.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BitcoinSV_price.setText("")
        self.BitcoinSV_price.setAlignment(QtCore.Qt.AlignCenter)
        self.BitcoinSV_price.setObjectName("BitcoinSV_price")
        self.BitcoinSV_change = QtWidgets.QLabel(self.centralwidget)
        self.BitcoinSV_change.setGeometry(QtCore.QRect(550, 370, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BitcoinSV_change.setFont(font)
        self.BitcoinSV_change.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BitcoinSV_change.setText("")
        self.BitcoinSV_change.setAlignment(QtCore.Qt.AlignCenter)
        self.BitcoinSV_change.setObjectName("BitcoinSV_change")
        self.Bitcoin_change = QtWidgets.QLabel(self.centralwidget)
        self.Bitcoin_change.setGeometry(QtCore.QRect(550, 56, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Bitcoin_change.setFont(font)
        self.Bitcoin_change.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bitcoin_change.setText("")
        self.Bitcoin_change.setAlignment(QtCore.Qt.AlignCenter)
        self.Bitcoin_change.setObjectName("Bitcoin_change")
        self.Ethereum_change = QtWidgets.QLabel(self.centralwidget)
        self.Ethereum_change.setGeometry(QtCore.QRect(550, 133, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ethereum_change.setFont(font)
        self.Ethereum_change.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Ethereum_change.setText("")
        self.Ethereum_change.setAlignment(QtCore.Qt.AlignCenter)
        self.Ethereum_change.setObjectName("Ethereum_change")
        self.BitcoinCash_change = QtWidgets.QLabel(self.centralwidget)
        self.BitcoinCash_change.setGeometry(QtCore.QRect(550, 293, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BitcoinCash_change.setFont(font)
        self.BitcoinCash_change.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BitcoinCash_change.setText("")
        self.BitcoinCash_change.setAlignment(QtCore.Qt.AlignCenter)
        self.BitcoinCash_change.setObjectName("BitcoinCash_change")
        self.Ripple_change = QtWidgets.QLabel(self.centralwidget)
        self.Ripple_change.setGeometry(QtCore.QRect(550, 211, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ripple_change.setFont(font)
        self.Ripple_change.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Ripple_change.setText("")
        self.Ripple_change.setAlignment(QtCore.Qt.AlignCenter)
        self.Ripple_change.setObjectName("Ripple_change")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuAlert = QtWidgets.QMenu(self.menubar)
        self.menuAlert.setObjectName("menuAlert")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.triggered.connect(lambda x: self.reset('All'))

        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.triggered.connect(self.help)

        self.actionBitcoin = QtWidgets.QAction(MainWindow)
        self.actionBitcoin.setCheckable(True)
        self.actionBitcoin.setObjectName("actionBitcoin")
        self.actionBitcoin.triggered.connect(
            lambda x: self.alert("Bitcoin", self.actionBitcoin))

        self.actionEthereum = QtWidgets.QAction(MainWindow)
        self.actionEthereum.setCheckable(True)
        self.actionEthereum.setObjectName("actionEthereum")
        self.actionEthereum.triggered.connect(
            lambda x: self.alert("Ethereum", self.actionEthereum))

        self.actionRipple = QtWidgets.QAction(MainWindow)
        self.actionRipple.setCheckable(True)
        self.actionRipple.setObjectName("actionRipple")
        self.actionRipple.triggered.connect(
            lambda x: self.alert("Ripple", self.actionRipple))

        self.actionBitcoin_Cash = QtWidgets.QAction(MainWindow)
        self.actionBitcoin_Cash.setCheckable(True)
        self.actionBitcoin_Cash.setObjectName("actionBitcoin_Cash")
        self.actionBitcoin_Cash.triggered.connect(
            lambda x: self.alert("Bitcoin Cash", self.actionBitcoin_Cash))

        self.actionBitcoin_SV = QtWidgets.QAction(MainWindow)
        self.actionBitcoin_SV.setCheckable(True)
        self.actionBitcoin_SV.setObjectName("actionBitcoin_SV")
        self.actionBitcoin_SV.triggered.connect(
            lambda x: self.alert("Bitcoin SV", self.actionBitcoin_SV))

        self.menuSetting.addAction(self.actionReset)
        self.menuSetting.addAction(self.actionHelp)
        self.menuAlert.addAction(self.actionBitcoin)
        self.menuAlert.addAction(self.actionEthereum)
        self.menuAlert.addAction(self.actionRipple)
        self.menuAlert.addAction(self.actionBitcoin_Cash)
        self.menuAlert.addAction(self.actionBitcoin_SV)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuAlert.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.reset()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coinify"))
        self.Name.setText(_translate("MainWindow", "نام رمزارز"))
        self.Bitcoin.setText(_translate("MainWindow", "Bitcoin"))
        self.Ethereum.setText(_translate("MainWindow", "Ethereum"))
        self.Ripple.setText(_translate("MainWindow", "Ripple"))
        self.BitcoinCash.setText(_translate("MainWindow", "Bitcoin Cash"))
        self.BitcoinSV.setText(_translate("MainWindow", "Bitcoin SV"))
        self.Price.setText(_translate("MainWindow", "قیمت"))
        self.Percent.setText(_translate("MainWindow", "درصد تغییرات"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuAlert.setTitle(_translate("MainWindow", "Alert"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionBitcoin.setText(_translate("MainWindow", "Bitcoin"))
        self.actionEthereum.setText(_translate("MainWindow", "Ethereum"))
        self.actionRipple.setText(_translate("MainWindow", "Ripple"))
        self.actionBitcoin_Cash.setText(
            _translate("MainWindow", "Bitcoin Cash"))
        self.actionBitcoin_SV.setText(_translate("MainWindow", "Bitcoin SV"))

    # Fetch data from Find_price function

    def reset(self, item='All'):

        # All
        if item == 'All':
            QtWidgets.QApplication.processEvents()
            self.price_dict["Bitcoin"] = round(
                float(get_stuff()[0]['quote']['USD']['price']), 2)
            self.btc_price_change = round(float(get_stuff()[0]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.Bitcoin_price.setText(str(self.price_dict["Bitcoin"]) + ' $')
            self.Bitcoin_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.Bitcoin_change.setText(str(self.btc_price_change) + ' %')
            self.Bitcoin_change.adjustSize()
            if float(self.btc_price_change) < 0:
                self.Bitcoin_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.Bitcoin_change.setStyleSheet("color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

            self.price_dict["Ethereum"] = round(
                float(get_stuff()[1]['quote']['USD']['price']), 2)
            self.eth_price_change = round(float(get_stuff()[1]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.Ethereum_price.setText(
                str(self.price_dict["Ethereum"]) + ' $')
            self.Ethereum_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.Ethereum_change.setText(str(self.eth_price_change) + ' %')
            self.Ethereum_change.adjustSize()
            if float(self.eth_price_change) < 0:
                self.Ethereum_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.Ethereum_change.setStyleSheet("color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

            self.price_dict["Ripple"] = round(
                float(get_stuff()[2]['quote']['USD']['price']), 2)
            self.xrp_price_change = round(float(get_stuff()[2]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.Ripple_price.setText(str(self.price_dict["Ripple"]) + ' $')
            self.Ripple_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.Ripple_change.setText(str(self.xrp_price_change) + ' %')
            self.Ripple_change.adjustSize()
            if float(self.xrp_price_change) < 0:
                self.Ripple_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.Ripple_change.setStyleSheet("color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

            self.price_dict["Bitcoin Cash"] = round(
                float(get_stuff()[5]['quote']['USD']['price']), 2)
            self.bch_price_change = round(float(get_stuff()[5]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.BitcoinCash_price.setText(
                str(self.price_dict["Bitcoin Cash"]) + ' $')
            self.BitcoinCash_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.BitcoinCash_change.setText(str(self.bch_price_change) + ' %')
            self.BitcoinCash_change.adjustSize()
            if float(self.bch_price_change) < 0:
                self.BitcoinCash_change.setStyleSheet(
                    "color : rgb(255, 0, 0);")
            else:
                self.BitcoinCash_change.setStyleSheet(
                    "color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

            self.price_dict["Bitcoin SV"] = round(
                float(get_stuff()[6]['quote']['USD']['price']), 2)
            self.bsv_price_change = round(float(get_stuff()[6]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.BitcoinSV_price.setText(
                str(self.price_dict["Bitcoin SV"]) + ' $')
            self.BitcoinSV_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.BitcoinSV_change.setText(str(self.bsv_price_change) + ' %')
            self.BitcoinSV_change.adjustSize()
            if float(self.bsv_price_change) < 0:
                self.BitcoinSV_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.BitcoinSV_change.setStyleSheet("color : rgb(60, 210, 0;)")
            QtWidgets.qApp.processEvents()

        # Bitcoin
        if item == 'Bitcoin':
            self.price_dict["Bitcoin"] = round(
                float(get_stuff()[0]['quote']['USD']['price']), 2)
            self.btc_price_change = round(float(get_stuff()[0]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.Bitcoin_price.setText(str(self.price_dict["Bitcoin"]) + ' $')
            self.Bitcoin_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.Bitcoin_change.setText(str(self.btc_price_change) + ' %')
            self.Bitcoin_change.adjustSize()
            if float(self.btc_price_change) < 0:
                self.Bitcoin_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.Bitcoin_change.setStyleSheet("color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

        # Ethereum
        if item == 'Ethereum':
            self.price_dict["Ethereum"] = round(
                float(get_stuff()[1]['quote']['USD']['price']), 2)
            self.eth_price_change = round(float(get_stuff()[1]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.Ethereum_price.setText(
                str(self.price_dict["Ethereum"]) + ' $')
            self.Ethereum_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.Ethereum_change.setText(str(self.eth_price_change) + ' %')
            self.Ethereum_change.adjustSize()
            if float(self.eth_price_change) < 0:
                self.Ethereum_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.Ethereum_change.setStyleSheet("color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

        # Ripple
        if item == 'Ripple':
            self.price_dict["Ripple"] = round(
                float(get_stuff()[2]['quote']['USD']['price']), 2)
            self.xrp_price_change = round(float(get_stuff()[2]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.Ripple_price.setText(str(self.price_dict["Ripple"]) + ' $')
            self.Ripple_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.Ripple_change.setText(str(self.xrp_price_change) + ' %')
            self.Ripple_change.adjustSize()
            if float(self.xrp_price_change) < 0:
                self.Ripple_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.Ripple_change.setStyleSheet("color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

        # Bitcoin Cash
        if item == 'Bitcoin Cash':
            self.price_dict["Bitcoin Cash"] = round(
                float(get_stuff()[4]['quote']['USD']['price']), 2)
            self.bch_price_change = round(float(get_stuff()[4]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.BitcoinCash_price.setText(
                str(self.price_dict["Bitcoin Cash"]) + ' $')
            self.BitcoinCash_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.BitcoinCash_change.setText(str(self.bch_price_change) + ' %')
            self.BitcoinCash_change.adjustSize()
            if float(self.bch_price_change) < 0:
                self.BitcoinCash_change.setStyleSheet(
                    "color : rgb(255, 0, 0);")
            else:
                self.BitcoinCash_change.setStyleSheet(
                    "color : rgb(60, 210, 0);")
            QtWidgets.qApp.processEvents()

        # Bitcoin SV
        if item == "Bitcoin SV":
            self.price_dict["Bitcoin SV"] = round(
                float(get_stuff()[5]['quote']['USD']['price']), 2)
            self.bsv_price_change = round(float(get_stuff()[5]['quote']
                                                ['USD']['percent_change_24h']), 2)
            self.BitcoinSV_price.setText(
                str(self.price_dict["Bitcoin SV"]) + ' $')
            self.BitcoinSV_price.adjustSize()
            QtWidgets.qApp.processEvents()
            self.BitcoinSV_change.setText(str(self.bsv_price_change) + ' %')
            self.BitcoinSV_change.adjustSize()
            if float(self.bsv_price_change) < 0:
                self.BitcoinSV_change.setStyleSheet("color : rgb(255, 0, 0);")
            else:
                self.BitcoinSV_change.setStyleSheet("color : rgb(60, 210, 0;)")
            QtWidgets.qApp.processEvents()

    def alert(self, typeOfButton, button):
        if button.isChecked():
            number_input = QtWidgets.QInputDialog.getInt(MainWindow, "Coinify",
                                                         "Please enter your alert price for %s" % typeOfButton)
            number_price = None
            run = True
            while run:
                for i in self.price_dict:
                    if i == typeOfButton:
                        number_price = self.price_dict[str(i)]
                        break
                    else:
                        print("Failed")
                        break

                if number_input[0] > number_price:
                    pass
                else:
                    print("else")
                    break

            sell = QMessageBox()
            sell.setWindowTitle("Coinify")
            sell.setText("%s is now cheaper than before!" % typeOfButton)
            sell.setWindowIcon(QtGui.QIcon(self.icon))
            sell.exec_()
            button.setChecked(False)

    def help(self):
        help_box = QMessageBox()
        help_box.setWindowTitle("Coinify")
        help_box.setText(
            "By using this application,you can keep track of the top 5 crypto currencies including Bitcoin,Ethereum,Ripple,Bitcoin cash and Bitcoin SV based on there price or popularity.\nYou can refresh prices by either clicking reset from the Setting menu or press and hold Ctrl+r.\nThis app in still in development status,so if you see any error or bug,please feel free to contact us")
        help_box.setIcon(QMessageBox.Information)
        help_box.setWindowIcon(QtGui.QIcon(self.icon))
        help_box.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.reset()
    MainWindow.show()
    sys.exit(app.exec_())

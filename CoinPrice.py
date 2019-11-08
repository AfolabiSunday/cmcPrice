from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import requests

main, _ = loadUiType('newPrice.ui')

class MainAll(QMainWindow, main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(359, 568)
        self.show()
        for i in range(1, 100):
            self.comboBox.addItem(str(i))

        self.pushButton.clicked.connect(self.cmc_api_func)


    def cmc_api_func(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '',
            'limit': '1',
            'convert': 'NGN'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'a8f73877-e12b-4e93-9683-e213e4a42379',
        }
        parameters['start'] = self.comboBox.currentText()
        page = requests.get(url, parameters, headers=headers).json()
        price = page['data'][0]['quote']['NGN']['price']
        name = page['data'][0]['name']
        rank = page['data'][0]['cmc_rank']
        max_sup = page['data'][0]['max_supply']
        int_page = int(price)
        int_page2 = ("The price for " + str(name).upper() + " is N" + str(int_page) + " and it Ranked " + str(rank) + " With a Max Supply of " + str(max_sup))
        self.textEdit.setText(int_page2)




def RunMain():
    app =QApplication(sys.argv)
    window = MainAll()
    window.show()
    app.exec()


if __name__ == '__main__':
    RunMain()
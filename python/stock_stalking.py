#!/usr/bin/env python

import requests
import logging
import configparser
import sys

class StockStalking:
    """
    This class is inteded to be a function class for use in interacting with the alpha advantage stock api
    """

    def __init__(self):
        """
        Intantiate the class
        """
        config = configparser.ConfigParser()
        config.read('stock_stalking.ini')
        url = config['General']['url']
        self.api_key = config['General']['api_key']
        self.logfile = config['General']['logfile']
        # https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo
        self.url = url + '/query?function=' + config['Data']['function'] + '&symbol=' + config['Data']['symbol'] + '&apikey=' + self.api_key 

    def get_data(self, url=""):
        """
        Function which takes the full url and returns the data dictionary.
        Utilizes the requests package.
        You can either pass in a URL or use one predefined in the config file.
        """
        # Check if variable contains anything
        try:
            if url:
                r = requests.get(url)
            else:
                r = requests.get(self.url)
        except:
                logging.error("No URL specified")
                sys.exit(2)  

        # Exctract data and return dict
        return r.json()
        

def main():
    ss = StockStalking()
    print(ss.url)
    data = ss.get_data()
    print(data)
    for item in data['Time Series (Daily)']:
        print(item)
        print(data['Time Series (Daily)'][item])

if __name__ == '__main__':
    main()
    
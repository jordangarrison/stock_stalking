#!/usr/bin/env python

import requests
import yaml
import logging

class StockStalking:
    """
    This class is inteded to be a function class for use in interacting with the alpha advantage stock api
    """

    def __init__(self):
        """
        Intantiate the class
        """
        self.url = "www.github.com"

def main():
    ss = StockStalking()
    try:
        r = requests.get("https://www.yelp.com")
        print(r.content)
    except:
        print("Error on request")

if __name__ == '__main__':
    main()
    
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
    r = requests.get("http://www.github.com")
    print(r.content)

if __name__ == '__main__':
    main()
    
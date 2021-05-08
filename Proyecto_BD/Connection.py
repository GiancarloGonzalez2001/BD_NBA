# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:44:19 2021

@author: gianc
"""

import psycopg2

class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port="5432",dbname="BD_NBA",user="postgres",password="123456")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()
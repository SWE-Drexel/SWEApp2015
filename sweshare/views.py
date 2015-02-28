#from django.shortcuts import render

# Create your views here.

import networkx as net
import matplotlib.pyplot as plot
import sqlite3 as lite
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
# Connect to the database
con = lite.connect('db.sqlite3')
cur = con.cursor()    
row = cur.execute("""SELECT * FROM Node""")
#print 'Connected to database!'
#print 'Error: could not connect'

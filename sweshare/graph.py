import networkx as net
import matplotlib.pyplot as plot
import sqlite3 as lite
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
# Connect to the database
try:
    con = lite.connect('db.sqlite3')
    cur = con.cursor()    
    raw_text = cur.execute('SELECT name, ') #text is the field from the database
    print 'Connected to database!'
except:
    print 'Error: could not connect'
# Remove stop words from text 

stops = set(stopwords.words('english'))
tag_text = []

tokenizer = RegexpTokenizer(r'\w+')
no_punc_text = tokenizer.tokenize(raw_text)

for w in no_punc_text:
        if w.lower() not in stops:
            tag_text.append(w) #non-stop word collected as tag

print tag_text

import os
import urllib.parse
username = urllib.parse.quote_plus('mupotsal')
password = urllib.parse.quote_plus('Usap2017')
class Config(object):
    MONGODB_SETTINGS = {
        'MONGODB_HOST'  : "mongodb+srv://%s:%s@cluster0-dp56j.mongodb.net/FlaskIntro?retryWrites=true&w=majority"%(username, password)
    }
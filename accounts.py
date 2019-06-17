from google.appengine.ext import ndb

class Account(ndb.Model):
    email =  ndb.StringProperty(required=True)
    favourite_bus_codes = ndb.IntegerProperty(required=False)

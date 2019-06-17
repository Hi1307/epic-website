import webapp2
from google.appengine.api import users
from google.appengine.api import urlfetch
import json
import os
import jinja2

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("templates/results.html")
        url = "https://arrivelah.busrouter.sg/?id=08057"
        dictionary = {"url": url,
                      }
        self.response.write(template.render(dictionary))

app = webapp2.WSGIApplication([
    ('/results', ResultsHandler),
], debug=True)

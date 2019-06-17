import webapp2
from google.appengine.api import users
from google.appengine.api import urlfetch
import json
import os
import jinja2
from accounts import Account

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("templates/welcome.html")
        self.response.write(template.render())

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("templates/results.html")
        url = "https://arrivelah.herokuapp.com/?id=08057"
        response = urlfetch.fetch(url)
        content = response.content
        response_as_json = json.loads(content)
        dictionary = {"url": response_as_json,
                      }
        self.response.write(template.render(dictionary))

app = webapp2.WSGIApplication([
    ('/results', ResultsHandler),
    ('/', WelcomeHandler)
], debug=True)

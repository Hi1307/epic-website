import webapp2
from google.appengine.api import users
from google.appengine.api import urlfetch
import json
import os
import jinja2
import accounts

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url("/")
        user = users.get_current_user()
        email = user.nickname()
        dipshit = accounts.Account(email = email)
        dipshit.put()
        dictionary = {"login_url": login_url}
        template = jinja_current_dir.get_template("templates/welcome.html")
        self.response.write(template.render(dictionary))

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

class datastorerHandler(webapp2.RequestHandler):
    def post(self):
        favourite_bus_stop_no = self.request.get("favourite_bus_stop_no")
        user = users.get_current_user()
        email = user.nickname()
        Account_query = accounts.Account.query().filter(accounts.Account.email == email)
        Account = Account_query.fetch()
        Account[2] = favourite_bus_stop_no
        dictionary = {"favourite_bus_stop_no": favourite_bus_stop_no,}
        template = jinja_current_dir.get_template("templates/data_storer.html")
        self.response.write(template.render(dictionary))

app = webapp2.WSGIApplication([
    ('/results', ResultsHandler),
    ('/', WelcomeHandler),
    ('/data_storer', datastorerHandler)
], debug=True)

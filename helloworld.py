"""A simple webapp2 server."""

import webapp2

form='''
Hello, World!
<br><br>Search it ^_^<br>
<input name = "month">
<form action="/testform">
	<input name = "month">
	<input type = "submit" value="Submit">
</form>
'''

months=["January"]

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(form)
    def valid_month(month):
    	if month:
    		cap_month=month.capitalize()
    		if cap_month in months:
    			return cap_month
    			else




application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler)
], debug=True)
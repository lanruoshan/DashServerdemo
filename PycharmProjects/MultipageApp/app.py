import dash
import dash_auth
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#1.create a dash object
app = dash.Dash(__name__)
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True

# Keep this out of source code repository - save in a file or a database
#VALID_USERNAME_PASSWORD_PAIRS = [
  ###  ['shell', '12345']
#]
#auth = dash_auth.BasicAuth(
 #   app,
 #   VALID_USERNAME_PASSWORD_PAIRS
#)

from app import app
from flask import render_template, session, redirect, request
from dropbox import DropboxOAuth2Flow

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/authenticate')    
def authenticate():
    result = dropbox_auth_start(session, request)
    return result

@app.route('/authenticate-finish')
def authenticate_finish():
    oauth_result = get_dropbox_auth_flow(session).finish(request.args)
    session['DROPBOX_KEY'] = oauth_result.access_token
    return redirect("/")

def get_dropbox_auth_flow(session):
    redirect_uri = "http://localhost:5000/authenticate-finish"
    return DropboxOAuth2Flow(
        app.config['DROPBOX_APP_KEY'],
        app.config['DROPBOX_APP_SECRET_KEY'], 
        redirect_uri, 
        session,
        "dropbox-auth-csrf-token")

def dropbox_auth_start(session, request):
    authorize_url = get_dropbox_auth_flow(session).start()
    response = redirect(authorize_url)
    return redirect(authorize_url)

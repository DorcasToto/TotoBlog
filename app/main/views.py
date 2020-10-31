
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import getQuotes



@main.route('/',methods = ['GET'])
def index():
    getquotes = getQuotes()
    return render_template ('index.html',getquotes = getquotes)


    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user,pitches=pitches)   

from flask import render_template,request,redirect,url_for
from . import main
from ..requests import getQuotes



@main.route('/',methods = ['GET'])
def index():
    getquotes = getQuotes()
    return render_template ('index.html',getquotes = getquotes)
    
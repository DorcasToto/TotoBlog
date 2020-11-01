
from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_user,logout_user,login_required,current_user
from ..requests import getQuotes
from .forms import BlogForm
from ..models import Blog

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

@main.route('/blog/newBlog',methods = ['GET','POST'])
@login_required
def newBlog():
    blogForm = BlogForm()
    if blogForm.validate_on_submit():
        titleBlog=blogForm.blogTitle.data
        description = blogForm.blogDescription.data
        newBlog = Blog(title_blog=titleBlog, description=description, user= current_user)
        newBlog.saveBlog()
        return redirect(url_for('main.allBlogs'))
    title = 'New Blog'
    return render_template('newBlog.html', title=title, blog_form=blogForm)


@main.route('/blog/allblogs', methods=['GET', 'POST'])
@login_required
def allBlogs():
    blogs = Blog.getallBlogs()
    return render_template('blogs.html', blogs=blogs)


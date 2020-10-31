from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo

class BlogForm(FlaskForm):

    blogTitle = StringField('Blog Title',validators=[Required()])
    blogDescription = StringField('Description',validators = [Required()])
    submit = SubmitField('Submit')
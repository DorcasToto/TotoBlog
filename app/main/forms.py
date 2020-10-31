rom flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo

class BlogForm(FlaskForm):

    title_blog = StringField('Title')
    description = TextAreaField('Write a Description', validators=[Required()])

    blog_title = StringField('Blog Title',validators=[Required()])
    description = StringField('Description',validators = [Required()])
    submit = SubmitField('Submit')
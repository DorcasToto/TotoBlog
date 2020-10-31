from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# from . import login_manager

class Quote:
    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote

class User:
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))


    @property
    def password(self):
        raise AltributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Role:

    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'
    
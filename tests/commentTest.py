import unittest
from app.models import Comment, Blog, User
from app import db

class CommentTest(unittest.TestCase):
    def setUp(self):
        
        self.newComment = Comment(id = 1, comment = 'Test comment', user = self.userDorcas, blog_id = self.newBlog)
        
    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
    
    def checkvariablesTest(self):
        self.assertEquals(self.newComment.comment,'Test comment')
        self.assertEquals(self.newComment.user,self.userDorcas)
        self.assertEquals(self.newComment.blog_id,self.newBlog)


class CommentTest(unittest.TestCase):
    def setUp(self):
        self.userDorcas = User(username='toto', password='1233', email='mosonik@gmail.com')
        self.newBlog = Blog(id=1, title='Encapsulation', content='Testing', user_id=self.userDorcas.id)
        self.newComment = Comment(id=1, comment =' test comment', user_id=self.userDorcas.id, blog_id = self.newBlog.id )

    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
        Comment.query.deleteComment()

    def checkInstanceVariables(self):
        self.assertEquals(self.newComment.comment, 'test comment')
        self.assertEquals(self.newComment.user_id, self.user_charles.id)
        self.assertEquals(self.newComment.blog_id, self.new_blog.id)

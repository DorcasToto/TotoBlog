import unittest
from app.models import Blog,User
from app import db


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.userDorcas= User(username='toto', password='1233', email='mosonik@gmail.com')
        self.new_blog = Blog(id=1, title='Encapusation', content='Testing', user_id=self.userDorcas.id)

    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteBlog()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Encapusation')
        self.assertEquals(self.new_blog.content, 'Testing')
        self.assertEquals(self.new_blog.user_id, self.userDorcas.id)

    def test_save_blog(self):
        self.new_blog.saveBlog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        got_blog = Blog.getallBlogs(1)
        self.assertTrue(getallBlogs is not None)
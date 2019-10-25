import unittest
from app import db
from app.models import User, Post

class DbUserPost(unittest.TestCase):
    '''
        Test Class tests db behaviour
      '''

    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.test_user = User(username="john", email="john@john.com", password='test' )
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        self.user = User.query.filter_by(username= "john").first()
        db.session.remove(self.user)
        db.session.commit()

    def test_save_user_to_db(self):
        user = User.query.filter_by(username='john').first()
        self.assertEqual('john',user.username)



if __name__ == "__main__":
    unittest.main()
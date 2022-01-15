import unittest
from flask_app import app
class TestUserApi(unittest.TestCase):

    def test_user(self):
        tester = app.test_client(self)
        response = tester.get("/user/user/")

        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_common_user(self):
        tester = app.test_client(self)
        response = tester.get("/user/usercommon/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_common(self):
        tester = app.test_client(self)
        response = tester.get("/common/Common/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_user_type(self):
        tester = app.test_client(self)
        response = tester.get("/user/user/")

        reponse_type = response.content_type
        self.assertEqual(reponse_type, 'application/json')

if __name__ == '__main__':
    unittest.main()

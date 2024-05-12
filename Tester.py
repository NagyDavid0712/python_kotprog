from run import app
import unittest


class Tester(unittest.TestCase):

    def test_index_response(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_about_response(self):
        tester = app.test_client(self)
        response = tester.get("/about")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_parts_response(self):
        tester = app.test_client(self)
        response = tester.get("/parts")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_profile_without_login(self):
        tester = app.test_client(self)
        response = tester.get("/profile")
        res_link = response.location
        self.assertEqual(res_link, "/login")

    def test_login_with_cred(self):
        tc = app.test_client()
        response = tc.post("/auth_user", data=dict({
            "login__name": "Tesztteszt",
            "login__password": "Tesztteszt"
        }), follow_redirects=200)
        
        self.assertEqual(response.status_code, 200)

        with tc as c:
            with c.session_transaction() as s:
                self.assertEqual(s["user"]["felh_n"], "Tesztteszt")

    

if __name__ == "__main__":
    unittest.main()

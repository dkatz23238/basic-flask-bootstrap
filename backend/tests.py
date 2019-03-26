import json
import datetime
import uuid
import requests
import unittest


class TestBackend(unittest.TestCase):
    def test_backend(self):
        user = {
            "username": "test1",
            "password": "test1"
        }

        print("USERS POST")
        r = requests.post("http://localhost:3030/api/users", json=json.dumps(user))
        print(r.content)
        print("USERS GET")
        print(requests.get("http://localhost:3030/api/users?username=%s" %
                        user["username"]).content)

        rpa = {
            "rpa_name": "rpa",
            "git_repository": "githib.com",
            "cron_fmat_schedule": "0 0 * * 0",
        }

        print("RPA POST")
        r = requests.post(
            "http://localhost:3030/api/roboticprocessautomations", json=json.dumps(rpa))
        print(r.content)
        print("RPA GET")
        print(requests.get("http://localhost:3030/api/roboticprocessautomations?rpa_id=%s" %
                        json.loads(r.content)["rpa_id"]).content)

        event = {
            "rpa_id": json.loads(r.content)["rpa_id"],
            "tag": "execution",
            "message": "STARTED"
        }
        r = requests.post(r"http://localhost:3030/api/events",
                        json=json.dumps(event))
        print("EVENT POST")
        print(r.content)


        print("EVENTS GET")
        print(requests.get("http://localhost:3030/api/events?rpa_id=%s" %
                        json.loads(r.content)["rpa_id"]).content)


if __name__ == '__main__':
    unittest.main()

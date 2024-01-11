import requests


def authorize(token):
    body = requests.get(
            "http://localhost:8089/authorize",
            headers={
                "Authorization": f"Bearer {token}"
            }
        ).json()

    return body["isAuthorized"]

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsInVzZXJuYW1lIjoidXNlcm5hbWUiLCJpYXQiOjE3MDQ5OTgxMTAsImV4cCI6MTcwNTAwNTMxMH0.o2lPKW0GCtZFY7Q6_6Nsdg9LV5rioQm2Yq7os5Z0cWM
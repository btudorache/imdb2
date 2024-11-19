import requests


def authorize(token):
    body = requests.get(
            "http://localhost:8089/authorize",
            headers={
                "Authorization": f"Bearer {token}"
            }
        ).json()

    return body["isAuthorized"]

import collections

from flask import Response, request
from http import HTTPStatus

from __main__ import app

POST = "POST"
DELETE = "DELETE"

SCORE_POST_REQ_KEYS = [
    "id_user",
    "id_movie",
    "score"
]

SCORE_DEL_REQ_KEYS = [
    "id_score"
]

COMMENT_POST_REQ_KEYS = [
    "id_user",
    "id_movie",
    "comment"
]

COMMENT_DEL_REQ_KEYS = [
    "id_comment"
]


@app.route("/movies/review/score", methods=[POST, DELETE])
def movie_score():
    body = request.get_json()

    if request.method == POST:
        if collections.Counter(body.keys()) != collections.Counter(SCORE_POST_REQ_KEYS):
            return Response(status=HTTPStatus.BAD_REQUEST)

        return f"SCORE POST with: {body}"
    elif request.method == DELETE:
        if collections.Counter(body.keys()) != collections.Counter(SCORE_DEL_REQ_KEYS):
            return Response(status=HTTPStatus.BAD_REQUEST)

        return f"SCORE DEL with: {body}"
    else:
        return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)


@app.route("/movies/review/comment", methods=[POST, DELETE])
def movie_comment():
    body = request.get_json()

    if request.method == POST:
        if collections.Counter(body.keys()) != collections.Counter(COMMENT_POST_REQ_KEYS):
            return Response(status=HTTPStatus.BAD_REQUEST)

        return f"COMMENT POST with: {body}"
    elif request.method == DELETE:
        if collections.Counter(body.keys()) != collections.Counter(COMMENT_DEL_REQ_KEYS):
            return Response(status=HTTPStatus.BAD_REQUEST)

        return f"COMMENT DEL with: {body}"
    else:
        return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)

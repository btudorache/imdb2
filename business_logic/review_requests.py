import json

from flask import Response, request
from http import HTTPStatus

from database import cursor, db
from authorize_utils import authorize

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


def verify_token():
    token = request.headers.get("Authorization").split()[1]

    return authorize(token)


@app.route("/movies/review/score", methods=[POST, DELETE])
def movie_score():
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

    body = request.get_json()

    if request.method == POST:
        try:
            id_user = body["id_user"]
            id_movie = body["id_movie"]
            score = body["score"]
        except Exception as _:
            return Response(status=HTTPStatus.BAD_REQUEST)

        query = (f"INSERT INTO SCORES (score, id_movie, id_user) "
                 f"VALUES ({score}, {id_movie}, {id_user})")

        try:
            cursor.execute(query)
        except Exception as e:
            return Response(status=409, response=str(e))

        db.commit()
        return json.dumps({'id': cursor.lastrowid}), 201

    elif request.method == DELETE:
        try:
            id_score = body["id_score"]
        except Exception as _:
            return Response(status=HTTPStatus.BAD_REQUEST)

        query = f"DELETE FROM SCORES WHERE id = {id_score}"

        try:
            cursor.execute(query)
        except Exception as e:
            return Response(status=404, response=str(e))

        db.commit()
        return Response(status=200)

    else:
        return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)


@app.route("/movies/review/comment", methods=[POST, DELETE])
def movie_comment():
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

    body = request.get_json()

    if request.method == POST:
        try:
            id_user = body["id_user"]
            id_movie = body["id_movie"]
            comment = body["comment"]
        except Exception as _:
            return Response(status=HTTPStatus.BAD_REQUEST)

        query = (f"INSERT INTO COMMENTS (comment, id_user, id_movie) "
                 f"VALUES (%s, %s, %s)")
        values = (comment, id_user, id_movie)

        try:
            cursor.execute(query, values)
        except Exception as e:
            return Response(status=409, response=str(e))

        db.commit()
        return json.dumps({'id': cursor.lastrowid}), 201

    elif request.method == DELETE:
        try:
            id_comment = body["id_comment"]
        except Exception as _:
            return Response(status=HTTPStatus.BAD_REQUEST)

        query = f"DELETE FROM COMMENTS WHERE id = {id_comment}"

        try:
            cursor.execute(query)
        except Exception as e:
            return Response(status=404, response=str(e))

        db.commit()
        return Response(status=200)

    else:
        return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)

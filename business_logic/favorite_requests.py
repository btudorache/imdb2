import json

from flask import Response, request
from http import HTTPStatus

from database import cursor, db
from review_requests import verify_token

from __main__ import app


@app.route('/movies/favorite', methods=["POST"])
def add_movie_to_favorites():
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

    body = request.get_json()

    if "id_user" not in body.keys():
        return Response(status=400)
    if "id_movie" not in body.keys():
        return Response(status=400)

    query = "INSERT INTO FAVORITE (id_user, id_movie) VALUES (%s, %s)"
    values = (body["id_user"], body["id_movie"])
    try:
        cursor.execute(query, values)
    except:
        # duplicated entry
        return Response(status=409)
    db.commit()
    return json.dumps({'id': cursor.lastrowid}), 201


@app.route('/movies/favorite', methods=["DELETE"])
def remove_movie_from_favorites():
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

    body = request.get_json()

    if "id_user" not in body.keys():
        return Response(status=400)
    if "id_movie" not in body.keys():
        return Response(status=400)

    query = "DELETE FROM FAVORITE WHERE id_user = %s AND id_movie = %s"
    values = (body["id_user"], body["id_movie"])
    try:
        cursor.execute(query, values)
    except:
        return Response(status=404)

    db.commit()
    return Response(status=200)
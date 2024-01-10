import collections
import json

from flask import Response, request
from http import HTTPStatus

from database import cursor, db

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
    

# ---------------------------------------------------------------------------------------------------

@app.route('/movies', methods=["POST"])
def add_movie():
    body = request.get_json()

    if "title" not in body.keys():
        return Response(status = 400)
    if "year" not in body.keys():
        return Response(status = 400)
    if "genre" not in body.keys():
        return Response(status = 400)
    if "director" not in body.keys():
        return Response(status = 400)

    title = body["title"]
    year = body["year"]
    genre = body["genre"]
    director = body["director"]

    query = "INSERT INTO MOVIES (title, year, genre, director) VALUES (%s, %s, %s, %s)"
    values = (title, year, genre, director)
    try:
        cursor.execute(query, values)
    except:
        return Response(status=409)
    db.commit()
    return json.dumps({'id': cursor.lastrowid}), 201


@app.route('/movies/<int:movie_id>', methods=["DELETE"])
def delete_movie(movie_id):
    query = "DELETE FROM MOVIES WHERE id = %s"
    values = (movie_id,)
    try:
        cursor.execute(query, values)
    except:
        return Response(status=404)

    db.commit()
    return Response(status=200)


@app.route('/movies', methods=["GET"])
def get_all_movies():
    query = "SELECT * FROM MOVIES"
    cursor.execute(query)

    data = cursor.fetchall()

    movies = []
    for entry in data:
        movies.append({
                'id': entry[0],
                'title': entry[1],
                'year': entry[2],
                'genre': entry[3],
                'director': entry[4]
            })

    return json.dumps(movies), 200


@app.route('/movies/<int:movie_id>', methods=["GET"])
def get_movie_by_id(movie_id):
    query = "SELECT * FROM MOVIES where id = %s"
    values = (movie_id,)
    cursor.execute(query, values)
    data = cursor.fetchone()

    if data is None:
        return Response(status=404)

    movie = {
        'id': data[0],
        'title': data[1],
        'year': data[2],
        'director': data[3],
    }

    return json.dumps(movie), 200


@app.route('/movies/favorite', methods=["POST"])
def add_movie_to_favorites():
    body = request.get_json()

    if "id_user" not in body.keys():
        return Response(status=400)
    if "id_movie" not in body.keys():
        return Response(status=400)

    # todo check if the ids exist

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

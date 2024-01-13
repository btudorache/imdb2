import json

from flask import Response, request
from http import HTTPStatus

from database import cursor, db
from review_requests import verify_token

from __main__ import app


@app.route('/movies', methods=["POST"])
def add_movie():
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

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
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

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
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

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
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

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

import json

from flask import Response, request
from http import HTTPStatus

from database import cursor
from review_requests import verify_token

from __main__ import app

GET = "GET"


@app.route("/movies/filter", methods=[GET])
def filter_movies():
    if not verify_token():
        return Response(status=HTTPStatus.UNAUTHORIZED)

    body = request.get_json()

    title = body.get("title", None)
    year = body.get("year", None)
    genre = body.get("genre", None)
    director = body.get("director", None)

    one_filter = False

    query = "SELECT * FROM MOVIES WHERE "

    if title:
        query += f'title="{title}"'

        one_filter = True
    if year:
        if one_filter:
            query += f" AND "

        query += f"year={year}"

        one_filter = True

    if genre:
        if one_filter:
            query += f" AND "

        query += f'genre="{genre}"'

        one_filter = True
    if director:
        if one_filter:
            query += f" AND "

        query += f'director="{director}"'

        one_filter = True

    if not one_filter:
        return Response(status=HTTPStatus.BAD_REQUEST)

    cursor.execute(query)
    data = cursor.fetchall()

    movie_list = []

    for movie in data:
        movie_list.append(
            {
                'id': movie[0],
                'title': movie[1],
                'year': movie[2],
                'director': movie[3]
            }
        )

    return json.dumps(movie_list), 200

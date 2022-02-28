# instagram_own_version

A simplified version of Instagram with the ability to add posts,
set likes or dislikes, follow other people and view your own page.

## Usage

To use this template, first ensure that you have
[Poetry](https://python-poetry.org/docs/) available.

After that, you should:

1. Install the requirements of the project template by running
    ```
    poetry install
    ```
2. Activate the virtualenv created by _poetry_:
    ```
    poetry shell
    ```

## How to use API
Most of API requests are available only for authorized users. In order to use project's API properly, please create a user account or run ```python3 manage.py createsuperuser``` to specify an admin user with expanded permissions.

Generally project's REST API includes:

1. Signing up (available for unauthorized users).
2. Getting own token (available for authorized users).
3. Getting self profile (available for authorized users).
4. Updating self profile (available for profile's owner).
5. Creating new post (available for authorized users).
6. Getting a post (available for authorized users).
7. Updating a post (available for the author).
8. Deleting a post (available for the author).
9. Adding a comment (available for authorized users).
10. Getting a comment (available for authorized users).
11. Updating a comment (available for the author).
12. Deleting a comment (available for the author).
13. Setting a like or dislike (available for authorized users).
14. Deleting a like or dislike (available for the like's owner)
15. Getting list of posts of a specific user (available for authorized users).
16. Getting own feed (available for authorized users).

To sign up make ```POST``` request to http://127.0.0.1:8000/api/signup/.

To retrieve or update specific profile make <code>GET</code>, <code>PATCH</code> or <code>PUT</code> request
to http://127.0.0.1:8000/api/users/1/.

To create a post make <code>POST</code> request to http://127.0.0.1:8000/api/posts/create/.

To retrieve, update or delete specific post make <code>GET</code>, <code>PATCH</code>, <code>PUT</code> or
<code>DELETE</code> request to http://127.0.0.1:8000/api/posts/1/.

To get a list of posts of a specific user make <code>GET</code> request to http://127.0.0.1:8000/api/posts/
with query parameter <code>user_id</code>.

To get a feed make <code>GET</code> request to http://127.0.0.1:8000/api/posts/
with boolean query parameter <code>feed</code>.

To create comment make <code>POST</code> request to http://127.0.0.1:8000/api/comments/.

To get a list of comments to a specific post make <code>GET</code> request to http://127.0.0.1:8000/api/comments/
with query parameter <code>post_id</code>.

To retrieve, update or delete specific comment make <code>GET</code>, <code>PATCH</code>, <code>PUT</code> or
<code>DELETE</code> request to http://127.0.0.1:8000/api/comments/1/.

To set or delete like make <code>POST</code> or <code>DELETE</code> request to http://127.0.0.1:8000/api/posts/1/like/.

To set or delete dislike make <code>POST</code> or <code>DELETE</code> request
to http://127.0.0.1:8000/api/posts/1/dislike/.

It's impossible to have like and dislike at the same time. If like exists, setting dislike will automatically
remove like.

## Tests
To run tests make in terminal

```
    python3 manage.py test
```

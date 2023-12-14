from bottle import route, post, run, template, redirect, request

import database

@route("/")
def get_index():
    redirect("/users")

@route("/users")
def get_users_list():
    search_term = request.query.get('search', '').strip()
    users = database.get_users_list(search_term)
    return template("list_users.tpl", users_list=users, search_term=search_term)


@route("/posts")
def get_posts_list():
    posts = database.get_posts_with_users()
    return template("list_posts.tpl", posts_list=posts)

@route("/add_user")
def get_add_user():
    return template("add_user.tpl")

@route("/add_post")
def get_add_post():
    return template("add_post.tpl")

@post("/add_user")
def post_add_user():
    username = request.forms.get("username")
    name = request.forms.get("name")
    email = request.forms.get("email")
    database.add_user(username, name, email)
    redirect("/users")

@post("/add_post")
def post_add_post():
    title = request.forms.get("title")
    content = request.forms.get("content")
    user_id = request.forms.get("user_id")
    database.add_post(title, content, user_id)
    redirect("/posts")

@route("/delete_user/<id>")
def get_delete_user(id):
    database.delete_user(id)
    redirect("/users")

@route("/delete_post/<id>")
def get_delete_post(id):
    database.delete_post(id)
    redirect("/posts")

@route("/update_user/<id>")
def get_update_user(id):
    users = database.get_users_list(id)
    if len(users) != 1:
        redirect("/users")
    username = users[0]['username']
    name = users[0]['name']
    email = users[0]['email']
    return template("update_user.tpl", id=id, username=username, name=name, email=email)

@route("/update_post/<id>")
def get_update_post(id):
    posts = database.get_posts_list(id)
    if len(posts) != 1:
        redirect("/posts")
    title = posts[0]['title']
    content = posts[0]['content']
    user_id = posts[0]['user_id']
    return template("update_post.tpl", id=id, title=title, content=content, user_id=user_id)

@post("/update_user")
def post_update_user():
    username = request.forms.get("username")
    name = request.forms.get("name")
    email = request.forms.get("email")
    id = request.forms.get("id")
    database.update_user(id, username, name, email)
    redirect("/users")

@post("/update_post")
def post_update_post():
    title = request.forms.get("title")
    content = request.forms.get("content")
    user_id = request.forms.get("user_id")
    id = request.forms.get("id")
    database.update_post(id, title, content, user_id)
    redirect("/posts")

run(host='localhost', port=8080)
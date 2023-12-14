<!DOCTYPE html>
<html>
<head>
    <title>Post List</title>
</head>
<body>
    <h1>Post List</h1>
    <ul>
        % for post in posts_list:
            <li>{{ post.title }} - {{ post.content }} - {{ post.user.username }} <a href="/update_post/{{ post.id }}">Update</a> <a href="/delete_post/{{ post.id }}">Delete</a></li>
        % end
    </ul>
    <a href="/add_post">Add Post</a>
</body>
</html>

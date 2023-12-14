<!DOCTYPE html>
<html>
<head>
    <title>Update Post</title>
</head>
<body>
    <h1>Update Post</h1>
    <form action="/update_post" method="post">
        <input type="hidden" name="id" value="{{ id }}">
        <label for="title">Title:</label>
        <input type="text" name="title" value="{{ title }}" required><br>
        <label for="content">Content:</label>
        <textarea name="content" required>{{ content }}</textarea><br>
        <label for="user_id">User ID:</label>
        <input type="text" name="user_id" value="{{ user_id }}" required><br>
        <input type="submit" value="Update Post">
    </form>
    <a href="/posts">Back to Post List</a>
</body>
</html>

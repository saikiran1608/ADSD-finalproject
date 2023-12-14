<!DOCTYPE html>
<html>
<head>
    <title>Add Post</title>
</head>
<body>
    <h1>Add Post</h1>
    <form action="/add_post" method="post">
        <label for="title">Title:</label>
        <input type="text" name="title" required><br>
        <label for="content">Content:</label>
        <textarea name="content" required></textarea><br>
        <label for="user_id">User ID:</label>
        <input type="text" name="user_id" required><br>
        <input type="submit" value="Add Post">
    </form>
    <a href="/posts">Back to Post List</a>
</body>
</html>

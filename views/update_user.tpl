<!DOCTYPE html>
<html>
<head>
    <title>Update User</title>
</head>
<body>
    <h1>Update User</h1>
    <form action="/update_user" method="post">
        <input type="hidden" name="id" value="{{ id }}">
        <label for="username">Username:</label>
        <input type="text" name="username" value="{{ username }}" required><br>
        <label for="name">Name:</label>
        <input type="text" name="name" value="{{ name }}" required><br>
        <label for="email">Email:</label>
        <input type="email" name="email" value="{{ email }}" required><br>
        <input type="submit" value="Update User">
    </form>
    <a href="/users">Back to User List</a>
</body>
</html>

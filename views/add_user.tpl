<!DOCTYPE html>
<html>
<head>
    <title>Add User</title>
</head>
<body>
    <h1>Add User</h1>
    <form action="/add_user" method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" required><br>
        <label for="name">Name:</label>
        <input type="text" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" name="email" required><br>
        <input type="submit" value="Add User">
    </form>
    <a href="/users">Back to User List</a>
</body>
</html>

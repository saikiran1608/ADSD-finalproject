<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
</head>
<body>
    <h1>User List</h1>
    <ul>
        % for user in users_list:
            <li>{{ user.username }} - {{ user.name }} - {{ user.email }} <a href="/update_user/{{ user.id }}">Update</a> <a href="/delete_user/{{ user.id }}">Delete</a></li>
        % end
    </ul>
    <a href="/add_user">Add User</a>
</body>
</html>

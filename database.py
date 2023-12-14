from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://saikirangoud1016:Messi10@adsd.a1n28m2.mongodb.net?retryWrites=true&w=majority"

# uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

feed = client.feed

def setup_database():
    feed.drop_collection(feed.users)
    feed.drop_collection(feed.posts)

def get_users_list(id=None):
    users_collection = feed.users
    if id == None:
        users = users_collection.find({})
    else:
        users = users_collection.find({"_id":ObjectId(id)})
    users = list(users)
    for user in users:
        user["id"] = str(user["_id"])
    return users

def get_posts_list(id=None):
    posts_collection = feed.posts
    if id == None:
        posts = posts_collection.find({})
    else:
        posts = posts_collection.find({"_id":ObjectId(id)})
    posts = list(posts)
    for post in posts:
        post["id"] = str(post["_id"])
    return posts

def get_posts_with_users():
    pipeline = [
        {
            "$lookup": {
                "from": "users",
                "localField": "user_id",
                "foreignField": "_id",
                "as": "user"
            }
        },
        {
            "$unwind": "$user"
        },
        {
            "$project": {
                "title": 1,
                "content": 1,
                "user.username": 1,
                "user.name": 1,
                "user.email": 1
            }
        }
    ]

    posts_collection = feed.posts
    result = posts_collection.aggregate(pipeline)
    return list(result)

def add_post(title, content, user_id):
    posts_collection = feed.posts
    post_data = {"title": title, "content": content, "user_id": ObjectId(user_id)}
    result = posts_collection.insert_one(post_data)
    return str(result.inserted_id)

def delete_post(post_id):
    posts_collection = feed.posts
    result = posts_collection.delete_one({"_id": ObjectId(post_id)})
    return result.deleted_count > 0


def update_post(post_id, title=None, content=None):
    posts_collection = feed.posts
    update_data = {}
    
    if title is not None:
        update_data["title"] = title

    if content is not None:
        update_data["content"] = content

    if not update_data:
        # Nothing to update
        return False

    result = posts_collection.update_one({"_id": ObjectId(post_id)}, {"$set": update_data})
    return result.modified_count > 0


def add_user(username, name, email):
    users_collection = feed.users
    user_data = {"username": username, "name": name, "email": email}
    result = users_collection.insert_one(user_data)
    return str(result.inserted_id)


def test_setup_database():
    print("Testing setup_database()")
    setup_database()
    users = get_users_list()
    assert len(users) == 0
    posts = get_posts_list()
    assert len(posts) == 0

def test_add_user_and_post():
    print("Testing add_user_and_post()")
    setup_database()
    user_id = add_user("john_doe", "John Doe", "john@example.com")
    post_id = add_post("First Post", "Content of the first post.", user_id)
    users = get_users_list()
    assert len(users) == 1
    posts = get_posts_list()
    assert len(posts) == 1
    assert posts[0]["user_id"] == user_id

def test_get_posts_with_users():
    print("Testing get_posts_with_users()")
    setup_database()
    user_id = add_user("john_doe", "John Doe", "john@example.com")
    post_id = add_post("First Post", "Content of the first post.", user_id)
    
    posts_with_users = get_posts_with_users()
    
    assert len(posts_with_users) == 1
    assert posts_with_users[0]["title"] == "First Post"
    assert posts_with_users[0]["user"]["username"] == "john_doe"

def test_update_post():
    print("Testing update_post()")
    setup_database()
    user_id = add_user("john_doe", "John Doe", "john@example.com")
    post_id = add_post("First Post", "Content of the first post.", user_id)

    success = update_post(post_id, title="Updated Title", content="Updated Content")
    
    assert success

    updated_post = get_posts_list(post_id)[0]
    assert updated_post["title"] == "Updated Title"
    assert updated_post["content"] == "Updated Content"

def test_delete_post():
    print("Testing delete_post()")
    setup_database()
    user_id = add_user("john_doe", "John Doe", "john@example.com")
    post_id = add_post("First Post", "Content of the first post.", user_id)

    success = delete_post(post_id)
    
    assert success

    posts = get_posts_list()
    assert len(posts) == 0

if __name__ == "__main__":
    test_setup_database()
    test_add_user_and_post()
    test_get_posts_with_users()
    test_update_post()
    test_delete_post()
    print("All tests passed.")



import os

from main import UserManager

BASE = os.path.dirname(os.path.abspath(__file__))
path_to_json = os.path.join(BASE, "users.json")

if __name__ == "__main__":
    if os.path.exists(path_to_json):
        raise RuntimeError(f"{path_to_json} already exists, please check if it is safe to delete, and delete it to run the test.")
    
    um = UserManager()
    um.add_user("张三", 18)    #  {"id": 1, "username": "张三", "age": 18}
    um.add_user("李四", 20)    #  {"id": 2, "username": "李四", "age": 20}
    u1 = um.get_user(1)
    u2 = um.get_user(2)
    assert u1 == {"id": 1, "username": "张三", "age": 18}, u1
    assert u2 == {"id": 2, "username": "李四", "age": 20}, u2
    assert um.get_user(3) is None
    print("add_user and get_user passed")

    assert um.update_age(1, 19) is True
    assert um.update_age(3, 21) is False
    assert um.get_user(1)["age"] == 19, um.get_user(1)
    print("update_age passed")

    assert um.remove_user(2) is True
    assert um.remove_user(2) is False
    print("remove_user passed")

    assert um.list_users() == [{"id": 1, "username": "张三", "age": 19}], um.list_users()
    print("list_users passed")

    um.save_to_json(path_to_json)
    um2 = UserManager()
    um2.load_from_json(path_to_json)
    assert um2.list_users() == [{"id": 1, "username": "张三", "age": 19}], um2.list_users()
    print("save_to_json and load_from_json passed")

    if os.path.exists(path_to_json):
        os.remove(path_to_json)
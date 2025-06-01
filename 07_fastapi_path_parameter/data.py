from typing import Optional


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


# ダミーデータベースとしてリストを用意
user_list = [User(id=1, name="内藤"), User(id=2, name="後藤"), User(id=3, name="中藤")]


# user_idを引数で受けとりリストから検索する
# return UserオブジェクトまたはNone
def get_user(user_id: int) -> Optional[User]:
    for user in user_list:
        if user.id == user_id:
            return user
    return None  # Userが見つからない場合はNoneを返す

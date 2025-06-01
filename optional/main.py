# optional型：変数が指定した型をもつか，Noneをもつかどちらを指す
from typing import Optional


# emailは必須パラメータ，他2つはオプショナル（任意）で，デフォルト値にNoneが設定されている
def get_profile(
    email: str, username: Optional[str] = None, age: Optional[int] = None
) -> dict:
    profile = {"email": email}
    if username:  # 引数にusernameが存在すればディクショナリに追加
        profile["username"] = username
    if age:
        profile["age"] = age
    return profile


print(get_profile("abc@gmail.com", "Meoe", 15))
print(get_profile("zzz@gmail.com", "Niko"))
print(get_profile("yyy@gmail.com"))


# 第2,3引数の"=None"を削除するとエラーになる。
# Optionalは「NoneもOK」という型ヒント 引数を任意にするものではないことに留意
# 「引数を任意にする」にはデフォルト値（= Noneなど）が必要

print(get_profile("ooo@gmail.com", None, None))

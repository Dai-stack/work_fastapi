from typing import Optional
from fastapi import FastAPI, HTTPException

# data.pyから関数とクラスをインポート
from data import get_user, User

# user_idをパスパラメータとして受取り，ユーザ情報を返すエンドポイント


@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    user: Optional[User] = get_user(user_id)
    # Userが見つからない場合は404エラーを返す。
    if user
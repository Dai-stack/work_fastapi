from typing import Optional
from fastapi import FastAPI, HTTPException

# data.pyから関数とクラスをインポート
from data import get_user, User

app = FastAPI()


# user_idをパスパラメータとして受取り，ユーザ情報を返すエンドポイント
@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    user: Optional[User] = get_user(user_id)
    # Userが見つからない場合は404エラーを返す。
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return {"user_id": user_id, "username": user.name}


# uvicorn main:app --reload
# http://127.0.0.1:8000/docs
# 引数に型ヒントを用いていることにより，バリデーションが実装される

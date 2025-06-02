from typing import Optional
from fastapi import FastAPI, HTTPException

# data.pyから関数とクラスをインポート
from data import get_books_by_category

app = FastAPI()


# クエリパラメータ（URLの？以降を指す）で指定されたカテゴリに基づいて書籍情報を検索し，
# 結果をJSONで返す。
# クエリパラメータは引数で受け取る
@app.get("/users/{books}")
async def read_books(category: Optional[str] = None) -> list[dict[str, str]]:
    result = get_books_by_category(category)
    # 辞書のリストを返す
    return [
        {"id": book.id, "title": book.title, "category": book.category}
        for book in result
    ]


# http://127.0.0.1:8000/docs
# 引数に型ヒントを用いていることにより，バリデーションが実装される

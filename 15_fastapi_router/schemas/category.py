from pydantic import BaseModel


# カテゴリのスキーマ
# 復習：Basemodelを継承することで自動でバリデーションがかかる
class Category(BaseModel):
    category_id: int
    category_name: str

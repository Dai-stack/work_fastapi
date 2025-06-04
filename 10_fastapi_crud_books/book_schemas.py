# スキーマ：データ構造を定義した設計図
from pydantic import BaseModel


# 書籍の作成と更新に使用するスキーマ
class BookSchema(BaseModel):
    titel: str
    category: str


# レスポンス用のスキーマ
# 書籍スキーマを継承してidも含める
class BookResponseSchema(BookSchema):
    id: int

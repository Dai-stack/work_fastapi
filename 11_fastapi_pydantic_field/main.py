from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# スキーマ
# PydanticのField関数：（フロント→API送信データの）バリデーション, デフォルト値の設定,メタデータ，説明文の追加
# Fieldの引数...はEllipsis（エリプシス）といい，フィールド入力が必須であることを示す。
class BookSchema(BaseModel):
    title: str = Field(
        ..., description="タイトルの指定：必須", example="コイノボリの如く"
    )
    category: str = Field(..., description="カテゴリの指定：必須", example="comics")
    publish_year: int = Field(
        default=None, description="出版年の指定：任意", example=2023
    )
    price: float = Field(
        ...,
        gt=0,
        le=5000,
        description="販売価格の指定：0 < 価格 <= 10000",
        example=2500,
    )


# エンドポイント
@app.post("/books/", response_model=BookSchema)
async def create_book(book: BookSchema):
    return book

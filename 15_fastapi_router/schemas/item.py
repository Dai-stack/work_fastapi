from pydantic import BaseModel


# 商品のスキーマ
class Item(BaseModel):
    item_id: int
    item_name: str
    category_id: int

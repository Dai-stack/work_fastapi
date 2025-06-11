from fastapi import APIRouter
from schemas.category import Category


# app = FastAPI()
router = APIRouter()  # APIRouterインスタンスを作成する


# =====【カテゴリ】 のエンドポイント=====
# カテゴリ一覧を取得
@router.get("/categories/", response_model=dict)
async def read_categories():
    # 実際にはデータベースから取得する
    return {"message": "カテゴリ一覧を表示", "categories": []}


# 新しいカテゴリを作成
@router.post("/categories/", response_model=dict)
async def create_category(category: Category):
    # 実際にはデータベースに保存する
    return {"message": "カテゴリを作成しました", "category": category}


# カテゴリを更新
@router.put("/categories/{category_id}", response_model=dict)
async def update_category(category_id: int, category: Category):
    # 実際にはデータベースを更新する
    return {
        "message": "カテゴリを更新しました",
        "category_id": category_id,
        "category": category,
    }


# カテゴリを削除
@router.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    # 実際にはデータベースから削除する処理が入ります
    return {"message": "カテゴリを削除しました", "category_id": category_id}

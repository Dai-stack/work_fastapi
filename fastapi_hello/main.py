from fastapi import FastAPI


# FastAPIのインスタンスを作成
app = FastAPI()


# GETメソッドかつエンドポイント"/"で呼ばれる関数
# @app FastAPIのインスタンスを表す
# デコレータ 関数に機能を飾りつけすることから（追加する）
@app.get("/")
async def get_hello():
    return {"message": "Hello World"}


# #起動コマンド
# ・uvicorn main:app --reload
# #Swagger UI
# #API動作テストのためのインターフェース
# ・http://127.0.0.1:8000/docs

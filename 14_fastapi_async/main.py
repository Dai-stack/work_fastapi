# httpxライブラリ→非同期通信に対応しているライブラリ
# 住所情報を非同期に取得するライブラリ
from fastapi import FastAPI
import asyncio
import httpx

app = FastAPI()


async def fetch_address(zip_code: str):
    # async with でHTTPクライアントを非同期に開始し，awaitでリクエストのレスポンスを待つ。
    async with httpx.AsyncClient() as client:
        # AsyncClient().get()は非同期関数なので，awaitをつけてレスポンスが返るまで待つ
        response = await client.get(
            f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zip_code}"
        )
        return response.json()


@app.get("/addresses/")
async def get_addresses():
    zip_codes = ["0600000", "1000001", "9000000"]
    # * アンパック演算子，リストを回すときに個々の要素を引数として関数に渡す
    # ★ここではzip_codesの各要素に対して，fetch_address関数を非同期実行し，JSON戻り値を集めてリストにしている
    # * リストやタプルなどの位置引数のアンパックに使う
    # ** 辞書などのキーワード引数のアンパックに使う。
    return await asyncio.gather(*(fetch_address(zip_code) for zip_code in zip_codes))


# uvicorn main:app --reload
# 127.0.0.1:8000/addresses/

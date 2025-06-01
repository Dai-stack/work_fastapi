import requests
import json


# リンク先は郵便番号API
url = "https://zipcloud.ibsnet.co.jp/api/search"

zip = input("Enter a Zipcode >>")  # 5400012

# パラメータを用意
param = {"zipcode": zip}

# APIにHTTP GETリクエストを送りレスポンスを得る。第二引数はパラメータ
res = requests.get(url, param)

# レスポンスデータに格納されているJSON形式のレスポンスデータを，ディクショナリに格納
data = json.loads(res.text)

print(data)

# 区切り
print("*" * 50)

if data["results"] is not None:  # （翻訳）JSONデータの"results"キーの中身が存在すれば

    address_info = data["results"][0]

    print(
        f"あなたの住所情報 -> {address_info["address1"]} {address_info["address2"]} {address_info["address3"]}"
    )

else:
    print("住所情報が見つかりませんでした")

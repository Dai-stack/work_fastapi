from datetime import datetime
from pydantic import BaseModel, ValidationError


# イベントを表すクラス
# BaseModelを継承する→pydantic 自動でコンストラクタが提供される
class Event(BaseModel):
    name: str = "未定"
    start_datetime: datetime
    participants: list[str] = []


# 値を変えてみるとバリデーションがかかる
external_data = {
    "name": "FastAPI勉強会",
    "start_datetime": "2025-01-05 09:00",
    "participants": ["山田", "鈴木", "田中"],
}

# ディクショナリのアンパック代入（引数に**がついてる）
# ディクショナリに含まれるキーバリューのペアを関数の引数として展開するPythonの機能
# 各キーが関数の引数名として，対応する値がその引数の値として自動的に渡される。

try:
    event = Event(**external_data)
    print(event.name, type(event.name))
    print(event.start_datetime, type(event.start_datetime))
    print(event.participants, type(event.participants))
except ValidationError as e:
    print("データのバリデーションエラーが発生しました：", e.errors())

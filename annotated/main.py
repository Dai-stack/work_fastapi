# 型ヒントに追加情報を付け加える
# 実際の動作には影響しない（FastAPIの機能と絡めると嬉しいことがあるらしい）
from typing import Annotated


def process_value(value: Annotated[int, "範囲：0 <= value <= 100"]) -> None:
    if 0 <= value <= 100:
        print(f"受け取った値は範囲内です:{value}")
    else:
        raise ValueError(f"範囲外の値です。値:{value}")


process_value(60)


try:
    process_value(150)
except ValueError as e:
    print(e)

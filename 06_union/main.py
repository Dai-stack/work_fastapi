# パイプ演算子：2つの型のいずれかであることを示す
# str | Noneとすれば Optional[str]と同じ意味になる
def parse_input(value: int | str) -> str:
    if isinstance(value, int):
        return f"値は整数型です : {value}"
    elif isinstance(value, str):
        return f"値は文字列です : {value}"
    else:
        raise ValueError("引数が整数型・文字列型ではありません。")


print(parse_input("猫好きに悪いひとはいないかもしれない"))
print(parse_input(123))
print(parse_input(123.0))  # 例外発生

# def add(num1, num2):
#     result = "足し算結果 ＝>"
#     return result + str(num1 + num2)


def add(num1: int, num2: int) -> str:
    result: str = "足し算結果 ＝> "
    return result + str(num1 + num2)


print(add(4, 5))


def greet(name: str) -> str:
    return f"おはよう {name}!"


print(greet("猫ちゃん"))


def divide(dividend: float, divisor: float) -> float:
    return dividend / divisor


print(divide(39.0, 5.0))


def process_items(items: list[str]) -> None:
    for item in items:
        print(item)


process_items(["猫", "コアラ", "きつね"])


# para:リスト[str]
# return:ディクショナリ[str, int]


def count_characters(word_list: list[str]) -> dict[str, int]:

    # キー：ワード 値：文字数
    count_map: dict[str, int] = {}

    for word in word_list:
        count_map[word] = len(word)  # 要素の追加

    return count_map


character_counts = count_characters(["amazon", "facebook", "google"])
print(character_counts)

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

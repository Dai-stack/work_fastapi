from typing import Optional


class Books:
    def __init__(self, id: str, title: str, category: str):
        self.id = id
        self.title = title
        self.category = category


books = [
    Books(id="1", title="愛するということ", category="心理学"),
    Books(id="2", title="読書について", category="哲学"),
    Books(id="3", title="Python入門", category="プログラミング"),
    Books(id="4", title="データサイエンスの基礎", category="プログラミング"),
    Books(id="5", title="幸福の条件", category="心理学"),
    Books(id="6", title="源氏物語", category="文学"),
    Books(id="7", title="コンピュータサイエンス入門", category="プログラミング"),
    Books(id="8", title="日本の歴史", category="歴史"),
    Books(id="9", title="現代アートの理解", category="芸術"),
    Books(id="10", title="経済学の基礎", category="経済学"),
]


def get_books_by_category(category: Optional[str] = None) -> list[Book]:
    if category is None:
        return books  # カテゴリ指定しない場合は全書籍を返す
    else:  # 指定カテゴリに一致する書籍だけを返す
        return [book for book in books if book.category == category]
    # P.80
    # リスト内包表記（list comprehension）はリストの中でループと条件を一行で書いて新しいリストを作るPythonの短縮記法

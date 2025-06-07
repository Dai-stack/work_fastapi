from fastapi import FastAPI, HTTPException
from book_schemas import BookSchema, BookResponseSchema

app = FastAPI()

# ダミー書籍データ（リスト）
books: list[BookResponseSchema] = [
    BookResponseSchema(id=1, titel="Python入門", category="プログラミング"),
    BookResponseSchema(id=2, titel="FastAPIガイド", category="Web開発"),
    BookResponseSchema(id=3, titel="英文解釈の技法", category="英語学習"),
    BookResponseSchema(id=4, titel="データサイエンス入門", category="データ分析"),
    BookResponseSchema(id=5, titel="機械学習の基礎", category="AI・機械学習"),
    BookResponseSchema(
        id=6, titel="アルゴリズムとデータ構造", category="コンピュータサイエンス"
    ),
    BookResponseSchema(id=7, titel="Web開発の基礎", category="Web開発"),
    BookResponseSchema(id=8, titel="データベース入門", category="データベース"),
    BookResponseSchema(id=9, titel="ネットワークの基礎", category="ネットワーク"),
    BookResponseSchema(id=10, titel="セキュリティの基礎", category="セキュリティ"),
]


# 書籍を追加するためのエンドポイント
# 引数：BookSchema
# 戻り値：BookResponseSchema
# デコレータの第二引数はエンドポイントが返すレスポンスデータ（＝戻り値）の型を示す。
@app.post("/books/", response_model=BookResponseSchema)
def create_book(book: BookSchema):
    # リスト要素の最大IDを見つけて1をたす
    new_book_id = max([book.id for book in books], default=0) + 1
    # Pydanticモデルのインスタンスから辞書形式のデータを生成し，
    # 辞書のアンパックを実施してBookResponseSchemaインスタンスを作成している。
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    # リストに追加
    books.append(new_book)
    # 登録書籍データを返却
    return new_book


# 書籍情報を全件取得するエンドポイント
# 引数：なし
# 戻り値：BookResponseSchemaのリスト
@app.get("/books/", response_model=list[BookResponseSchema])
def read_books():
    return books


# IDをパスパラメータで受取り，1件書籍を取得するエンドポイント
@app.get("/books/{book_id}", response_model=BookResponseSchema)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# IDに対応する書籍情報を更新するエンドポイント
@app.put("/books/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book: BookSchema):
    # パラメータで引き受けたIDの書籍を更新
    # enumerate リストのループ時にインデックスと要素の両方を取得できる
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            updated_book = BookResponseSchema(id=book_id, **book.model_dump())
            books[index] = updated_book
            return updated_book
    # 該当IDの書籍がない場合は例外を投げる。
    raise HTTPException(status_code=404, detail="Book NOT Found")


# パスパラメータで受けたIDに対応する書籍情報を削除するためのエンドポイント
@app.delete("/books/{book_id}", response_model=BookResponseSchema)
def delete_book(book_id: int):
    # 特定のIDの書籍を削除
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return book
    # ない場合は例外をなげる
    raise HTTPException(status_code=404, detail="Book Not Foun")

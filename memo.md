#パラメータなど

<!-- 仮想環境に入る -->
conda activate fastapi_env 


#ASGI
・非同期Webサーバーゲートウェイインターフェース

#起動コマンド
・uvicorn main:app --reload 
・http://127.0.0.1:8000/docs

#Swagger UI
・FastAPIのルーティングは、Web アプリケーションにおけるURL のパスに対応する
  特定の関数を割り当てる仕組みのこと

##REST4原則 Representational State Transfer 代表的な状態転送 
#stateless
・クライアントの情報を保持しない
#Uniform Interface
・統一的なインターフェース
#Addressability
・アドレス指定可能性

#HTTPメソッド
・安全性と冪等性（べきとう）の観点で考える
・安全性：リソースの状態を変えない 
・冪等性：何度実行しても結果が同じ
・GETメソッドは両方満たす，POSTメソッドは両方とも満たさない。

#AnnotetdとField型
・Annotetedは便利な機能だがPydanticのFieldで代替できる。

#非同期通信
・FastAPIのasyncとPythonのasyncは同じもの（FastAPIはPythonの非同期通信を利用している）

#ORM Object Relational Mapper
・アプリのオブジェクトとリレーショナルデータベースのデータをマッピングする
・予め対応情報を保存しておくと，自動で，インスタンスのデータを対応するテーブルに書き出しだり，データベースから
  値を読み込んでインスタンスに値を代入したりできる。

#SQLAlchemy
・Pythonのオブジェクト操作でデータベースを扱える
・セッション，DB接続，トランザクション管理を自動化。非同期処理にも対応

#SQLite
・データをファイルとして保存する軽量なデータベース。学習には最適。
・Pythonではsqlite3（標準ライブラリ）で利用できる。
・aiosalite：SQLiteデータベースを非同期IO（入出力操作を待つ間，他のタスクを同時に進めることができる技術）で利用するためのライブラリ
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Select

# ベースクラスの定義
Base = declarative_base()

# DBファイル作成
base_dir = os.path.dirname(__file__)  # 実行ファイルmain.pyの場所を取得

# データベースのURL
DATABASE_URL = "sqlite+aiosqlite:///" + os.path.join(base_dir, "example.sqlite")

# 非同期エンジンの作成
engine = create_async_engine(DATABASE_URL, echo=True)

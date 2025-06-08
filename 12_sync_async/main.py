# 同期処理
import time


def sync_task(name):
    print(f"{name} タスク開始")
    time.sleep(2)  # 2秒待機
    print(f"{name} タスク終了")


def run_sync_tanks():
    sync_task("タスク1")
    sync_task("タスク2")
    sync_task("タスク3")


print("同期処理")

run_sync_tanks()

# 非同期処理
# asyncをつけることで非同期関数の宣言になる。
# asyncio イベントループと呼ばれる仕組みを利用している
import asyncio


async def async_task(name):
    print(f"{name} タスク開始")
    await asyncio.sleep(2)  # 非同期的な待機（他のタスクが実行可能）
    print(f"{name} タスク終了")


async def run_async_tasks():
    await asyncio.gather(
        async_task("タスクA"), async_task("タスクB"), async_task("タスクC")
    )


print("\n\n非同期処理の例：")
asyncio.run(run_async_tasks())

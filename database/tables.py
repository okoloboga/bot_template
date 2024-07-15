from sqlalchemy import Table, MetaData, Column, BigInteger, String, Integer

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("telegram_id", BigInteger, primary_key=True),  # 0
    Column("first_name", String),  # 1
    Column("last_name", String),  # 2
    Column("status", String)  # 3
)

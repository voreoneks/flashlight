from sqlalchemy import Column, Float, String, Table

from app.db.tables import metadata

state_table = Table(
    "state",
    metadata,
    Column("state", String, nullable=False),
    Column("color", Float, nullable=False),
)

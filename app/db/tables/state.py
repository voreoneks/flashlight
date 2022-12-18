from sqlalchemy import Table, String, Float, Column
from app.db.tables import metadata

state_table = Table(
    'state',
    metadata,
    Column('state', String, nullable=False),
    Column('color', Float, nullable=False)
)
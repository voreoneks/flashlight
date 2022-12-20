"""create_table

Revision ID: 549fb37e38fd
Revises: 
Create Date: 2022-12-18 23:26:20.315185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "549fb37e38fd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "state_table",
        sa.Column("state", sa.String, nullable=False),
        sa.Column("color", sa.Float, nullable=False),
    )


def downgrade() -> None:
    pass

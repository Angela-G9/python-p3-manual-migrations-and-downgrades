"""Renaming name to full_name in Student model

Revision ID: 42383fb74789
Revises: 791279dd0760
Create Date: 2025-03-09 12:31:13.512979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42383fb74789'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')

"""add tour and user

Revision ID: 9234059a8018
Revises: a8d16b778232
Create Date: 2024-02-18 14:06:18.774456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9234059a8018'
down_revision: Union[str, None] = 'a8d16b778232'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tour', sa.Column('user_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tour', 'user_name')
    # ### end Alembic commands ###

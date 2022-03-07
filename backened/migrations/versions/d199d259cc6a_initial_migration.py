"""Initial migration.

Revision ID: d199d259cc6a
Revises: 
Create Date: 2022-03-06 23:49:00.437026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd199d259cc6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mosmetro_news',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(length=125), nullable=True),
    sa.Column('img_url', sa.String(length=255), nullable=True),
    sa.Column('posted_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title', 'img_url', 'posted_at', name='_unique_news')
    )
    op.create_index(op.f('ix_mosmetro_news_id'), 'mosmetro_news', ['id'], unique=False)
    op.create_index(op.f('ix_mosmetro_news_posted_at'), 'mosmetro_news', ['posted_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mosmetro_news_posted_at'), table_name='mosmetro_news')
    op.drop_index(op.f('ix_mosmetro_news_id'), table_name='mosmetro_news')
    op.drop_table('mosmetro_news')
    # ### end Alembic commands ###
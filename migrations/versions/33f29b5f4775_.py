"""empty message

Revision ID: 33f29b5f4775
Revises: 08c81aae25f3
Create Date: 2022-02-08 00:15:37.138626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33f29b5f4775'
down_revision = '08c81aae25f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_answer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=True),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_answer_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

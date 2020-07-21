"""Added work experience skills

Revision ID: 3ebedd1c0c83
Revises: e3eabcfcc0a4
Create Date: 2020-07-20 21:43:15.833657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ebedd1c0c83'
down_revision = 'e3eabcfcc0a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('work_experience_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('work_experience_id', sa.Integer(), nullable=True),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.id'], ),
    sa.ForeignKeyConstraint(['work_experience_id'], ['work_experience.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work_experience_skills')
    # ### end Alembic commands ###

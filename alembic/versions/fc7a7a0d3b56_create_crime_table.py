"""create crime table

Revision ID: fc7a7a0d3b56
Revises: 
Create Date: 2023-05-23 10:56:44.596329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc7a7a0d3b56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('crimes',
                    sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
                    sa.Column('dr_no', sa.Integer(), nullable=False),
                    sa.Column('date_rptd', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('date_occ', sa.TIMESTAMP(timezone=True), nullable=False), 
                    sa.Column('time_occ', sa.Integer(),  nullable=False),
                    sa.Column('area', sa.Integer(),  nullable=False),
                    sa.Column('area_name', sa.String(),  nullable=False),
                    sa.Column('rpt_dist_no', sa.Integer(),  nullable=False),
                    sa.Column('part_1_2', sa.Integer(),  nullable=False),
                    sa.Column('crm_cd', sa.Integer(),  nullable=False),
                    sa.Column('crm_cd_desc', sa.String(),  nullable=False),
                    sa.Column('mocodes', sa.String(),  nullable=True),
                    sa.Column('vict_age', sa.Integer(),  nullable=False), 
                    sa.Column('vict_sex', sa.String(),  nullable=True), 
                    sa.Column('vict_descent', sa.String(),  nullable=True),
                    sa.Column('premis_cd', sa.Float(),  nullable=True),
                    sa.Column('premis_desc', sa.String(),  nullable=True),
                    sa.Column('weapon_used_cd', sa.Float(),  nullable=True),
                    sa.Column('weapon_desc', sa.String(),  nullable=True),
                    sa.Column('status', sa.String(),  nullable=False),
                    sa.Column('status_desc', sa.String(),  nullable=False),
                    sa.Column('crm_cd_1', sa.Float(),  nullable=True),
                    sa.Column('crm_cd_2', sa.Float(),  nullable=True),
                    sa.Column('crm_cd_3', sa.Float(),  nullable=True),
                    sa.Column('crm_cd_4', sa.Float(),  nullable=True),
                    sa.Column('location', sa.String(),  nullable=False),
                    sa.Column('cross_street', sa.String(),  nullable=True),
                    sa.Column('lat', sa.Float(),  nullable=False),
                    sa.Column('lon', sa.Float(),  nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.text('CURRENT_TIMESTAMP')),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('crimes')

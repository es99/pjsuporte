"""empty message

Revision ID: 19719ab5254d
Revises: 7c809aecec59
Create Date: 2023-06-22 22:57:30.593017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19719ab5254d'
down_revision = '7c809aecec59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solicitacao_cadastros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=120), nullable=False),
    sa.Column('cpf', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('tel', sa.String(length=64), nullable=False),
    sa.Column('rg', sa.String(length=64), nullable=False),
    sa.Column('entidade', sa.String(length=120), nullable=False),
    sa.Column('sistema', sa.String(length=64), nullable=False),
    sa.Column('nome_solicitante', sa.String(length=120), nullable=False),
    sa.Column('cpf_solicitante', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_solicitacao_cadastros_cpf'), 'solicitacao_cadastros', ['cpf'], unique=False)
    op.create_index(op.f('ix_solicitacao_cadastros_cpf_solicitante'), 'solicitacao_cadastros', ['cpf_solicitante'], unique=False)
    op.create_index(op.f('ix_solicitacao_cadastros_email'), 'solicitacao_cadastros', ['email'], unique=False)
    op.create_index(op.f('ix_solicitacao_cadastros_nome'), 'solicitacao_cadastros', ['nome'], unique=False)
    op.create_index(op.f('ix_solicitacao_cadastros_nome_solicitante'), 'solicitacao_cadastros', ['nome_solicitante'], unique=False)
    op.create_index(op.f('ix_solicitacao_cadastros_rg'), 'solicitacao_cadastros', ['rg'], unique=False)
    op.create_index(op.f('ix_solicitacao_cadastros_sistema'), 'solicitacao_cadastros', ['sistema'], unique=False)
    op.create_index(op.f('ix_solicitacao_cadastros_tel'), 'solicitacao_cadastros', ['tel'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_solicitacao_cadastros_tel'), table_name='solicitacao_cadastros')
    op.drop_index(op.f('ix_solicitacao_cadastros_sistema'), table_name='solicitacao_cadastros')
    op.drop_index(op.f('ix_solicitacao_cadastros_rg'), table_name='solicitacao_cadastros')
    op.drop_index(op.f('ix_solicitacao_cadastros_nome_solicitante'), table_name='solicitacao_cadastros')
    op.drop_index(op.f('ix_solicitacao_cadastros_nome'), table_name='solicitacao_cadastros')
    op.drop_index(op.f('ix_solicitacao_cadastros_email'), table_name='solicitacao_cadastros')
    op.drop_index(op.f('ix_solicitacao_cadastros_cpf_solicitante'), table_name='solicitacao_cadastros')
    op.drop_index(op.f('ix_solicitacao_cadastros_cpf'), table_name='solicitacao_cadastros')
    op.drop_table('solicitacao_cadastros')
    # ### end Alembic commands ###
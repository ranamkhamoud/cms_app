"""create tables

Revision ID: 8bacef5e7e98
Revises: 
Create Date: 2023-06-21 15:40:12.785898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bacef5e7e98'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Mall
    op.create_table(
        'malls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('location', sa.String(50), nullable=False),
        sa.Column('contact', sa.String(50), nullable=False),
    )

    # Department
    op.create_table(
        'departments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('mall_id', sa.Integer, sa.ForeignKey('malls.id')),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('contact', sa.String(50), nullable=False),
    )

    # Employee
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('contact', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('department_id', sa.Integer, sa.ForeignKey('departments.id')),
    )

    # Customer
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('contact', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
    )

    # Complaint
    op.create_table(
        'complaints',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('department_id', sa.Integer, sa.ForeignKey('departments.id')),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.id')),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.id')),
        sa.Column('category', sa.String(50), nullable=False),
        sa.Column('details', sa.String(200), nullable=False),
        sa.Column('date', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('priority', sa.String(50), nullable=False),
    )

    # Resolution
    op.create_table(
        'resolutions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('complaint_id', sa.Integer, sa.ForeignKey('complaints.id')),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.id')),
        sa.Column('details', sa.String(200), nullable=False),
        sa.Column('date', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    pass

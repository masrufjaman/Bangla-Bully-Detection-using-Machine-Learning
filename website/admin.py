from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route('/')
def admin_dashboard():
    return "<h1>Admin Dashboard</h1>"
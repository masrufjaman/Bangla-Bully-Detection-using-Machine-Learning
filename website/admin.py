from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)


@admin.route('/')
def admin_dashboard():
    return render_template("admin_dashboard.html")

@admin.route('/customers-info')
def customers_info():
    return render_template("customers_info.html")
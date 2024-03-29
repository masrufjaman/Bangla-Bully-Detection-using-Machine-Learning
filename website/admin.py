from flask import Blueprint, render_template
from website.models import *

admin = Blueprint('admin', __name__)


@admin.route('/')
def admin_dashboard():
    customers = User.query.all()
    return render_template("admin_dashboard.html",customers=customers)

@admin.route('/customers-info')
def customers_info():
    customers = User.query.all()
    return render_template("customers_info.html",customers=customers)

@admin.route('/messages')
def customer_messages():
    messages = Message.query.all()
    return render_template("customer_messages.html", messages=messages)

@admin.route('/settings')
def settings():
    return render_template("admin_settings.html")
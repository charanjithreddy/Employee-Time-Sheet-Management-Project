from flask import Flask, render_template, request,flash,session
from routes.login_validate import login_validate
from models.user_credentials import user_credentials
import mysql.connector

app = Flask(__name__)

from routes.index_routes import index_bp
from routes.login_routes import login_bp
from routes.home_routes import home_bp
from routes.timesheet_entry_routes import timesheet_entry_bp
from routes.employee_login_creation_routes import employee_login_creation_bp
from routes.password_reset_route import password_reset_bp
from routes.logout_routes import logout_bp
from routes.password_reset_success_routes import password_reset_succes_bp

app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)
app.register_blueprint(timesheet_entry_bp)
app.register_blueprint(employee_login_creation_bp)
app.register_blueprint(password_reset_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(password_reset_succes_bp)

app.secret_key='acr' #secret key for using flash

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username_here',         # replace with your MySQL username
    'password': 'your_password_here', # replace with your MySQL password
    'database': 'flask_app'
}


if __name__ == "__main__":
    app.run(debug=True)
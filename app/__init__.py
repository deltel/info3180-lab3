from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphrase123'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '5b5dae88a29907'
app.config['MAIL_PASSWORD'] = '2a5e86cd1d71d7'

mail = Mail(app)
from app import views
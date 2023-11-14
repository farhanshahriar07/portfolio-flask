from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__, static_url_path='/static')

# Configure email settings for Gmail SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'samanthahaque2@gmail.com'
app.config['MAIL_PASSWORD'] = 'pksf adnc udfb hkpq '  # Use an App Password for more security
app.config['MAIL_DEFAULT_SENDER'] = 'samanthahaque2@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = 'frhnshhrr@gmail.com'
    subject = request.form['subject']
    name = request.form['from_name']
    message_body = f'<strong>Name :</strong> {name} <br><br><strong>Email:</strong> {request.form['recipient']}<br><br><strong>Message:</strong> {request.form['message_body']}'

    try:
        message = Message(subject, recipients=[recipient], body=message_body, html=message_body)
        message.body = message_body
        mail.send(message)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Error sending email: {str(e)}', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'  # Change this to a random secret key
    app.run()

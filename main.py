 
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

# Create a Flask app
app = Flask(__name__)

# Configure the mail server
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Initialize the mail object
mail = Mail(app)

# Define the route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for sending the email
@app.route('/send_email', methods=['POST'])
def send_email():
    # Get the form data
    sender = request.form['sender']
    recipient = request.form['recipient']
    subject = request.form['subject']
    message = request.form['message']

    # Create the email message
    msg = Message(subject, sender=sender, recipients=[recipient])
    msg.body = message

    # Send the email
    try:
        mail.send(msg)
        return redirect(url_for('success'))
    except Exception as e:
        return redirect(url_for('error'))

# Define the route for the success page
@app.route('/success')
def success():
    return render_template('success.html')

# Define the route for the error page
@app.route('/error')
def error():
    return render_template('error.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

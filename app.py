from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hemanthanamala110@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'hemanthkumar1234'  # Use an app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'hemanthanamala110@gmail.com'  # Your email address

mail = Mail(app)

@app.route('/')
def index():
    return render_template('imag.html')

@app.route('/thank_you')
def thank_you():
    return render_template('Thank_you.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    print(request.form)  # Debug: Print form data to console

    try:
        # Get form data
        customer_email = request.form['email']  # Get customer email from the form
        quantity = request.form['quantity']
        delivery_address = request.form['delivery']
        payment_method = request.form['payment']
        rating = request.form['rating']
        
        # Create email content
        subject = 'New Order from Customer'
        body = f"""
        You have received a new order!

        Customer Email: {customer_email}
        Quantity (in KGs): {quantity}
        Delivery Address: {delivery_address}
        Payment Method: {payment_method}
        Rating: {rating}
        """

        # Prepare the email message
        msg = Message(subject, recipients=['hemanthanamala110@gmail.com'])
        msg.body = body

        # Send the email
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except KeyError as e:
        flash(f'Missing form field: {str(e)}', 'error')
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'error')

    return redirect(url_for('thank_you'))

if __name__ == '__main__':
    app.run(debug=True)

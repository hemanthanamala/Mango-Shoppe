from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # This will render the HTML form

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    roll_number = request.form['roll']
    
    # Print form data to the console
    print(f'Name: {name}, Email: {email}, Mobile: {mobile}, Roll Number: {roll_number}')
    
    # Display a confirmation message
    return f"Form submitted! Name: {name}, Email: {email}, Mobile: {mobile}, Roll Number: {roll_number}"

if __name__ == '__main__':
    app.run(debug=True)

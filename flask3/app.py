from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global dictionary to store registered users
registered_users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    organization = request.form['organization']
    
    # Backend validation
    if not name or organization not in ['Org1', 'Org2', 'Org3', 'Org4', 'Org5']:
        return "Invalid data. Please go back and try again."
    
    # Store the registration in the global dictionary
    registered_users[name] = organization
    
    # Redirect to the registered users page
    return redirect(url_for('registered_users'))

@app.route('/registered-users')
def registered_users():
    return render_template('registered_users.html', users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)

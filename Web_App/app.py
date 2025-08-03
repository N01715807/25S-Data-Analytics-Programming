from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os, json

from data_analysis import clean_and_summarize
from data_visualization import generate_charts

# Import the separated logic modules
#from data_analysis import clean_and_summarize
#from data_visualization import generate_charts

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use env var in production

# Uploads folder setup
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# JSON file for user storage
USERS_FILE = 'users.json'

# -------------------- Helper Functions --------------------

def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f)
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

# -------------------- Routes --------------------

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()

        if username in users:
            flash("Username already exists!")
            return redirect(url_for('register'))

        users[username] = generate_password_hash(password)
        save_users(users)
        flash("Registered successfully. Please login.")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            flash("Logged in successfully.")
            return redirect(url_for('upload'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Logged out successfully.")
    return redirect(url_for('home'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' not in session:
        flash("You must be logged in to upload.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return redirect(url_for('analyze', filename=file.filename))
    return render_template('upload.html')

@app.route('/analyze/<filename>')
def analyze(filename):
    if 'username' not in session:
        flash("Login required.")
        return redirect(url_for('login'))

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    summary, cleaned_filename = clean_and_summarize(filepath)

    return render_template('analysis.html', summary=summary, filename=cleaned_filename)

@app.route('/visualize/<filename>')
def visualize(filename):
    if 'username' not in session:
        flash("Please log in to view visualizations.")
        return redirect(url_for('login'))

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    chart_paths = generate_charts(filepath)

    return render_template('visualizations.html', charts=chart_paths)

    # return "<p>Chart generation coming soon...</p>"

# -------------------- Run --------------------
if __name__ == '__main__':
    app.run(debug=True)
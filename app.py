from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # You can later process the POST data here if needed
        flash('Event(s) created successfully!')
        return redirect(url_for('index'))
    return render_template('schedule.html')  # your HTML file is named event_form.html

if __name__ == '__main__':
    app.run(debug=True)

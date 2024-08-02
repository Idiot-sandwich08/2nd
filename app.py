from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


submissions = []

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gig = request.form['gig']
        description = request.form['description']
        submission = {
            'name': name,
            'email': email,
            'gig': gig,
            'description': description
        }
        submissions.append(submission)
        return redirect(url_for('view_submissions'))
    return render_template('submit.html')

@app.route('/view_submissions')
def view_submissions():
    return render_template('view_submissions.html', submissions=submissions)

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(submissions):
        submissions.pop(index)
    return redirect(url_for('view_submissions'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


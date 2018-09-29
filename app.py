from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    
    return render_template('index.html')

@app.route('/home')
def user_home():
    
    return render_template('home.html')

@app.route('/newmeetup')

def new_meetup():
    
    
    return render_template('newmeetup.html')

@app.route('/create', methods=['POST'])
def create():
    
    return str(request.form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import sqlite3
from queries import *

app = Flask(__name__)


@app.route('/')
def root():
    
    return render_template('index.html')

@app.route('/home/<user>')
def user_home(user):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(get_meetups_query, [user])
    rows = cur.fetchall()
    return render_template('home.html', meetups = rows)

@app.route('/newmeetup')
def new_meetup():
    
    return render_template('newmeetup.html')

@app.route('/create', methods=['POST'])
def create():
    usr = 'chris'
    name = request.form['name']
    address = request.form['address']
    meetup_date = request.form['meetup_date']
    meetup_time = request.form['meetup_time']
    invites = request.form['invites']
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute(add_meetup_query,
                    [usr, name, address, meetup_date, meetup_time, invites])
        con.commit()
        
    return str(request.form)


if __name__ == '__main__':
    app.run(debug=True)

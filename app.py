from flask import Flask, render_template, request
import sqlite3
from queries import *
import datetime
from urllib.parse import quote
import requests

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/home/<user>')
def user_home(user):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(get_all_meetups_query, (user, '%'+user+'%'))
    rows = cur.fetchall()
    upcoming = []
    previous = []
    for r in rows:
        if datetime.datetime.strptime(r['meetup_date'], '%Y-%m-%d') >= datetime.datetime.today():
            upcoming.append(r)
        else:
            previous.append(r)
    
    return render_template('home.html', upcoming = upcoming, previous = previous, user = user)

@app.route('/newmeetup/<user>')
def new_meetup(user):
    
    return render_template('newmeetup.html', user = user)

@app.route('/create', methods=['POST'])
def create():
    user = request.form['user']
    name = request.form['name']
    address = request.form['address']
    meetup_date = request.form['meetup_date']
    meetup_time = request.form['meetup_time']
    invites = request.form['invites'].replace('\r\n', '*')
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute(add_meetup_query,
                    [user, name, address, meetup_date, meetup_time, invites])
        con.commit()
        
    return 'done'

@app.route('/meetup/<name>')
def existing_meetup(name):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(get_meetup_query, (name,))
    row = cur.fetchall()[0]
    address = row['address']
    r = requests.get(geocoder_url + quote(address))
    print(r.text)
    return render_template('meetup.html', info = row)



if __name__ == '__main__':
    app.run(debug=True)

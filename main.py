from flask import Flask, render_template, url_for, request
from datetime import datetime

app = Flask(__name__)


movies = [{'mTitle': 'Armageddon', 'mType': 'Disaster Film/Thriller', 'mreleaseDate': 'June 30, 1998', 'mfeaturedSong': 'I Don\'t Want to Miss a Thing', 'mDirector': 'Michael Bay'},
          {'mTitle': 'The Green Mile', 'mType': 'Drama/Fantasy', 'mreleaseDate': 'December 6, 1999', 'mfeaturedSong': 'Cheek to Cheek', 'mDirector': 'Frank Darabont'},
          {'mTitle': 'Lady in the Water', 'mType': 'Fantasy/Thriller', 'mreleaseDate': 'July 21, 2006', 'mfeaturedSong': 'None', 'mDirector': 'M. Night Shyamalan'},
          {'mTitle': 'Notting Hill', 'mType': 'Drama/Romance', 'mreleaseDate': 'May 13, 1999', 'mfeaturedSong': 'She', 'mDirector': 'Roger Michell'}]

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
@app.route('/dashboard')
def index():
	return render_template('index.html', title='DashBoard')

@app.route('/movielist')
def movieList():
	return render_template('movielist.html', title='Movies List', movies=movies)

if __name__=='__main__':
	app.run(debug=True)
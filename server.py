import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def get_club_by_email(email, clubs):
    for club in clubs:
        if club["email"] == email:
            return club
    return None


def get_club_by_name(name, clubs):
    for club in clubs:
        if club["name"] == name:
            return club
    return None


def get_competition_by_name(name, competitions):
    for competition in competitions:
        if competition["name"] == name:
            return competition
    return None


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    club = get_club_by_email(request.form['email'], clubs)
    if club is None:
        flash("Sorry, this email is not registered.")
        return render_template('index.html')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = get_club_by_name(club, clubs)
    foundCompetition = get_competition_by_name(competition, competitions)
    if foundClub is None:
        flash("Something went wrong-please try again")
        return render_template('index.html')
    if foundCompetition is None:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=foundClub,
                               competitions=competitions)
    return render_template('booking.html', club=foundClub,
                           competition=foundCompetition)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
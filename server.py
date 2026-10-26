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


def parse_places(value):
    try:
        return int(value)
    except ValueError:
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


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = get_competition_by_name(request.form['competition'],
                                          competitions)
    club = get_club_by_name(request.form['club'], clubs)
    if club is None:
        flash("Something went wrong-please try again")
        return render_template('index.html')
    if competition is None:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club,
                               competitions=competitions)
    placesRequired = parse_places(request.form['places'])
    if placesRequired is None:
        flash("Please enter a valid number of places.")
        return render_template('booking.html', club=club,
                               competition=competition)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    club['points'] = int(club['points']) - placesRequired
    flash(f"Great-booking complete! {placesRequired} places booked.")
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

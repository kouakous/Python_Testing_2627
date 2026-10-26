import json
import os
from datetime import datetime
from flask import Flask,render_template,request,redirect,flash,url_for

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def loadClubs():
    path = os.path.join(BASE_DIR, 'clubs.json')
    with open(path, encoding='utf-8') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    path = os.path.join(BASE_DIR, 'competitions.json')
    with open(path, encoding='utf-8') as comps:
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


MAX_PLACES_PER_COMPETITION = 12


def is_past(competition):
    date = datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
    return date < datetime.now()


def get_booked_places(bookings, competition_name, club_name):
    return bookings.get((competition_name, club_name), 0)


def record_booking(bookings, competition_name, club_name, places):
    key = (competition_name, club_name)
    bookings[key] = bookings.get(key, 0) + places


def validate_booking(club, competition, places, already_booked=0):
    if is_past(competition):
        return "This competition is already over."
    if places <= 0:
        return "Please enter a positive number of places."
    if already_booked + places > MAX_PLACES_PER_COMPETITION:
        return "You cannot book more than 12 places in a competition."
    if int(competition["numberOfPlaces"]) <= 0:
        return "This competition is full."
    if places > int(competition["numberOfPlaces"]):
        return "Not enough places available in this competition."
    if places > int(club["points"]):
        return "You do not have enough points."
    return None


def get_points_board(clubs):
    return sorted(clubs, key=lambda club: club["name"])


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
bookings = {}

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
    if is_past(foundCompetition):
        flash("This competition is already over.")
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
    already_booked = get_booked_places(bookings, competition['name'],
                                       club['name'])
    error = validate_booking(club, competition, placesRequired,
                             already_booked)
    if error is not None:
        flash(error)
        return render_template('booking.html', club=club,
                               competition=competition)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    club['points'] = int(club['points']) - placesRequired
    record_booking(bookings, competition['name'], club['name'],
                   placesRequired)
    flash(f"Great-booking complete! {placesRequired} places booked.")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/points')
def points():
    return render_template('points.html', clubs=get_points_board(clubs))


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()

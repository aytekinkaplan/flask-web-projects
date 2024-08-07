from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    premier_league_stats = {
        "Manchester City": {
            "position": 1,
            "played": 32,
            "won": 22,
            "drawn": 5,
            "lost": 5,
            "goals_for": 72,
            "goals_against": 31,
            "goal_difference": 41,
            "points": 71
        },
        "Arsenal": {
            "position": 2,
            "played": 32,
            "won": 22,
            "drawn": 4,
            "lost": 6,
            "goals_for": 75,
            "goals_against": 26,
            "goal_difference": 49,
            "points": 70
        },
        "Liverpool": {
            "position": 3,
            "played": 32,
            "won": 21,
            "drawn": 8,
            "lost": 3,
            "goals_for": 72,
            "goals_against": 31,
            "goal_difference": 41,
            "points": 71
        },
        "Aston Villa": {
            "position": 4,
            "played": 33,
            "won": 19,
            "drawn": 6,
            "lost": 8,
            "goals_for": 66,
            "goals_against": 47,
            "goal_difference": 19,
            "points": 63
        },
        "Tottenham Hotspur": {
            "position": 5,
            "played": 32,
            "won": 18,
            "drawn": 5,
            "lost": 9,
            "goals_for": 65,
            "goals_against": 49,
            "goal_difference": 16,
            "points": 59
        }
    }
    return render_template('index.html', premier_league_stats=premier_league_stats)

if __name__ == '__main__':
    app.run(debug=True)
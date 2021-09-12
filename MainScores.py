from flask import Flask, request
from Utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    with open(SCORES_FILE_NAME, 'r') as f:
        final_score = f.readline()
    message = f"""
    <html>
        <head>
            <title>Game Scores</title>
        </head>
        <body>
            <h1>The score is <div id="score">{final_score}</div></h1>
        </body>
    </html>"""
    print(f'This is your Final Score: {final_score}')

    return message


app.run(debug=True)

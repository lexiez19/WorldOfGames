from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def score_server():
    with open("/home/almogr/World_Of_Games/Docker/Scores.txt", 'r') as file:
        final_score = file.readline()
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')

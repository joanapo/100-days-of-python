from flask import Flask
import random

app = Flask(__name__)

guessed_number = random.randint(0,9)

@app.route("/")
def homepage():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjBzejI5OW9ycng0d3dqYnk2NGlkYzNpcXprcWw0bHQ0ZmNodGl6diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6YfTUIfDYjPdnk52/giphy.gif'>"

@app.route("/<int:number>")
def guess(number):
    if number < guessed_number:
        return "<h1 style='color:blue'>Too low</h1>" \
                "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTIwaDdzM2VvbjNnbGM2cHEzMW1qZjcyYTZsbDk4N3A1a216MGZtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lJb2v0QXan1omGL4Qo/giphy.gif'>"
    elif number > guessed_number:
        return "<h1 style='color:pink'>Too high</h1>" \
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnd0Z2hhNGEyOXJnbnlxanUwYnh4Mzg3b3duOTh1OGRmZHV4dXJndCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W2puJHMBNAkTp2mCpP/giphy.gif'>"
    else:
        return "<h1 style='color:purple'>You found me!</h1>"\
                "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExenEzcDQyeXY1cG05OXB5anZqdWo2NWQwbThyYmVkbXN6aWFzcTI0cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0NxaTiy78BOQBblLDV/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)
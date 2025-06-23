from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number,
                           name="Joana", year=current_year)

@app.route('/guess/<name>')
def guess(name):
    title_name = name.title()

    #genderize API
    gender_response = requests.get(f"https://api.genderize.io?name={name.lower()}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    #agify API
    age_response = requests.get(f"https://api.agify.io?name={name.lower()}")
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess.html", name=title_name, gender=gender, age=age)

@app.route('/blog/<num>')
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
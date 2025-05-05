from flask import Flask, request, render_template
from recommender import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    title = ""
    if request.method == "POST":
        title = request.form.get("title")
        recommendations = get_recommendations(title)
    return render_template("index.html", recommendations=recommendations, title=title)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from scrapers.youtube_scraper import get_youtube_data
from scrapers.amazon_scraper import get_amazon_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    search_term = request.form['search']
    youtube_results = get_youtube_data(search_term)
    amazon_results = get_amazon_data(search_term)
    return render_template('results.html', yt_data=youtube_results, amz_data=amazon_results)

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 10000))  # fallback to 10000 for local
app.run(host="0.0.0.0", port=port)


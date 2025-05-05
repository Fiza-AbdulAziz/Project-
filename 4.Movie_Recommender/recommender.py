import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load and preprocess data
df = pd.read_csv('C:/Users/FIZA ABDUL AZIZ/DS/project assignment/4. Movie_Recommender/data/movies_data.csv', encoding='utf-8')
df = df[['title', 'overview']].dropna().drop_duplicates(subset='title')

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['overview'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Map indices to titles
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def get_recommendations(title, num=5):
    idx = indices.get(title)
    if idx is None:
        return []
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()


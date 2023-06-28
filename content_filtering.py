from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

shared = pd.read_csv('shared_articles.csv')
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(shared['title'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
# shared['title'] = shared['title'].reset_index()
indices = pd.Series(shared.index, index = shared['title'])

def get_recomendation(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    return shared[['title','text','lang']].iloc[movie_indices]
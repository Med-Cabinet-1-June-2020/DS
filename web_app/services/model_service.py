from joblib import load


def modelservice(features, pg_curs):

    tfidf = load('vectorizer.joblib')
    text_transformed = tfidf.transform(features)

    model = load('strain_recommender.joblib')
    prediction = model.kneighbors(text_transformed.todense())
    prediction = tuple(prediction[1][0])

    query = f'''SELECT index, strain, "Type", "Rating", flavors, positive, negative, medical, "Description" FROM medcabinet WHERE index in {prediction} ORDER BY "Rating" DESC;'''

    pg_curs.execute(query)
    result = pg_curs.fetchall()

    return result

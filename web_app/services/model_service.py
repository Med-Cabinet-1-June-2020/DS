from joblib import load


def modelservice(features, pg_curs):

    tfidf = load('vectorizer.joblib')
    text_transformed = tfidf.transform(features)

    model = load('strain_recommender.joblib')
    prediction = model.kneighbors(text_transformed.todense())
    prediction = tuple(prediction[1][0])

    query = f'''SELECT index, strain, "Type", "Rating", flavors, positive, negative, medical, "Description" FROM medcabinet WHERE index in {prediction} ORDER BY "Rating" DESC;'''

    pg_curs.execute(query)

    desc = pg_curs.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))
            for row in pg_curs.fetchall()]

    return data

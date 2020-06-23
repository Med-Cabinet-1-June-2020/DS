from joblib import load
# import en_core_web_sm
# nlp = en_core_web_sm.load()

def get_lemmas(text):

    lemmas = []
    # STOP_WORDS = nlp.Defaults.stop_words.union([])

    doc = nlp(text)

    for token in doc: # ignore first two elements containing blank space and date
        if ((token.is_stop == False) and (token.is_punct == False)) and (token.pos_ != 'PRON') \
                and (token.is_space == False) and (token.is_digit == False):
            lemmas.append(token.lemma_.lower())

    return lemmas

def modelservice(features, pg_curs):
    tfidf = load('vectorizer.joblib')
    text_transformed = tfidf.transform(features)

    model = load('strain_recommender.joblib')
    prediction = model.kneighbors(text_transformed.todense())

    print(prediction)

    prediction = tuple(prediction[1][0])

    query = f'''SELECT * FROM strains WHERE index in {prediction} ORDER BY "Rating" DESC'''
    pg_curs.execute(query)
    result = pg_curs.fetchall()

    return result
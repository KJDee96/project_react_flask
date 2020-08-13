from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances


def get_corpus(query):
    i = 0
    text = []
    while i < len(query):
        text.append(query[i].job_description)
        i += 1
    return text


def get_tfidf(query):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tf_idf_weights = tfidf_vectorizer.fit_transform(get_corpus(query))
    return tfidf_vectorizer, tf_idf_weights


def get_cosine(tfidf_vectorizer, weights, document):
    vector = tfidf_vectorizer.transform([document])
    return cosine_similarity(vector, weights).flatten()


def get_euc(tfidf_vectorizer, weights, document):
    vector = tfidf_vectorizer.transform([document])
    return euclidean_distances(vector, weights).flatten()


def get_doc_ids(matches):
    matches_with_id = dict()
    i = 0
    for item in matches:
        matches_with_id[i] = item
        i += 1

    id_list = []
    matches_with_id_sorted = dict(sorted(matches_with_id.items(),
                                         key=lambda element: element[1],reverse=True))  # result of sorted = list of tuples
    for x, y in list(matches_with_id_sorted.items())[:50]:  # start from 0, stop at 100
        if y != 0.0:
            id_list.append(x)
    return id_list

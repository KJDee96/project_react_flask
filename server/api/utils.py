from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer


def get_tfidf(query):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tf_idf_weights = tfidf_vectorizer.fit_transform(query)
    return tfidf_vectorizer, tf_idf_weights


def get_cosine(tfidf_vectorizer, weights, document):
    vector = tfidf_vectorizer.transform([document])
    return cosine_similarity(vector, weights).flatten()


def get_euc(tfidf_vectorizer, weights, document):
    vector = tfidf_vectorizer.transform([document])
    return euclidean_distances(vector, weights).flatten()


def get_doc_ids(matches, data, amount, doc_id):
    matches_with_id = {key: item for (key, item) in zip(range(len(matches)), matches)}

    # result of sorted = list of tuples so convert to dict
    matches_with_id_sorted = dict(sorted(matches_with_id.items(),
                                         key=lambda element: element[1], reverse=True))

    id_list = [x for x, y in list(matches_with_id_sorted.items())[:amount]]  # slice = start from 0, stop at int(amount)

    # list of all job ids from the data parameter as index != id, and I get index from weight list
    return [data[item_id] for item_id in id_list if data[item_id] != doc_id]


class Tfidf:
    def __init__(self, query):
        self.vectorizer, self.weights = get_tfidf(query)

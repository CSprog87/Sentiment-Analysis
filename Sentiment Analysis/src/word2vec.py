from typing import List

import numpy as np
from gensim.models.word2vec import Word2Vec


def vectorizer(
    corpus: List[List[str]], model: Word2Vec, num_features: int = 100
) -> np.ndarray:
    """
    This function takes a list of tokenized text documents (corpus) and a pre-trained
    Word2Vec model as input, and returns a matrix where each row represents the
    vectorized form of a document.

    Args:
        corpus : list
            A list of text documents that needs to be vectorized.

        model : Word2Vec
            A pre-trained Word2Vec model that will be used to vectorize the corpus.

        num_features : int
            The size of the vector representation of each word. Default is 100.

    Returns:
        corpus_vectors : numpy.ndarray
            A 2D numpy array where each row represents the vectorized form of a
            document in the corpus.
    """
    corpus_vectors = np.zeros((len(corpus), num_features), dtype='float32')
    
    for i, tokens in enumerate(corpus):
        feature_vector = np.zeros((num_features,), dtype='float32')
        num_words = 0

        for word in tokens:
            if word in model.wv:
                feature_vector = np.add(feature_vector, model.wv[word])
                num_words += 1
        
        if num_words > 0:
            feature_vector = np.divide(feature_vector, num_words)
        corpus_vectors[i] = feature_vector
    
    return corpus_vectors        
    


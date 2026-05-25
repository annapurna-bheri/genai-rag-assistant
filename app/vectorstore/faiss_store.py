import faiss
import numpy as np


dimension = 32

index = faiss.IndexFlatL2(
    dimension
)

documents = []


def add_vector(vector, text):

    global documents

    np_vector = np.array(
        [vector],
        dtype="float32"
    )

    index.add(np_vector)

    documents.append(text)


def search_vector(vector, k=3):

    np_vector = np.array(
        [vector],
        dtype="float32"
    )

    distances, indices = index.search(
        np_vector,
        k
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):

            results.append(
                documents[idx]
            )

    return results
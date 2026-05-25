import hashlib
import numpy as np


def generate_embedding(text):

    hash_object = hashlib.sha256(
        text.encode()
    ).digest()

    vector = np.frombuffer(
        hash_object,
        dtype=np.uint8
    )

    vector = vector.astype("float32")

    return vector.tolist()
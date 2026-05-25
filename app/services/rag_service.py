import json

from app.services.embedding_service import (
    generate_embedding
)

from app.vectorstore.faiss_store import (
    add_vector,
    search_vector
)

from app.services.chunk_service import (
    chunk_text
)

from app.services.llm_service import (
    generate_response
)

from app.prompts.prompt_template import (
    PROMPT_TEMPLATE
)

conversation_memory = {}

def load_documents():

    with open("docs.json", "r") as file:

        docs = json.load(file)

    for doc in docs:

        chunks = chunk_text(
            doc["content"]
        )

        for idx, chunk in enumerate(chunks):

            embedding = generate_embedding(
                chunk
            )

            metadata = {
                "title": doc["title"],
                "chunk": chunk,
                "chunk_id": idx
            }

            add_vector(
                embedding,
                metadata
            )

def chat(session_id, message):

    query_embedding = generate_embedding(
        message
    )

    retrieved_docs = search_vector(
        query_embedding
    )

    if len(retrieved_docs) == 0:

        return {
            "reply":
            "I could not find enough information.",
            "retrievedChunks": 0
        }

    context = "\n".join([
        doc["chunk"]
        for doc in retrieved_docs
    ])

    history = conversation_memory.get(
        session_id,
        []
    )

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        history=history,
        question=message
    )

    response = generate_response(
        prompt
    )

    history.append({
        "user": message,
        "assistant": response
    })

    conversation_memory[session_id] = history[-5:]

    return {
        "reply": response,
        "retrievedChunks": len(retrieved_docs)
    }
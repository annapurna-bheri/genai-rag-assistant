def generate_response(prompt):

    lines = prompt.split("Context:")

    if len(lines) > 1:

        context_part = lines[1]

        return (
            "Based on retrieved documents:\n\n"
            + context_part[:500]
        )

    return "No relevant information found."
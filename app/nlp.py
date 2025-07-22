import re

def process_input(user_input):
    """
    Processes the user's natural language input and returns a structured command.
    """
    # This is a very basic implementation. It will be expanded upon later.
    # For now, it just looks for keywords.
    user_input = user_input.lower()

    if "create a file" in user_input:
        # Try to extract the filename
        match = re.search(r"create a file named (.+)", user_input)
        if match:
            filename = match.group(1)
            return {"command": "create_file", "filename": filename}
        else:
            return {"command": "error", "message": "Could not determine filename."}

    if "hello" in user_input:
        return {"command": "greet"}

    return {"command": "unknown"}

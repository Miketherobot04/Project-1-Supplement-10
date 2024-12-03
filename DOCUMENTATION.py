def save_document(document):
    """
    Saves a document to the MongoDB collection.

    Args:
        document (dict): The document to save, must include a UUID field.

    Returns:
        None
    """
    collection.insert_one(document)
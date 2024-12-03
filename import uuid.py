import uuid

def create_random_document():
    return {
        "UUID": str(uuid.uuid4()),
        "name": "Sample Name",
        "age": 30,
        "created_at": "2024-12-02"
    }
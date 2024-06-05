from bson import ObjectId


def serialize_dict(item) -> dict:
    return {k: str(v) if isinstance(v, ObjectId) else v for k, v in item.items()}

def serialize_list(entity) -> list:
    return [serialize_dict(item) for item in entity]

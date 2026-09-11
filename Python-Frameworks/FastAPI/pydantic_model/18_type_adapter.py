# ============================================================
#                     TYPEADAPTER
#
# TypeAdapter → Validates, parses and serializes Python types without requiring a BaseModel
#
# validate_python() → Validates Python objects
# validate_json()   → Validates JSON data
# dump_python()     → Converts data into Python representation
# dump_json()       → Converts data into JSON bytes
# json_schema()     → Generates JSON Schema for the type
# ============================================================


from fastapi import FastAPI
from pydantic import BaseModel, TypeAdapter


app = FastAPI()


# User Model

class User(BaseModel):

    name: str
    age: int


# TypeAdapter for list of Users

users_adapter = TypeAdapter(list[User])


# ------------------------------------------------------------
# validate_python()
# ------------------------------------------------------------

@app.post("/validate-python")
def validate_python(users: list[User]):

    validated_users = users_adapter.validate_python(
        users
    )

    return {
        "message": "Python data validated successfully",
        "users": validated_users
    }


# ------------------------------------------------------------
# validate_json()
# ------------------------------------------------------------

@app.post("/validate-json")
def validate_json():

    json_data = """
    [
        {
            "name": "Gaurav",
            "age": 22
        },
        {
            "name": "Rahul",
            "age": 23
        }
    ]
    """

    validated_users = users_adapter.validate_json(
        json_data
    )

    return {
        "message": "JSON data validated successfully",
        "users": validated_users
    }


# ------------------------------------------------------------
# dump_python()
# ------------------------------------------------------------

@app.post("/dump-python")
def dump_python(users: list[User]):

    validated_users = users_adapter.validate_python(
        users
    )

    python_data = users_adapter.dump_python(
        validated_users
    )

    return {
        "message": "Data dumped as Python representation",
        "users": python_data
    }


# ------------------------------------------------------------
# dump_json()
# ------------------------------------------------------------

@app.post("/dump-json")
def dump_json(users: list[User]):

    validated_users = users_adapter.validate_python(
        users
    )

    json_data = users_adapter.dump_json(
        validated_users
    )

    return {
        "message": "Data dumped as JSON",
        "users": json_data.decode()
    }


# ------------------------------------------------------------
# json_schema()
# ------------------------------------------------------------

@app.get("/json-schema")
def json_schema():

    schema = users_adapter.json_schema()

    return {
        "schema": schema
    }

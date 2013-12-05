from jsonschema import validate, ValidationError

schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}

if __name__ == '__main__':
    from minitest import *
    with test("validate"):
        # If no exception is raised by validate(), the instance is valid.
        validate({"name" : "Eggs", "price" : 34.99}, schema).must_equal(None)
        # (validate({"name" : "Eggs", "price" : 34.99}, schema)==None).must_true()
        (lambda : validate({"name" : "Eggs", "price" : "Invalid"}, schema)).must_raise(
            ValidationError, "'Invalid' is not of type 'number'\n\nFailed validating 'type' in schema['properties']['price']:\n    {'type': 'number'}\n\nOn instance['price']:\n    'Invalid'")


import json


def to_json(_object):
    """
    Method used to convert objects to json strings
    :param _object: The object to be transformed
    :return: The json string of the object
    """
    return json.dumps(_object.__dict__)


def from_json(_json, _object):
    """
    Method used to convert json string to python object
    :param _object: The target python object passed by reference
    :param _json: The json string
    :return: The newly created object
    """
    new_object = _object()
    new_object.__dict__ = json.loads(_json)
    return new_object


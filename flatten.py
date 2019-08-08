def flatten(nested_json, name='', out={}):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    if type(nested_json) is dict:
        for key in nested_json:
            out = flatten(nested_json[key], name + key + '_', out)
    elif type(nested_json) is list:
        i = 0
        for itm in nested_json:
            out = flatten(itm, name + str(i) + '_', out)
            i += 1
    else:
        out[name[:-1]] = nested_json
    return out

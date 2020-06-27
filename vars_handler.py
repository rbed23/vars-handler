import json

TRUNC_LIMIT=50

def show_vars(vars_object, trunc_limit=int(TRUNC_LIMIT)):
    if isinstance(vars_object, str):
        print("TypeError: object argument must be of <class dict>")
        return "TypeError: object argument must be of <class dict>"
    if not isinstance(trunc_limit, int):
        return "TypeError: trunc_limit argument must be of <class int>"
    try:
        if not isinstance(vars(vars_object), dict):
            return "TypeError: argument must be of <class dict>"
    except TypeError as typ_err:
        return f"TypeError: {typ_err}"
    try:
        kvs = {
                (x[0], (str(x[1])[:trunc_limit] + f" (<<<---truncated at"
                                                f" {trunc_limit} chars)") if\
                                    len(str(x[1])) > trunc_limit else str(x[1]))
                for x in vars(vars_object).items()
            }
        __kvs = {x for x in kvs if x[0].startswith('_')}

        new = { **dict(sorted(__kvs, reverse=True)), 
                **dict(sorted(kvs, key=lambda x: (x[0].upper(), x[0].islower())))}

        print(json.dumps(new, indent=4))
        print(f"Use the format 'object'.'key_name' to"
                " access the specific attribute.")
    except TypeError as typ_err:
        print(json.dumps(dict(vars_object), indent=4))
    except NameError as nm_err: 
        return f"NameError [vars()]: {nm_err}"


if __name__ == "__main__":
    vars_object = input("Enter the object: ")
    print(type(vars_object), vars_object)
    show_vars(vars_object)

import json

TRUNC_LIMIT=50


def dump_vars(obj, trunc_limit=int(TRUNC_LIMIT)):
    try:
        kvs = {
                (x[0], (str(x[1])[:trunc_limit] + f" (<<<---truncated at"
                                                f" {trunc_limit} chars)") if\
                                    len(str(x[1])) > trunc_limit else str(x[1]))
                for x in vars(obj).items()
            }
        __kvs = {x for x in kvs if x[0].startswith('_')}

        new = { **dict(sorted(__kvs, reverse=True)), 
                **dict(sorted(kvs, key=lambda x: (x[0].upper(), x[0].islower())))}

        print(json.dumps(new, indent=4))
        print(f"Use the format 'object'.'key_name' to"
                " access the specific attribute.")
    except TypeError as typ_err:
        try:
            print(json.dumps(dict(obj), indent=4))
        except Exception as exc:
            print(f"Error: Cannot handle this object: {exc}")
    except NameError as nm_err: 
        print(f"NameError: {nm_err}")


def show_vars(vars_object, trunc_limit=int(TRUNC_LIMIT)):
    if isinstance(vars_object, str) or isinstance(vars_object, int):
        return TypeError("object argument must be of <class dict>")
    if not isinstance(trunc_limit, int):
        return TypeError("trunc_limit argument must be of <class int>")
    try: 
        print(json.dumps(vars_object, indent=4))
    except:
        dump_vars(vars_object, trunc_limit)

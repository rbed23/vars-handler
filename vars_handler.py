import json

TRUNC_LIMIT=50


def dump_vars(obj, trunc: int = TRUNC_LIMIT, keys: bool = False) -> dict:
    '''
    Prettify show object dict corresponding to its symbol table

    :type obj: any
    :desc obj: any defined object variable
    '''
    if isinstance(obj, str) or isinstance(obj, int):
        raise TypeError("object must have __dict__ method")

    # validate argument as type <int>
    trunc = check_trunc_type(trunc)

    if check_keys(keys): # print only keys list
        vars_keys = sorted(
                        [x for x in vars(obj).keys()],
                        key=lambda x: x.casefold())
        print(json.dumps(vars_keys, indent=2))

    else: # print attributes with values
        try:
            kvs = {(x[0],(str(x[1])[:trunc] + " (<<<---truncated)")\
                    if len(str(x[1])) > trunc\
                    else str(x[1]))\
                for x in vars(obj).items()}

            _kvs = {x for x in kvs if x[0].startswith('_')}

            new = { **dict(sorted(_kvs, reverse=True)), 
                    **dict(sorted(kvs, key=lambda x: x[0].casefold()))}
            print(json.dumps(new, indent=4))

        except TypeError as typ_err:
            try:
                print(json.dumps(dict(obj), indent=4))

            except Exception as exc:
                print(f"Error: Cannot handle this object: {exc}")

        except NameError as nm_err: 
            print(f"NameError: {nm_err}")


def dump_dir(obj) -> list:
    '''
    Prettify show object attribute keys

    :type obj: any
    :desc obj: any defined object variable
    '''
    try:
        ks = sorted(
                [x for x in dir(obj)],
                key=lambda x: x.casefold())
        print(json.dumps(ks, indent=2))
    except Exception as exc:
        print(f"{exc}")


def show_attrs(obj, trunc: int = TRUNC_LIMIT, keys: bool = False) -> dict:
    '''
    Prettify show object responses from vars() and dir()

    :type obj: any
    :desc obj: any defined object variable
    '''

    try:
        print(json.dumps(obj, indent=4))

    except TypeError:
        try:
            if not obj.__dict__:
                dump_dir(obj)
            else:
                line = "Scoped Attributes"
                print(line)
                print("-" * (len(line)+1))
                dump_vars(obj, trunc, keys)
                vars_keys = [x for x in vars(obj).keys()]
                diff_list = sorted(list(set(dir(obj)).difference(vars_keys)))
                if len(diff_list):
                    line = "\nAttributes Scoped from Parent"
                    print(line)
                    print("-" * len(line))
                    print(json.dumps(diff_list, indent=2))
        except AttributeError as attr_err:
            dump_dir(obj)


def check_trunc_type(trunc: int) -> int:
    if not isinstance(trunc, int):
        print("WARNING: 'trunc' arg is not of type <int>; using default value")
        return TRUNC_LIMIT
    else:
        return trunc


def check_keys(keys: bool) -> bool:
    if not isinstance(keys, bool):
        print("WARNING: 'keys' arg is not of type <bool>; using default value")
        return False
    else:
        return keys

import inspect
from functools import wraps
from collections import OrderedDict

def parameter_types(*pos_types, **kw_types):
    ''' A decorator factory function that does type checking if used
    as a decorator on a function.
    
    Usage:
    @parameter_types(
        int, str, (int), x=str, y=tuple
    )
    def func(a, c, *args, **kwargs):
        ...
    '''
    def decorator(func):
        
        @wraps(func)
        def do_checks(*args, **kwargs):
            error_str = lambda type_passed, type_expected: (
                f"Argument of {type_passed} passed, {type_expected} expected." 
            )
            err_dict = {
                'other': {},
                'args': {},
                'kwargs': {}
            }
            other_pos_types = []
            var_kw_types = []
            var_pos_types = []
            var_pos_types_done = False
            for _type in pos_types:
                if isinstance(_type, tuple):
                    if var_pos_types_done:
                        raise Exception(
                            "Cannot have more than one " +
                            "*args tuple specified in parameter_types."
                        )
                    var_pos_types_done = True
                    var_pos_types = [t for t in _type]
                    continue
                other_pos_types.append(_type)
            
            if len(kw_types) != len(kwargs):
                raise Exception(
                    f"The number of keyword arguments passed is {len(kwargs)}, " +
                    f"but the number of types specified is {len(kw_types)}."
                )

            for param_name, param_value in kwargs.items():
                if var_kw_types[param_name] != type(param_value):
                    err_dict['kwargs'][param_name] = error_str(
                        type(param_value), var_kw_types[param_name]
                    )
            
            if n_pos_types != n_args:
                raise Exception(
                    f"The number of non-keyword arguments passed is {n_args}, " +
                    f"but the number of types specified is {n_pos_types}."
                )

            for param in inspect.signature(func).parameters.values():
                
                if param.kind == param.VAR_POSITIONAL:
                    pass
                
                if param.kind == param.VAR_KEYWORD:


            err_dict = dict()
            for i, (_arg, _type) in enumerate(zip(args, types)):
                if not isinstance(_arg, _type):
                    err_dict[i] = (type(_arg), _type)

                raise Exception(
                    f"The {arg_position(i)} argument is {type(_arg)}. " +
                    f"Must be {_type}."
                )                    
            return fn(*args, **kwargs)
        return do_checks
    return decorator


@parameter_types(int, list)
def do_something(a, b):
    return str(a) + b

print(do_something('3', '4'))

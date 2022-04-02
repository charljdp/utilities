import inspect
from functools import wraps
from copy import deepcopy
from typing import OrderedDict

# def _add_to_error_msg(
#     error_msg,
#     type_passed,
#     type_expected,
#     param_kind,
#     param_name,
#     param_position
# ):
#     "Argument of {type_passed} passed, {type_expected} expected."
#     return error_msg



def io_types( 
    *arg_types,
    **kwarg_types
):
    ''' A decorator factory function that does type checking if used
    as a decorator on a function.
    
    Usage:
    @parameter_types(
        int, str, (int), x=str, y=tuple
    )
    def func(a, c, *args, **kwargs):
        ...
    
    p, *a
    p, *a, **k
    p, **k
    *a, **k
    **k
    *a
    p
    '''
    def decorator(func):
        
        @wraps(func)
        def do_checks(*args, **kwargs):
            
            error_str = lambda type_passed, type_expected: (
                f"Argument of {type_passed} passed, {type_expected} expected." 
            )
            
            if len(kwarg_types) != len(kwargs):
                raise Exception(
                    "Number of keyword argument types given "
                    "and number of keyword arguments passed "
                    "must be the same."
                )

            # Vanilla cases 
            arg_pos = 0
            for arg_type in arg_types:
                if isinstance(arg_type, tuple):
                    for var_arg_type in arg_type:
                        arg = args[arg_pos]
                        if not isinstance(arg, var_arg_type):
                            # Log/build error
                            pass
                        arg_pos += 1
                else:
                    arg = args[arg_pos]
                    if not isinstance(arg, arg_type):
                        # Log/build error
                        pass
                    arg_pos += 1
            
            for kwarg_type in kwarg_types:
                pass


            n_args_to_inspect = len(args) + len(kwargs)
            if n_types_specified > n_args_to_inspect:
                raise Exception("More types specified than passed arguments.")
            if n_types_specified < n_args_to_inspect:
                raise Exception("Less types specified than passed arguments.")

            # result = OrderedDict()
            # for _type in arg_types:
            #     if isinstance(_type, tuple):
            #         key = 'VAR_POSITIONAL'
            #     else:
            #         key = 'POSITIONAL'
            #     result[key] = _type
            # for _type in kwarg_types:
            #     result['KEYWORD'] = _type

            # arg_param_type_compare = {}
            # args_and_types = zip(arg_types, args)

            n_types_specified = len(kwarg_types)
            for arg_type in arg_types:
                if isinstance(arg_type, tuple):
                    n_types_specified += len(arg_type)
                else:
                    n_types_specified += 1
            
            {
                ''
            }
                    


            for param in inspect.signature(func).parameters.values():
                if param.kind ==
                if param.kind == param.POSITIONAL_ONLY:
                    arg_param_type_compare[param.name] = 


            positional_params = [
                param.name 
                for param in inspect.signature(func).parameters.values()
                if param.kind == param.POSITIONAL_ONLY
            ]
            var_positional_params = [
                param.name 
                for param in inspect.signature(func).parameters.values()
                if param.kind == param.VAR_POSITIONAL
            ]
            position = 0
            for _type in arg_types:
                if isinstance(_type, tuple):  
                    # Then we are dealing with var_positional arguments
                    for t in _type:
                        if isinstance()
                else:
                    # Then we are dealing with positional arguments



                
            for _type in kwarg_types:
                pass

            error_msg = ""
            args_index = 0
            kwargs_index = 0
            largs = deepcopy(args)
            lkwargs = deepcopy(kwargs)
            for param in inspect.signature(func).parameters.values():
                
                if param.kind == param.POSITIONAL_ONLY:
                    if not isinstance(largs[args_index], arg_types[args_index]):
                        error_msg += (
                            
                            f"For parameter {param.name}." + error_str(
                                type(kwarg), var_kw_types[param_name]
                            )
                        )
                    args_index += 1
                
                if param.kind == param.POSITIONAL_OR_KEYWORD:
                    if param.name in lkwargs
                    if not isinstance(largs[args_index]):

                    args_index += 1
                
                if param.kind == param.VAR_POSITIONAL:
                    pass
                
                if param.kind == param.KEYWORD_ONLY:
                    kwargs_index += 1
                if param.kind == param.VAR_KEYWORD:
                    kwargs_index += 1

                if param.kind == param.VAR_POSITIONAL:
                    for _type in var_pos_types:
                        if not isinstance(, _type):
                            err_dict['kwargs'][param_name] = error_str(
                                type(kwarg), var_kw_types[param_name]
                            )
                elif param.kind not in (param.VAR_KEYWORD, param.KEYWORD_ONLY):
                    pass
            if returns:
                if isinstance(returns, )
            if isinstance(func(*args, **kwargs)
            return fn(*args, **kwargs)
        return do_checks
    return decorator

def get_func_name(func):
    return type(func).__name__

# env means globals() or locals()
def get_funcation_in_env(env, func_name):
    return env[func_name]

def is_just_one_argument_and_name_equal(func, arg_name):
    # for int, str something like these methods which are either 'type' or 'function'
    if (get_func_name(func) == 'type'):
        return False
    def for_function():
        return (func.func_code.co_argcount == 1
            and func.func_code.co_varnames[-1] == arg_name)
    def for_partial():
        return (func.func.func_code.co_argcount-len(func.args) == 1 
            and func.func_code.co_varnames[-1] == arg_name)
    return get_funcation_in_env(locals(), 'for_'+get_func_name(func))()

def call_method_with_special_arg(func, module_names, arg_name):
    if is_just_one_argument_and_name_equal(func, arg_name):
        return [func(module_name) for module_name in module_names]
    else:
        return func()


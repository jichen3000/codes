

__all__ = ['comb']

def combinate(*funcs):
    def comb_func(*args, **kvargs):
        first_func = funcs[0]
        result = first_func(*args, **kvargs)
        others_reverse_funcs = funcs[1:]
        for func in others_reverse_funcs:
            result = func(result)
        return result
    return comb_func

comb = combinate

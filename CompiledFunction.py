import sys

def compiled(f):
    try:
        sys.modules[f.__name__] = __import__('gwlfe_compiled', globals(), locals(), [f.__name__], -1)
    except ImportError:
        print("Unable to load compiled version of " + f.__name__ + " using slow version")
    return f
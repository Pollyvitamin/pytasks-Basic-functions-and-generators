"""
Create simple function factory add_factory using 3 different approaches:

Interactive usage example:

>>> add5 = add_factory(5)
>>> print(add5(10))
15
"""

#first option, using closures:

def add_factory(base_arg):
  
    """
    Examples of use:
    >>> add5=add_factory(5)
    >>> print(add5(10))
    15
    """
    
    def inner(ext_arg):
        result=ext_arg+base_arg
        return result
    return inner

#second option, using decorators:

def add_factory(base_arg):
      
    """
    Examples of use:
    >>> @add_factory(5)
    >>> def add5(n):
    >>>   return n
    >>> print(add5(10))
    15
    """
  
    def decorator(fun):
        def inner(*args):
            result = fun(*args)
            return base_arg+result
        return inner
    return decorator

#third option, using functools.partial:

import functools

def add_factory(*args):
    return sum(args)

add5 = functools.partial(add_factory,5)
print(add5(10))

#fourth option, using class:

class AddFactory(object):
  
    """
    Examples of use:
    >>> add5=AddFactory(5)
    >>> print(add5(10))
    15
    """
  
    def __init__(self, base_arg):
        self.base_arg=base_arg
    def __call__(self, ext_arg):
        return ext_arg+self.base_arg

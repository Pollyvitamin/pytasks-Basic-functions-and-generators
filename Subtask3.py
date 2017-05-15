"""
Create function planify and generator planify2 to expand a nested sequence.

For example, you have nested sequences such as list, tuple, MyList:

class MyList(list):
    def __str__(self):
        return "<MyList>"

seq = ('abc', 3, [8, ('x', 'y'), MyList(xrange(5)), [100, [99, [98, [97]]]]])
print(planify(seq))
# ['abc', 3, 8, 'x', 'y', 0, 1, 2, 3, 4, 100, 99, 98, 97]
gen = planify2(seq)
print(type(gen))
# <type 'generator'>
print(list(gen))
# ['abc', 3, 8, 'x', 'y', 0, 1, 2, 3, 4, 100, 99, 98, 97]

Note 1: let's take the possible depth of nesting no more than 100.
"""

#second option - generator planify2 function:

import sys

sys.setrecursionlimit(100)

def planify2(seq):
    
    """
    Examples of use:
    >>> seq = ('abc', 3, [8, ('x', 'y'), MyList(xrange(5)), [100, [99, [98, [97]]]]])
    >>> gen = planify2(seq)
    >>> print(type(gen))
    <class 'generator'>
    >>> print(list(gen))
    ['abc', 3, 8, 'x', 'y', 0, 1, 2, 3, 4, 100, 99, 98, 97]
    """
    
    for element in seq:
        if isinstance(element, (list,tuple)):
            for item in planify2(element):
                yield item
        else:
            yield element

"""
Subtask 4

Make a generator izip_repeat(*iters) that aggregates elements from each of the iterables (sequences). If the iterables
 are of uneven (short) length, missing values are filled-in with elements of iterable started with beginning.

See usage examples bellow:

print(list(izip_repeat([0, 1, 2], 'mn')))
# [(0, 'm'), (1, 'n'), (2, 'm')]
print(list(izip_repeat('ABCD', 'xy')))
# [('A', 'x'), ('B', 'y'), ('C', 'x'), ('D', 'y')]
print(list(izip_repeat('xy', ['mn', 'op'] , range(5))))
# [('x', 'mn', 0), ('y', 'op', 1), ('x', 'mn', 2), ('y', 'op', 3), ('x', 'mn', 4)]
Moreover, make sure you created a generator not function:

import types
g = izip_repeat('ab', [0, 1])
print(type(g))
# <type 'generator'>
"""

def izip_repeat(*iters):

    # Abstract infinite generator:
    def infinite_gen(lst):
        while True:
            for item in lst:
                yield item

    # Abstract limited generator:
    def limited_gen(count, lst):
        n=0
        gen=infinite_gen(lst)
        while n<count:
            yield gen.__next__()
            n+=1

    # Define item's max length:
    def max_len(*iters):
        max_length=0
        for item in iters:
            if len(item) > max_length:
                max_length=len(item)
        return max_length

    # Make a zip generator:
    def zip_gen(*iters):
        prepared_lst=[]
        max_length=max_len(*iters)
        for item in iters:
            item=limited_gen(max_length,item)
            prepared_lst.append(item)
        result=zip(*prepared_lst)
        for item in result:
            yield item

    return zip_gen(*iters)

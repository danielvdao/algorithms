'''
some implementation of the 0-1 kp problem
given array of tuples and a weight
return the max amount you can get with that weight
'''


from collections import namedtuple

Item = namedtuple('item', ['weight', 'value'])

def kp(items, max_wt):
    print items, max_wt

item1 = Item(weight=20, value=5)
item2 = Item(weight=10, value=10)
item3 = Item(weight=1, value=3)
items = [item1, item2, item3]

print kp(items, 100)

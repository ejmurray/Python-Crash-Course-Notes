"""
Examples taken from Mouse vs python 101
https://goo.gl/9UrpVB
Also try the following from 201
https://goo.gl/by0rg7
Also look at the counter module.
2017-03-16 08:50:05
"""

# coding: utf-8
from collections import defaultdict
from collections import OrderedDict
my_dict = {}
my_other_dict = dict()
my_other_other_dict = {1: 'one', 2: 'two', 3: 'three'}
my_other_other_dict[1]
my_other_other_dict[4]
my_other_other_dict.get[4, None]
my_other_other_dict.get(4, None)
key = 4
if key in my_other_other_dict:
    print('Key ({}) found'.format(key))
else:
    print('Key ({}) NOT found'.format(key))

my_dict = {}
my_dict[1] = 'one'
my_dict[1]
my_dict[1] = 'something else'
my_dict[1]
my_dict
my_dict = {}
my_dict[1] = 'something else'
my_dict.pop(1, None)
my_dict.pop(2)
my_dict = {1: 'one', 2: 'two', 3: 'three'}
del my_dict[1]
my_dict
my_dict = {1: 'one', 2: 'two', 3: 'three'}
for key in my_dict:
    print(key)

my_dict = {1: 'one', 2: 'two', 3: 'three'}
my_dict.keys()
my_dict.values()
my_dict.items()
for item in my_dict.values:
    print(item)
for item in my_dict.values():
    print(item)

sentence = 'The red fox jumped over the fence and ran to the zoo'
words = sentence.split(' ')
d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
new_d
for key in new_d:
    print(key, new_d[key])

# saved from ipython using %save filename 1-48 (line numbers)
# get_ipython().magic('save file_collections 1-48')

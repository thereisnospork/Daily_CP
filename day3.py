# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
#

import numpy as np

def serialize_root(de_serialized):

    tree = dict()
    for i, each in enumerate(de_serialized):
        if i % 3 == 0: #identifying each root
            children = []
            try:
                children.append(de_serialized[i+1])
            except:
                None
            try:
                children.append(de_serialized[i+2])
            except:
                None
            tree[each]=children
#### first layer done / working, need to add recursion
    print(tree)

def de_serialize_root():
    None

de_serialized = np.arange(1,51)
print(de_serialized)

serialize_root(de_serialized)
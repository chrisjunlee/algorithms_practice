from test_data_0904 import long_test_list
import sys

from collections import defaultdict
def totalFruit(tree: 'List[int]') -> 'int':
    length, max_length = 0, 0
    tree_count = defaultdict(lambda: 0)
    uniq_count = 0
    left = 0

    max_mem = 0
    for right, fruit in enumerate(tree):
        max_mem = max(max_mem, sys.getsizeof(tree_count))
        tree_count[fruit] += 1
        uniq_count = len([v for v in tree_count.values() if v > 0])

        if uniq_count <= 2:
            length += 1
            max_length = max(max_length, length)
        else:
            tree_count[tree[left]] -= 1
            left += 1

    print(max_mem)
    return max_length

def totalFruit_with_delete(tree: 'List[int]') -> 'int':
    length, max_length = 0, 0
    tree_count = defaultdict(lambda: 0)
    uniq_count = 0
    left = 0

    max_mem = 0
    for right, fruit in enumerate(tree):
        max_mem = max(max_mem, sys.getsizeof(tree_count))
        print(sys.getsizeof(tree_count))
        tree_count[fruit] += 1
        uniq_count = len([v for v in tree_count.values() if v > 0])

        if uniq_count <= 2:
            length += 1
            max_length = max(max_length, length)
        else:
            tree_count[tree[left]] -= 1
            if tree_count[tree[left]] == 0:
                del tree_count[tree[left]]
            left += 1
    print(max_mem)
    return max_length

import timeit
print(timeit.timeit("totalFruit(long_test_list)", number=5, setup="from __main__ import totalFruit, long_test_list"))
print(timeit.timeit("totalFruit_2(long_test_list)", number=5, setup="from __main__ import totalFruit_2, long_test_list"))











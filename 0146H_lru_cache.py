class LRUCache:
    def __init__(self, capacity: 'int'):
        self.cache = collections.OrderedDict()
        self.max_count = capacity

    def get(self, key: 'int') -> 'int':
        ret = -1
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            ret = val
        return ret


    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.cache:
            del self.cache[key]

        if len(self.cache) == self.max_count:
            self.cache.popitem(last=False)

        self.cache[key] = value


class Node:
    def __init__(self, key, value, pre = None, nxt = None):
        self.k = key
        self.v = value
        self.pre = pre
        self.nxt = nxt


class lru_cache:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.data = {}
        self.head = None

    def set(self, key, value):
        node = Node(key, value)
        if key in self.data:
            print("set", key, value)
            self.pop_key(key)
            self.add_key(node)
            return

        if self.size == self.maxsize:
            self.pop_key()
        self.add_key(node)


    def get(self, key):
        v = self.data.get(key, None)
        if v == None:
            return -1
        else:
            self.pop_key(key)
            self.add_key(Node(key, v))
            return v

    # 用来删除一个节点或者删除首节点
    def pop_key(self, key = None):
        if key == None:
            cur = self.head
            while cur.nxt.nxt:
                cur = cur.nxt
            cur.nxt = None
        else:
            cur = self.head
            while cur.nxt:
                if cur.nxt.k == key:
                    break
                cur = cur.nxt
            if cur.nxt.nxt == None:
                cur.nxt = None
            else:
                cur.nxt = cur.nxt.nxt
            del self.data[key]
        self.size -= 1

    def add_key(self, node):
        if self.head == None:
            self.head = node
            self.size += 1
            return
        cur = self.head
        self.head = node
        self.head.nxt = cur
        self.data[node.k] = node.v
        self.size += 1


    def pprint(self):
        cur = self.head
        r = []
        while cur != None:
            r.append(cur.v)
            cur = cur.nxt
        print("->".join([str(i) for i in r]))

if __name__ == "__main__":
    lru = lru_cache(3)
    lru.set(1, 1)
    lru.set(2, 2)
    lru.set(3, 3)
    lru.set(4, 4)
    lru.pprint()
    print("get 4: ", lru.get(2))
    lru.pprint()

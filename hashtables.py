"""This is Lab 8 where we cover hash tables
and three collision resolution strategies
Course: CPE 202
Quarter: Spring 2020
Author: Drew Soderquist"""

from node import Node  # Node


class HashTableSepchain:
    """HashTableSepchain is one of
        - None, or
        - list of nodes of Item Objects, HashTableSepchain(Item(key, val), nxt)
    Attributes:
        table_size(int): size of the hash table
        table(list): list of nodes of Item Objects
        num_collisions(int): number of collisions when creating the hash table
        num_items(int): number of items in the hash table
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.table = [None] * table_size
        self.num_collisions = 0
        self.num_items = 0

    def __repr__(self):
        return f"HashTableSepChain(table: {self.table}, size: {self.table_size}" \
               f", # of collisions: {self.num_collisions}, # of items: {self.num_items})"

    def __eq__(self, other):
        return (self.table == other.table and self.num_items == other.num_items
                and self.num_collisions == other.num_collisions
                and self.table_size == other.table_size)

    def resize(self):
        """resizes an array if the load factor becomes too large
        Args:
            N/A
        Returns:
            N/A, updates the table
        """
        num_items = self.num_items
        new_size = 2 * self.table_size + 1
        new_table = [None] * new_size
        self.table_size = new_size
        table = self.table
        print("old table", self.table)
        self.table = new_table
        for node in table:
            while node is not None:
                #node = item
                #while node:
                self.put(node.val.key, node.val.val)
                node = node.nxt
        # self.table = new_table
        self.num_items = num_items
        return  # is this return needed?

    def put(self, key, data):
        """inserts a key-value pair into the hash table
        Args:
            key(str): the key of the item being inserted
            data(any): the payload
        Returns:
            N/A, updates the hash table
        """
        self.num_items += 1
        if self.load_factor() >= 1.5:  # threshold <= 1
            self.resize()
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        i = hash_num  # % size
        new_node = Node(Item(key, data))
        if self.table[i] is None:
            self.table[i] = new_node
            return
        else:
            old_head = self.table[i]
            new_node.nxt = old_head
            self.table[i] = new_node
            self.table[i] = new_node
            self.num_collisions += 1
            return



        #for idx, value in enumerate(self.table):
         #   if value is None and idx == i:
        #        self.table[i] = new_node
        #        return
         #   if value is not None and idx == i:
        #        old_head = self.table[i]
         #       new_node.nxt = old_head
        #        self.table[i] = new_node
        #        return
        #    self.num_collisions += 1


        #node = self.table[i]
        #if node is None:  # empty index
        #    self.table[i] = Node(Item(key, data), None)
        #    return
        #while self.table[i] is not None and key != self.table[i].val.key:
        #top = self.table[i]
        #new_node = Node(Item(key, data), top)
        #new_node.nxt = top
        #self.table[i] = new_node

        #node = Node(Item(key, data), top)
        #node.


        #while node.nxt is not None:
        #    if key == node.val.key:
        #        node.val.data = data
        #        self.num_collisions += 1
        #        self.num_items -= 1
        #        return
       #     node = node.nxt
        #if node.nxt is None:
        #node.nxt = Node(Item(key, data), None)
        #else:  # val.key == key
        #    node.val.data = data

    def get(self, key):
        """returns value of a key
        Args:
            key(str): the key of the item
        Returns:
            any: the payload at the specified key
        Raises:
            KeyError: raises KeyError when the key does not exist in the hash table
        """
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        i = hash_num % size
        # assuming that the load factor < 1 is always True
        node = self.table[i]
        while node is not None and key != node.val.key:
            # i = (i + 1) % size
            node = node.nxt
        if node is not None and key == node.val.key:
            #print("here")
            #print(node)
            #print(node.val.val)
            return node.val.val
        raise KeyError

    def contains(self, key):
        """sees if a key exists in the hash
        Args:
            key(str): the key of the item
        Returns:
            bool: True if exists, False if not
        """
        try:
            val = self.get(key)
            return True
        except:
            return False

    def remove(self, key):
        """removes a key-value pair from the hash table
        Args:
            key(str): key of key-value pair you wish to delete
        Returns:
            Item: the key-value pair
        Raises:
            KeyError: raises KeyError if key does not exist in the hash table
        """
        i = (hash_string(key, self.table_size)) # % self.table_size
        node = self.table[i]
        if self.contains(key) is False:
            raise KeyError
        # print("item ", item)
        if node is None:
            raise KeyError
        self.num_items -= 1
        if self.table[i].val.key == key:  # self.table[i].nxt is None:  # no child
            # print("nxt None ", item.nxt)
            temp = self.table[i]
            self.table[i] = self.table[i].nxt
            return temp
        else:
            print("else")
            #while node.nxt is not None and node.nxt.val.key != key:
            while node is not None and node.nxt.val.key != key:
            # while item is not None and item.nxt.key != key:
                # i = (i + 1) % self.table_size
                node = node.nxt
            temp = node.nxt
            node.nxt = node.nxt.nxt
        return temp
            #print("broke")
            #if node.nxt is not None and node.nxt.val.key == key:
            #    #print("nxt None")
            #    #node = None
            #    print("key equal")
            #    node = node.nxt
            #    # node.nxt = None  # node.nxt.nxt
            #else:  # node.nxt.val.key == key:
            #    print("nxt None")
            #    node = None
        #return temp

        # i = hash_string(key, self.table_size)
        #if self.table[i] is None:
        #    raise KeyError
        #item = self.table[i]
        #if self.table[i].key == key:
        #    temp = self.table[i]
        #    self.table[i] = self.table[i].next
        #else:
        #    while item.next.key != key:
        #        item = item.next
        #    temp = item.next
        #    item.next = item.next.next
        #return temp

    def size(self):
        """returns number of items in the hash table
        Args:
            N/A
        Returns:
            int: number of items
        """
        return self.num_items

    def load_factor(self):
        """returns current load factor of the hash table, max 1.5
        Args:
            N/A
        Returns:
            float: load factor of the hash table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """returns number of collisions that have occurred in the hash table
        Args:
            N/A
        Returns:
            int: number of collisions
        """
        return self.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)


class HashTableLinear:
    """HashTableLinear is one of
            - None, or
            - list of Item objects, HashTableLinear(Item(data, val))
        Attributes:
            table_size(int): size of the hash table
            table(list): list of Item Objects
            num_collisions(int): number of collisions when creating the hash table
            num_items(int): number of items in the hash table
        """

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.table = [None] * table_size
        self.num_collisions = 0
        self.num_items = 0

    def __repr__(self):
        return f"HashTableLinear(table: {self.table}, size: {self.table_size}" \
               f", # of collisions: {self.num_collisions}, # of items: {self.num_items})"

    def __eq__(self, other):
        return (self.table == other.table and self.num_items == other.num_items
                and self.num_collisions == other.num_collisions
                and self.table_size == other.table_size)

    def resize(self):
        """resizes an array if the load factor becomes too large
        Args:
            N/A
        Returns:
            N/A, updates the table
        """
        num_items = self.num_items
        new_size = 2 * self.table_size + 1
        new_table = [None] * new_size
        self.table_size = new_size
        # print("size", self.table_size)
        table = self.table
        self.table = new_table
        # print("empty ", self.table)
        for item in table:
            if item is not None:
                node = item
                #while node:
                self.put(node.key, node.val)
                # node = node.next
        self.table = new_table
        self.num_items = num_items
        return  # is this return needed?

    def put(self, key, data):
        """inserts a key-value pair into the hash table
        Args:
            key(str): the key of the item being inserted
            data(any): the payload
        Returns:
            N/A, updates the hash table
        """
        self.num_items += 1
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        if self.load_factor() >= 0.75:  # threshold <= 1
            # print("resized")
            num_items = self.num_items
            self.resize()
            self.num_items = num_items
        i = hash_num % size
        # print("put i", i)
        while self.table[i] is not None and key != self.table[i].key:
            i = (i + 1) % size
        if self.table[i] is None:
            self.table[i] = Item(key, data)
        else:
            self.table[i].val = data
            self.num_collisions += 1

    def get(self, key):
        """returns value of a key
        Args:
            key(str): the key of the item
        Returns:
            any: the payload at the specified key
        Raises:
            KeyError: raises KeyError when the key does not exist in the hash table
        """
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        i = hash_num % size
        # assuming that the load factor < 1 is always True
        while self.table[i] is not None and key != self.table[i].key:
            i = (i + 1) % size
        if self.table[i] is not None and key == self.table[i].key:
            return self.table[i].val
        raise KeyError

    def contains(self, key):
        """sees if a key exists in the hash
        Args:
            key(str): the key of the item
        Returns:
            bool: True if exists, False if not
        """
        try:
            val = self.get(key)
            return True
        except:
            return False

    def remove(self, key):
        """removes a key-value pair from the hash table
        Args:
            key(str): key of key-value pair you wish to delete
        Returns:
            Item: the key-value pair
        Raises:
            KeyError: raises KeyError if key does not exist in the hash table
        """
        i = hash_string(key, self.table_size)
        num_items = self.num_items
        # print(i)
        # print(self.table[i])
        while self.table[i] is not None and self.table[i].key != key:
            i = (i + 1) % self.table_size
        if self.table[i] is None:
            raise KeyError
        else:  # if self.table[i].key == key:
            temp = self.table[i]
            self.table[i] = None  # Item(None, None)
            i = (i + 1) % self.table_size
            while self.table[i] is not None:
                self.put(self.table[i].key, self.table[i].val)
                i = (i + 1) % self.table_size
        self.num_items = num_items - 1
        return temp

        #i = hash_string(key, self.table_size)
        #if self.table[i] is None:
        #    raise KeyError
        #item = self.table[i]
        #self.table[i] = Item(None, None)
        #i = (i + 1) % self.table_size
        #while self.table[i] is not None:
        #    self.put(i.key, i.data)
        #    i = (i + 1) % self.table_size
        #self.num_items -= 1
        #return item


        # self.table[i] = Item(None, None)
        # i = (i + 1) % self.table_size
        # while self.table[i] is not None:
        #    self.put(i.key, i.data)
        #    i = (i + 1) % self.table_size
        # self.num_items -= 1
        # return temp

    def size(self):
        """returns number of items in the hash table
        Args:
            N/A
        Returns:
            int: number of items
        """
        return self.num_items

    def load_factor(self):
        """returns current load factor of the hash table, max 0.75
        Args:
            N/A
        Returns:
            float: load factor of the hash table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """returns number of collisions that have occurred in the hash table
        Args:
            N/A
        Returns:
            int: number of collisions
        """
        return self.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def keys(self):
        """gets list of keys in the hash table
        Args:
            N/A
        Returns:
            list: list of the keys in the hash table
        """
        keys = []
        for i in self.table:
            if i is not None:
                keys.append(i.key)
        return keys


class HashTableQuadratic:
    """HashTableQuadratic is one of
            - None, or
            - list of Item objects, HashTableQuadratic(Item(data, val))
        Attributes:
            table_size(int): size of the hash table
            table(list): list of Item Objects
            num_collisions(int): number of collisions when creating the hash table
            num_items(int): number of items in the hash table
            deleted(Dummy): dummy object to mark indexes of deletion
        """

    def __init__(self, table_size=16):
        self.table_size = table_size
        self.table = [None] * table_size
        self.num_collisions = 0
        self.num_items = 0
        self.deleted = Item(Dummy(), Dummy())  # market

    def __repr__(self):
        return f"HashTableSepChain(table: {self.table}, size: {self.table_size}" \
               f", # of collisions: {self.num_collisions}, # of items: {self.num_items})"

    def __eq__(self, other):
        return (self.table == other.table and self.num_items == other.num_items
                and self.num_collisions == other.num_collisions
                and self.table_size == other.table_size)

    def resize(self):
        """resizes an array if the load factor becomes too large
        Args:
            N/A
        Returns:
            N/A, updates the table
        """
        num_items = self.num_items
        new_size = 2 * self.table_size
        new_table = [None] * new_size
        self.table_size = new_size
        #print("size", self.table_size)
        table = self.table
        self.table = new_table
        #print("empty ", self.table)
        for item in table:
            if item is not None:
                node = item
                # while node:
                self.put(node.key, node.val)
                # node = node.next
        # self.table = new_table
        self.num_items = num_items
        return  # is this return needed?

        # num_items = self.num_items
        #new_size = 2 * self.table_size + 1
        #new_table = [None] * new_size
        #self.table_size = new_size
        #table = self.table
        #self.table = new_table
        #for item in table:
        #    if item is not None:
        #        node = item
        #        while node:
        #            self.put(node.key, node.val)
        #            node = node.next
        #self.table = new_table
        # self.num_items = num_items
        #return  # is this return needed?

    def put(self, key, data):
        """inserts a key-value pair into the hash table
        Args:
            key(str): the key of the item being inserted
            data(any): the payload
        Returns:
            N/A, updates the hash table
        """
        self.num_items += 1
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        if self.load_factor() >= 0.75:  # threshold <= 1
            num_items = self.num_items
            self.resize()
            self.num_items = num_items
            # print("new table", self.table)
        i = hash_num % size
        new_hash = i
        idx = 1
        # print("put i", i)
        # print("item", self.table[i])
        while self.table[new_hash] is not None and key != self.table[new_hash].key \
                and self.table[new_hash] is not self.deleted:
            # print(self.table[new_hash])
            # print("value", i)
            new_hash = (i + ((idx + (idx ^ 2)) // 2)) % self.table_size
            idx += 1
            #i = ((i + idx ^ 2) // 2) % self.table_size
        if self.table[i] is None or self.table[i] is self.deleted:
            self.table[i] = Item(key, data)
        else:
            self.table[i].val = data
            self.num_collisions += 1

    def get(self, key):
        """returns value of a key
        Args:
            key(str): the key of the item
        Returns:
            any: the payload at the specified key
        Raises:
            KeyError: raises KeyError when the key does not exist in the hash table
        """
        size, hash_num = self.table_size, hash_string(key, self.table_size)
        i = hash_num % size
        # assuming that the load factor < 1 is always True
        new_hash = i
        idx = 1
        while self.table[new_hash] is not None and key != self.table[new_hash].key:
            new_hash = i + ((idx + idx ^ 2) // 2) % self.table_size
            idx += 1
        if self.table[i] is not None and key == self.table[i].key:
            return self.table[i].val
        raise KeyError

    def contains(self, key):
        """sees if a key exists in the hash
        Args:
            key(str): the key of the item
        Returns:
            bool: True if exists, False if not
        """
        try:
            val = self.get(key)
            return True
        except:
            return False

    def remove(self, key):
        """removes a key-value pair from the hash table
        Args:
            key(str): key of key-value pair you wish to delete
        Returns:
            Item: the key-value pair
        Raises:
            KeyError: raises KeyError if key does not exist in the hash table
        """
        num_items = self.num_items
        i = hash_string(key, self.table_size)
        while self.table[i] is not None and self.table[i].key != key:
            i = ((i + (i ^ 2)) // 2) % self.table_size
        if self.table[i] is None or self.table[i] is self.deleted:  # == self.deleted?
            raise KeyError
        else:  # if self.table[i].key == key:
            temp = self.table[i]
            self.table[i] = self.deleted
        self.num_items = num_items - 1
        return temp

        #i = hash_string(key, self.table_size)
        #if self.table[i] is None or self.table[i] is self.deleted:  # == self.deleted?
        #    raise KeyError
        #item = self.table[i]
        #self.table[i] = self.deleted  # Dummy()  # Item(None, None)
        #i = ((i + (i ^ 2)) / 2) % self.table_size  # might need to check
        #while self.table[i] is not None:
        #    self.put(i.key, i.data)
        #    i = ((i + i ^ 2) / 2) % self.table_size
        #self.num_items -= 1
        #return item

    def size(self):
        """returns number of items in the hash table
        Args:
            N/A
        Returns:
            int: number of items
        """
        return self.num_items

    def load_factor(self):
        """returns current load factor of the hash table, max 0.75
        Args:
            N/A
        Returns:
            float: load factor of the hash table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """returns number of collisions that have occurred in the hash table
        Args:
            N/A
        Returns:
            int: number of collisions
        """
        return self.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)


class Item:
    """items store in the table: Key-Value pair
    Attributes:
        key(str): the key
        val(any): the value
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return f"Item(key: {self.key}, val: {self.val})"

    def __eq__(self, other):
        return self.key == other.key and self.val == other.val


class Dummy:
    """Dummy object used as a special marker
    """
    def __init__(self):
        pass


def hash_string(string, size):
    """computes the hash value of a string
    Args:
        string(str): the word (payload) you want to insert into the hash table
        size(int): size of the hash table
    Returns:
        int: hash value
    """
    hash1 = 0
    for c in string:
        # print("c", c)
        hash1 = (hash1 * 31 + ord(c)) % size
    return hash1


def import_stopwords(filename, hashtable):
    """imports a file and creates a hashtable of stop words
    Args:
        filename(file): input text file
        hashtable(hashtable): list of nodes of Item objects, or list of Item objects
    Returns:
        list: the hashtable
    """
    file1 = open(filename, "r")
    lines = file1.readlines()
    file1.close()
    for i in lines:
        i = i.strip()
        words = i.split()
        for single in words:
            hashtable.put(single, 0)
    return hashtable

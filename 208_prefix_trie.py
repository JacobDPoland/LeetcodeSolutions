class Trie(object):

    def __init__(self, value=""):
        self.val = value
        self.left = None
        self.right = None

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        O(n) = log(n)
        """
        if word <= self.val:  # word belongs to the left
            if self.left == None:
                self.left = Trie(word)
            else:
                self.left.insert(word)
        else:                 # word belongs to the right
            if self.right == None:
                self.right = Trie(word)
            else:
                self.right.insert(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        O(n) = log(n)
        """
        if self.val == None:
            return False
        elif self.val == word:
            return True
        elif word < self.val:   # word is to the left or isn't there at all
            if self.left == None:
                return False
            else:
                return self.left.search(word)
        else:                   # word is to the right or isn't there at all
            if self.right == None:
                return False
            else:
                return self.right.search(word)
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        O(n) = log(n)
        same as search function but with string slicing
        """
        if self.val == None:
            return False
        elif self.val[:len(prefix)] == prefix:
            return True
        elif prefix < self.val:
            if self.left == None:
                return False
            else:
                return self.left.startsWith(prefix)
        else:
            if self.right == None:
                return False
            else:
                return self.right.startsWith(prefix)
        


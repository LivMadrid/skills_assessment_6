"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children or []

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)

    def to_find(self,data): 
        ## added this here because it kept saying Tree class has no
        #data attribute. As the question is similar to the hermione 
        #one in class and nodes themselves are trees. it delegates 
        #methods to both tree class itself and node class so you can 
        #search on both levels 
        #pop(o) makes it A BFS search so a hiearchy search. 

        to_find = [self]

        while to_find:
            current = to_find.pop(0)

            if current.data == data:
                return current

            to_find.extend(current.children)



class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def get_nodes(self, data):
        """ Return a list of nodes with the given data

        For example::

            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> e = Node("E")
            >>> c = Node("C", [ b1, e])
            >>> a = Node("A", [b2, c])
            >>> tree = Tree(a)
            >>> result = tree.get_nodes("B")
            >>> result == [b2, b1]
            True
            >>> tree.get_nodes("L")
            []

        """

        return self.root.to_find(data)

      #starts at root then goes through the nodes. 
      #>>> c = Node('C' [b1, e])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: string indices must be integers ??????

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()

class Node:

    def __init__(self, data = -1, left = None, right = None):

        self.data = data

        self.left = left

        self.right = right

    def get_data(self):

        return self.data

    def set_data(self, new_data):

        self.data = new_data

    def get_left(self):

        return self.left

    def set_left(self, new_left):

        self.left = new_left

    def get_right(self):

        return self.right

    def set_right(self, new_right):

        self.right = new_right

class BST:

    def __init__(self, root = None, node_cnt = 0):

        self.root = root

        self.node_cnt = node_cnt
##        总结点数

    def isEmpty(self):

        return self.node_cnt == 0

    def findV1(self, item, bst_base):

        if bst_base == None:

            return None

        if item > bst_base.get_data():

            return self.find(bst_base.get_right(), item)

        elif item < bst_base.get_data():

            return self.find(bst_base.get_left(), item)

        else:

            return bst_base

    def findV2(self, item):

##        if bst_base == None:
##
##            return None

        found = False

        bst_base = self.root

        while not found and bst_base != None:

            if item > bst_base.get_data():

                bst_base = bst_base.get_right()

            elif item < bst_base.get_data():

                bst_base = bst_base.get_left()

            else:

                found = True

                break

        return bst_base

    def find_min(self, bst_base):

        while bst_base.get_left() != None:

            bst_base = bst_base.get_left()

        return bst_base.get_data()

    def find_max(self, bst_base):

        while bst_base.get_right() != None:

            bst_base = bst_base.get_right()

        return bst_base.get_data()

    def insert(self, item, tree_base):

        if tree_base == None:

            tree_base = Node(item)

        else:

            if item < tree_base.get_data():

                tree_base.set_left(self.insert(item, tree_base.get_left()))

            elif item > tree_base.get_data():

                tree_base.set_right(self.insert(item, tree_base.get_right()))

        return tree_base

    def delete(self, item, tree_base):

        if tree_base == None:

            print('It is not founded!')

        else:

            if item < tree_base.get_data():

                tree_base.set_left(self.delete(item, tree_base.get_left()))

            elif item > tree_base.get_data():

                tree_base.set_right(self.delete(item, tree_base.get_right()))

            else:

                if  tree_base.get_left() != None and tree_base.get_right() != None:

                    p = self.find_min(tree_base.get_right())

                    tree_base.set_data(p.get_data())

                    tree_base.set_right(self.delete(tree_base.get_data(), tree_base.get_right()))

                else:

                    p = tree_base

                    if tree_base.get_left() == None:

                        tree_base = tree_base.get_right()

                    else:

                        tree_base = tree_base.get_left()

                    del p

        return tree_base

##

##
                
def test():

    a = Node(5)

    b = Node(8)

    c = Node(6, a)

    d = Node(9, b)

    z = Node(7, c, d)

    tree = BST(z, 5)

    print(tree.find_min(tree.root))

    print(tree.find_max(tree.root))

    tree.insert(10, tree.root)

    print(tree.find_max(tree.root))

    tree.delete(10, tree.root)

    print(tree.find_max(tree.root))

test()

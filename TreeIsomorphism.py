class Node:
    def __init__(self, label=None):
        self.label = label
        self.left = None
        self.right = None

def isIsomorphic(tree1, tree2):
    """Checks if two rooted binary trees (of type Node) are isomorphic."""

    # Both roots are empty: trees isomorphic by def
    if tree1 == None and tree2 == None:
        return True
    # Exactly one empty: trees can not be isomorphic
    elif tree1 == None or tree2 == None:
        return False
    
    if tree1.label != tree2.label:
        return False
    
    isNonFlippedIsomorphic = (isIsomorphic(tree1.left,tree2.left) and
                              isIsomorphic(tree1.right,tree2.right))
    isFlippedIsomorphic = (isIsomorphic(tree1.left,tree2.right) and
                           isIsomorphic(tree1.left,tree2.right))

    return isNonFlippedIsomorphic or isFlippedIsomorphic

def string2tree(s):
    """Converts a rooted binary tree in string representation to a linked tree
       data structure of type Node
    """
    
    if s[0] != '(': # we have a leaf
        return Node(s)

    i = 0
    for pos, char in enumerate(s):
        if char == "(":
           i += 1
        if char == ")":
           i -= 1
        if char == "," and i == 1:
           s_left = s[1:pos]
           s_right = s[pos+1:-1]
    t = Node()
    if len(s_left) > 0:
        t.left = string2tree(s_left)
    if len(s_right) > 0:
        t.right = string2tree(s_right)
    return t



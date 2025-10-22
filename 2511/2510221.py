class Tree:
    def __init__(self,label,branch=None):
        self.label = label
        if branch != None:
            self.branch = branch
        else:
            self.branch = []
        for t in self.branch:
           assert isinstance(t,Tree)

def delete_tree(branch,tree):
    t = []
    for i in tree.branch:
        if i != branch:
            t.append(i)
    return Tree(tree.label,branch = t)


def cut_tree(n,tree):
    if tree.branch == []:
        return tree
    else:
        for i in tree.branch:
            if i.label == n:
                tree = delete_tree(i,tree)
        return Tree(tree.label,[cut_tree(n,i) for i in tree.branch])

def print_tree(tree):
    blank = '    '
    if tree.branch == []:
        print(tree.label)
    else:
        print(tree.label,'\n')
        for i in tree.branch:
            print_tree(i)

a = Tree(3,[Tree(1),Tree(9)])
print_tree(cut_tree(1,a))

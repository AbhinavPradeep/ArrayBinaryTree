from Tree import BinaryTree

Tree = BinaryTree()

Tree.Insert(10)

Tree.Insert(12)

Tree.Insert(8)

Tree.Insert(16)

Tree.Insert(14)

Tree.Insert(5)

Tree.Insert(6)

Tree.Insert(7)

Tree.Insert(3)

Tree.Insert(10)

Tree.Insert(11)

Tree.Insert(10.5)

print(Tree.Tree)
print(Tree.NumberOfNodes)

print(Tree.Search(11))

Tree.Delete(16)
print(Tree.Tree)


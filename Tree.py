from Node import Node
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

class BinaryTree:
    def __init__(self) -> None:
        self.Tree = np.empty(1, dtype=Node)
        self.NumberOfNodes = 0
    
    def Insert(self,ValueToInsert) -> None:
        self.NumberOfNodes += 1
        # NewTree = np.empty(sum([2**n for n in range(0,self.NumberOfNodes)]), dtype=Node)
        # for i,j in np.ndenumerate(self.Tree):
        #     NewTree[i] = j
        # self.Tree = NewTree
        if self.Tree[0] == None:
            self.Tree[0] = Node(ValueToInsert)
        else:
            CurrentNode = self.Tree[0]
            Inserted = False
            Index = 0
            while Inserted == False:
                if ValueToInsert > CurrentNode.Value and len(self.Tree) <= (2*Index)+2:
                    NewTree = np.empty(2*len(self.Tree)+1, dtype=Node)
                    for i,j in np.ndenumerate(self.Tree):
                         NewTree[i] = j
                    self.Tree = NewTree
                    self.Tree[(2*Index)+2] = Node(ValueToInsert)
                    Inserted  = True
                elif ValueToInsert <= CurrentNode.Value and len(self.Tree) <= (2*Index)+1:
                    NewTree = np.empty(2*len(self.Tree)+1, dtype=Node)
                    for i,j in np.ndenumerate(self.Tree):
                         NewTree[i] = j
                    self.Tree = NewTree
                    self.Tree[(2*Index)+1] = Node(ValueToInsert)
                    Inserted = True
                elif ValueToInsert > CurrentNode.Value and self.Tree[(2*Index)+2] == None:
                    self.Tree[(2*Index)+2] = Node(ValueToInsert)
                    Inserted  = True
                elif ValueToInsert <= CurrentNode.Value and self.Tree[(2*Index)+1] == None:
                    self.Tree[(2*Index)+1] = Node(ValueToInsert)
                    Inserted = True
                elif ValueToInsert > CurrentNode.Value and self.Tree[(2*Index)+2] != None:
                    CurrentNode = self.Tree[(2*Index)+2]
                    Index = ((2*Index)+2)
                elif ValueToInsert <= CurrentNode.Value and self.Tree[(2*Index)+1] != None:
                    CurrentNode = self.Tree[(2*Index)+1]
                    Index = ((2*Index)+1)
    
    def Search(self,ValueToBeFound) -> Node|None:
        if self.Tree[0] == None:
            return None
        else:
            CurrentNode = self.Tree[0]
            EndReached = False
            ReturnNode = None
            Index = 0
            while EndReached == False:
                if CurrentNode.Value == ValueToBeFound:
                    ReturnNode = CurrentNode
                    EndReached = True
                elif CurrentNode.Value != ValueToBeFound and len(self.Tree) <= (2*Index)+1:
                    EndReached = False
                elif ValueToBeFound > CurrentNode.Value and self.Tree[(2*Index)+2] != None:
                    CurrentNode = self.Tree[(2*Index)+2]
                    Index = ((2*Index)+2)
                elif ValueToBeFound < CurrentNode.Value and self.Tree[(2*Index)+1] != None:
                    CurrentNode = self.Tree[(2*Index)+1]
                    Index = ((2*Index)+1)
                elif (ValueToBeFound > CurrentNode.Value and self.Tree[(2*Index)+2] == None) or (ValueToBeFound < CurrentNode.Value and self.Tree[(2*Index)+1] == None):
                    EndReached = True
            return ReturnNode
        
    def Delete(self,ValueToBeDeleted) -> None:
        if self.Tree[0] == None:
            return None
        else:
            CurrentNode = self.Tree[0]
            EndReached = False
            Index = 0
            while EndReached == False:
                if CurrentNode.Value == ValueToBeDeleted:
                    self.Tree[Index] = None
                    EndReached = True
                    # if len(self.Tree) <= (2*Index)+1:
                    #     self.Tree[Index] = None
                    # elif self.Tree[(2*Index)+1] == None:
                    #     pass
                    # else:
                    #     IndexToReplace = Index 
                    #     Index = (2*Index)+1
                    #     while len(self.Tree) >= (2*Index)+3 and self.Tree[(2*Index)+2] != None:
                    #         Index = (2*Index)+2
                    #         CurrentNode = self.Tree[Index]
                    #     self.Tree[IndexToReplace] = CurrentNode
                    # EndReached = True
                elif CurrentNode.Value != ValueToBeDeleted and len(self.Tree) <= (2*Index)+1:
                    EndReached = False
                elif ValueToBeDeleted > CurrentNode.Value and self.Tree[(2*Index)+2] != None:
                    CurrentNode = self.Tree[(2*Index)+2]
                    Index = ((2*Index)+2)
                elif ValueToBeDeleted < CurrentNode.Value and self.Tree[(2*Index)+1] != None:
                    CurrentNode = self.Tree[(2*Index)+1]
                    Index = ((2*Index)+1)
                elif (ValueToBeDeleted > CurrentNode.Value and self.Tree[(2*Index)+2] == None) or (ValueToBeDeleted < CurrentNode.Value and self.Tree[(2*Index)+1] == None):
                    EndReached = True
                # if CurrentNode.Value != ValueToBeDeleted and len(self.Tree) <= (2*Index)+1:
                #     EndReached = True
                # elif self.Tree[(2*Index)+2] != None and ValueToBeDeleted > CurrentNode.RightNode.Value:
                #     CurrentNode = self.Tree[(2*Index)+2]
                #     Index = (2*Index)+2
                # elif self.Tree[(2*Index)+1] != None and ValueToBeDeleted < CurrentNode.LeftNode.Value:
                #     CurrentNode = self.Tree[(2*Index)+1]
                #     Index = (2*Index)+1
                # elif self.Tree[(2*Index)+1] == None and ValueToBeDeleted > CurrentNode.Value:
                #     CurrentNode = self.Tree[(2*Index)+2]
                #     Index = (2*Index)+2
                # elif self.Tree[(2*Index)+2] == None and ValueToBeDeleted < CurrentNode.Value:
                #     CurrentNode = self.Tree[(2*Index)+1]
                #     Index = (2*Index)+1
                # elif (ValueToBeDeleted > CurrentNode.Value and self.Tree[(2*Index)+2] == None) or (ValueToBeDeleted < CurrentNode.Value and self.Tree[(2*Index)+1] == None):
                #     EndReached = True
                # if CurrentNode.Value == ValueToBeDeleted:
                #     self.Tree[Index] = None
                
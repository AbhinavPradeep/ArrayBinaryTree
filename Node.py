class Node:
    def __init__(self,Value) -> None:
        self.Value = Value
    
    def __str__(self) -> str:
        return str(self.Value)
    
    __repr__ = __str__
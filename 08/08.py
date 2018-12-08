import sys

class MetaNode:
    def __init__(self, numChildren, numMetas):
        self.numChildren = numChildren
        self.numMetas = numMetas
        self.unprocessedChildren = numChildren
        self.children = []
        self.metadata = []

    def GetMetaTotal(self):
        value = sum(self.metadata)
        for child in self.children:
            value += child.GetMetaTotal()
        return value

    def GetValue(self):
        if (self.numChildren == 0):
            return sum(self.metadata)
        childValues = 0

        for mIndex in self.metadata:
            childIndex = mIndex - 1
            if (childIndex >= 0 and childIndex < self.numChildren):
                childValues += self.children[childIndex].GetValue()
        return childValues

    def AddChild(self, child):
        self.children.append(child)
        self.unprocessedChildren -= 1

    def HasUnproccessedChildren(self):
        return self.unprocessedChildren > 0

    def AddMetadata(self, metaList):
        self.metadata = metaList

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\08\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

inputs = []
for seg in lines[0].split(' '):
    inputs.append(int(seg))

nodeStack = []
i = 0
total = 0
value = 0
while (i < len(inputs)):
    if (len(nodeStack) > 0):
        if (not nodeStack[-1].HasUnproccessedChildren()):
            child = nodeStack.pop()
            child.AddMetadata(inputs[i: i+child.numMetas])
            i += child.numMetas
            if (len(nodeStack) == 0): #done, this is the root
                total = child.GetMetaTotal()
                value = child.GetValue()
            else:
                nodeStack[-1].AddChild(child)
            continue

    newNode = MetaNode(inputs[i], inputs[i+1])
    # Has children - push to stack
    if newNode.numChildren > 0:
        nodeStack.append(newNode)
        i += 2
    # Has no children - append metadata, assign to parent, traverse siblings
    else:
        newNode.AddMetadata(inputs[i+2: i+2+newNode.numMetas])
        lastNode = nodeStack[-1]
        lastNode.AddChild(newNode)
        i += 2 + newNode.numMetas

print(total)
print(value)
# Project: advent_of_code
# File: day_8
# Author: Joinemm
# Date created: 08/12/18
# Python Version: 3.6.6

data = []
with open("input_8.txt", "r") as input:
    for x in input.read().split(" "):
        data.append(int(x))

metadata = []
nodes = []


class Node:

    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata
        self.value = None

    def setvalue(self, value):
        self.value = value


def parse(data):
    try:
        kids = data[0]
        metas = data[1]
        thismeta = []
        children = []
        newdata = data[2:]
        for i in range(kids):
            newdata, kid = parse(newdata)
            children.append(kid)
        for x in range(metas):
            metadata.append(newdata[x])
            thismeta.append(newdata[x])
        newdata = newdata[metas:]
        thisnode = Node(children, thismeta)
        nodes.append(thisnode)
        return newdata, thisnode
    except IndexError:
        return []


while len(data) > 0:
    data, x = parse(data)

for node in nodes:
    if not node.children:
        value = sum(node.metadata)
        node.setvalue(value)
    else:
        value = 0
        for metaindex in node.metadata:
            if not metaindex == 0:
                try:
                    value += node.children[metaindex-1].value
                except IndexError:
                    value += 0
            else:
                value += 0
        node.setvalue(value)

print(sum(metadata))
print(nodes[-1].value)



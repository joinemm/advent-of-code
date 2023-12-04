from timeit import default_timer as timer

start = timer()

class Node():

    def __init__(self, orbital_map, name):
        self.name = name
        self.children = []
        self.parent = None
        orbital_map[name] = self

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def orbits(self):
        count = 0
        orbits = self
        while orbits.parent is not None:
            count += 1
            orbits = orbits.parent
        return count
    
    def connections(self):
        return self.children + [self.parent]


def generate_map():
    orbital_map = {}
    for relationship in open('input.txt', 'r'):
        parent, child = relationship.strip().split(')')
        
        parentnode = orbital_map.get(parent)
        if parentnode is None:
            parentnode = Node(orbital_map, parent)

        childnode = orbital_map.get(child)
        if childnode is None:
            childnode = Node(orbital_map, child)

        parentnode.add_child(childnode)
        childnode.set_parent(parentnode)
    return orbital_map


def part_1(orbital_map):
    total = 0
    for planet in orbital_map:
        orbits = orbital_map[planet].orbits()
        total += orbits
    print(f'{timer()-start:.4f}s', 'part 1:', total)


def santa_search(orbital_map, origin, node, distances, hops):
    if orbital_map['SAN'] in node.children:
        distances.add(hops)
    else:
        connections = node.connections()
        connections.remove(origin)
        for connection in connections:
            if connection is not None:
                santa_search(orbital_map, node, connection, distances, hops + 1)


def part_2(orbital_map):
    you = orbital_map['YOU']
    distances = set()
    santa_search(orbital_map, you, you.parent, distances, 0)
    print(f'{timer()-start:.4f}s', 'part 2:', min(distances))


def main():
    orbital_map = generate_map()
    part_1(orbital_map)
    part_2(orbital_map)


main()

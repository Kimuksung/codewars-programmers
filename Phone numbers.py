class node :
    def __init__(self , key = None) :
        self.key = key
        self.children = dict()

class Trie :
    def __init__(self) :
        self.root = node( key = None )
        print ( 'init' )

    def insert( self , values ) :
        print ( 'insert ')
        print ( values )
        current = self.root
        print ( current.children )
        for value in values :
            if value not in current.children :
                temp = node( key = value )
                current.children.append(temp)
            current = current.children[current.children.index(value)]
    
    def dfs( self ) :
        stack = []
        cnt = 0
        visited = set()
        stack.append(self.root)

        while stack :
            node = stack.pop()
            if node in visited :
                continue
            cnt += 1
            stack.extend(node.children)
        print(cnt)

def phone_number(phone_numbers):
    trie = Trie()
    trie.insert( '123' )
    trie.dfs()

phone_number('')
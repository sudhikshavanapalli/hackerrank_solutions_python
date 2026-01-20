"""abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
CODE:"""
def mutate_string(string,position,charecter):
    return string[:position]+charecter+string[position++1:]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

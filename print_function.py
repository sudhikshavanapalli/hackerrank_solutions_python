"""The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following: 123...n
code:"""
if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep='')
"""
explaination:

Without the Star (*)
When you don't use the star, Python sees the range as one single container.
The Code: print(range(1, 6))
The Result: range(1, 6)
Why? You are printing the "instruction" for the numbers, not the numbers themselves.
With the Star (*)
The star "unpacks" the container. It’s like opening a bag and pouring the contents out onto the floor.
The Code: print(*range(1, 6))
The Result: 1 2 3 4 5
"""

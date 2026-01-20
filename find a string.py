"""Output the integer number indicating the total number of occurrences of the substring in the original string.
Sample Input
ABCDCDC
CDC
Sample Output
2
code:"""
def count_substring(string, sub_string):
    count=0
    n=len(sub_string)
    for i in range(len(string)-n+1):
        if string[i:i+n]==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

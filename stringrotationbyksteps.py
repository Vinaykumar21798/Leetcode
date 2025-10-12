def rotatestring(string,k):
    k=k%len(string)
    return string[k:]+string[:k]
string=input()
k=int(input())
print(rotatestring(string,k))
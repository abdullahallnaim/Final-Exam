t = int(input())
for i in range(0,t):
    a = list(input())
    a.reverse()
    # a -->list of string
    result = " ".join(a)
    print(result)
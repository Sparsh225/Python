
def sumAll(*args):
    print(*args) # 1 ,2
    print(args) #(1,2)
    return sum(args)

print(sumAll(1,2,4,4))
print(sumAll(1,2))
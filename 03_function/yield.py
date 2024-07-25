def evenGenerator(limit):
    for i in range(2,limit+1,2):
        yield i
    
for num in evenGenerator(10):
    print(num)


def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

print(fact(5))
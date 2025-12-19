def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

# for i in reverse("Rajesh Kumar"):
#     print(i)
name = "Subodh narayan"
var = iter(name)

for i in range(1,len(name),1):
    print(next(var))

print(sum(i*i for i in range(10)) )                # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))         # dot product

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
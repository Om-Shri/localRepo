def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

# for i in reverse("Rajesh Kumar"):
#     print(i)
name = "Subodh narayan"
var = iter(name)

for i in range(1,len(name),1):
    print(next(var))

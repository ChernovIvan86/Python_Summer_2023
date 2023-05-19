lst=[[1,5,3], [2,44,1,4], [3,3], [3,33,1,4]]

x=set(map(len,lst))
print(x)

print(list(map(len,lst)))

x=str(list(map(len,lst)))
print(x)

x=lambda y: ''.join(list(map(len,y)))
print(x(lst))


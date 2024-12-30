# add_by_2 = lambda x: x + 2
# print(add_by_2(3))

# sub= lambda x: x - 3
# print(sub(6))

#lambda with map 
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x:x**2, numbers))
# print(squared)


names=['suresh','anish','sabin']

shows = list(map(lambda x:x+x ,names))
print(shows)
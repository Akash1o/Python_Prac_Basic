def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
#Yeild doesnt generate all values at once but in lazy way .


        count += 1

counter = count_up_to(4)
for num in counter:
    print(num) 


#yeild can return one at time and saves memory .
#But in normal couting it stores all the values.
#Using yeild helps in counting like billin without any storage taking and easily.
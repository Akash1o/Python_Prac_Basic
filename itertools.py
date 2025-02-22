import itertools

counts=itertools.count(2,3)
#2 define starts from 2 and increase 3 in each.

for _ in range(5):
 print(next(counts))
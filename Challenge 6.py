sum_squars = 0
squar_sums = 0

for i in range(1,101):
  sum_squars = sum_squars + (i**2)
  squar_sums = squar_sums + i

squar_sums = squar_sums**2
print(squar_sums-sum_squars)
    

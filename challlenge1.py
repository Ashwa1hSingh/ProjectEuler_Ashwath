import array as arr

sum3 = 0
sum5 = 0
i = 0
sum = 0
for i in range(0,1000,1):
    if i % 3 == 0:
        sum3 = sum3 + i
    elif i % 5 == 0:
        sum5 = sum5 + i

print("sum of multiples of 3 and 5 up till 1000 is", sum3 + sum5)





                
            
    
    
    

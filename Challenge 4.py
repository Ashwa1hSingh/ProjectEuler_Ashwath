max = 0
reverse_num = 0
digit = 0
multiply = 0
number  = 0

for i in range(0,1000,1):
    for j in range(0,1000,1): 
        temp = i*j
        multiply = i*j 
        reverse_num=0
        while(multiply>0):
            digit= multiply%10
            reverse_num= (reverse_num*10) + digit
            multiply=multiply//10
            if(temp==reverse_num):
                if temp>max:
                    max = temp
        reverse_num = 0 
print("highest palindome number is",max)


maximum = 600851475143  
divisor = 2

while maximum > divisor:
    if maximum % divisor == 0:
        maximum = maximum / divisor
    else:
        divisor = divisor +1

print(divisor)

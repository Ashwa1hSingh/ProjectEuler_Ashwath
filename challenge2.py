def evenFibSum(limit) :
    if (limit < 2) :
        return 
    fibo1 = 0
    fibo2 = 2
    sm= fibo1 + fibo2
     
    while (fibo2 <= limit) :
 
        
        fibo3 = 4 * fibo2 + fibo1
 
        if (fibp3 > limit) :
            break
 
        
        fibo1 = fibo2
        fibo2 = fibo3
        sm = sm + fibo2
     
    return sm
 
# Driver code
limit = 4000000
print(evenFibSum(limit))

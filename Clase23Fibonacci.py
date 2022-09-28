def fibonacci(x= 0):
    if x <= 2:
        return("Error")
    
    fibo = [0, 1]
    while len(fibo) < x:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo 



print(fibonacci(10))
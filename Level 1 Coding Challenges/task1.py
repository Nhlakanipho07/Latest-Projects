def multiples(integer):
    sum_of_multiples = 0
    
    for i in range(1,integer):
        if i%3 == 0 or i%5 == 0:
            sum_of_multiples += i
            
    print(sum_of_multiples)
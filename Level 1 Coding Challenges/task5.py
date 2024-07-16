def triangle(integer):
    if integer > 0:
        for i in range(1,integer+1):
            hash = "#"
            shape = hash*i
            print(shape)
    elif integer < 0:
        for i in range(integer,0):
            hash = "#"
            shape = hash*(i*-1)
            print(shape)
            



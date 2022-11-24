with open('test.txt', 'r') as x:
    count = 0
    for sentence in x:
        y = sentence
        count+=1
        if count % 2 == 0:
            print(y)
        

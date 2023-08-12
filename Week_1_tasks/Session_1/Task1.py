
LIST1 = [1,2,3,4,5,6,4,6,7,8,4]
result =0

def Frequent_occurence(list):
    counter=0
    for x in list:
        if(x==4):
            counter+=1
        
    return counter

result=Frequent_occurence(LIST1)

print(result)
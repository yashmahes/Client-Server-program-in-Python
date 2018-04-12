import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def rearrange(elements):
    elements.sort()
    
    
    
            
    
    lis = []
    
    for num in elements:
        numberOfOnes = bin(num)[2:].count('1')
        lis.append(numberOfOnes)
        
    i = 0
    
    while i < len(elements) - 1:
        j = i+1
        while j < len(elements):
            if lis[i] > lis[j]:
                t1 = lis[i]
                lis[i] = lis[j]
                lis[j] = t1
                
                t2 = elements[i]
                elements[i] = elements[j]
                elements[j] = t2
                
            if lis[i] == lis[j]:
                if elements[i] > elements[j]:
                    t1 = lis[i]
                    lis[i] = lis[j]
                    lis[j] = t1
                
                    t2 = elements[i]
                    elements[i] = elements[j]
                    elements[j] = t2
        
            j += 1
            
        i += 1
        
        
        
    
    return elements
               

"""
* DO NOT MODIFY CODE BELOW THIS POINT!
"""
def main():
    data = [5,5,3,7,10,14]
    
    elements = []

    for i in range(1, int(data[0]) + 1):
        elements.append(int(data[i]))

    result = rearrange(elements)
    
    for val in result:
        print(val)

main()

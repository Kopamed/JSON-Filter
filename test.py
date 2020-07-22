f = "'test':fdsfdsjkfhisf,"

key = "test"

def verify(f, key, i):
        
        for j in range(len(key)):
                    
            if f[i+j] != key[j]:
                
                return False
        
        return True


for i in range(len(f)):
            
    if f[i] == key[0]:
                
        if verify(f, key, i) == True:
                    
            for k in range(len(f[i+len(key)+1:])):
                
                
                if f[k+i+len(key)+1] == ",":
                    
                    start = i+len(key)+2
                    end = k+i
                    print(f[start:end])
                    break        

print(f[start:end])
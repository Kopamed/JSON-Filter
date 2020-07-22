import json


#JBB == JSON But Better
class jbb:
    
    def __init__(self):
        
        pass
    
    
    def verify(self, f, key, i):
        
        for j in range(len(key)):
                    
            if f[i+j] != key[j]:
                
                return False
        
        return True
    
    

    def insert_before(self, main, string, pos):
    
        main1 = main[:pos]
        main2 = main[pos:]
    
        string = main1 + string + main2
    
        return string


    
    def find(self, key, filename):
        
        container = {}
        
        
        with open(filename, "r") as f:
            
            f = f.read()
           
            
        for i in range(len(f)):
            
            if f[i] == key[0]:
                
                if self.verify(f, key, i) == True:
                    
                    for k in range(len(f[i+len(key)+1:])):
                
                
                if f[k+i+len(key)+1] == ",":
                    
                    start = i+len(key)+2
                    end = k+i
                    print(f[start:end])
                    break      
        
        return f[start:end] 
                        
                        
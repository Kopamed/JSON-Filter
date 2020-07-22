import json
import rd

key_list = ["items"]

class Parser:
    
    def __init__(self, og_dir, new_dir, key_list = []):
        
        self.og_dir = og_dir
        self.new_dir = new_dir
        self.key_list = key_list
    
    
    def load_json(self,file_name):
        
        with open(file_name, "r") as write_file:
            
            data = write_file.read()
            #data = json.loads(data)
        
        
        if data[0] != "{":
            with open(file_name, "w") as write_file:
                
                write_file.write("{" + data + "}")
            
            
        with open(file_name, "r") as write_file:
            
            data = write_file.read()
            data = json.loads(data)
            
        return data



    def dump_json(self,file_name, data):
        
        with open(file_name, "w") as write_file:
            
            json.dump(data, write_file)
    
    
    
    def modify_file(self, filename, new_filename="filename"):
        
        f = load_json(filename)
        
        for i in f:
            pass
        
        
parser = Parser("defaults", "modified")

print(parser.load_json("defaults/1.json"))
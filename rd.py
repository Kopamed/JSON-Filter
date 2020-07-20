from oauth2client.service_account import ServiceAccountCredentials
import gspread, random, json, time

class Database:
    
    def __init__(self, url, name, worksheet_name):
        self.url = url
        self.name = name
        self.worksheet_name = worksheet_name
        self.count = 0
        self.n=7
        
        self.gc = gspread.service_account(filename="client_secret.json")
        self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        self.gc1 = gspread.service_account(filename="client_secret1.json")
        self.sh1 = self.gc1.open_by_url(self.url).worksheet(self.worksheet_name)
    
        self.gc2 = gspread.service_account(filename="client_secret2.json")
        self.sh2 = self.gc2.open_by_url(self.url).worksheet(self.worksheet_name)
        
        self.gc3 = gspread.service_account(filename="client_secret3.json")
        self.sh3 = self.gc3.open_by_url(self.url).worksheet(self.worksheet_name)
        
        self.gc4 = gspread.service_account(filename="client_secret4.json")
        self.sh4 = self.gc4.open_by_url(self.url).worksheet(self.worksheet_name)
        
        self.gc5 = gspread.service_account(filename="client_secret5.json")
        self.sh5 = self.gc5.open_by_url(self.url).worksheet(self.worksheet_name)
        
        self.gc6 = gspread.service_account(filename="client_secret6.json")
        self.sh6 = self.gc6.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
    
    def load_json(self,file_name):
        
        with open(file_name, "r") as write_file:
            data = write_file.read()
            data = json.loads(data)
            
        return data



    def dump_json(self,file_name, data):
        
        with open(file_name, "w") as write_file:
            json.dump(data, write_file)



    def push(self, arr):
        
        y = len(self.sh.col_values(1))+1
        for i in range(len(arr)):
            
            if self.count == 0:
                self.sh.update_cell(y, i+1, arr[i])
            
            elif self.count == 1:
                self.sh1.update_cell(y, i+1, arr[i])
                
            elif self.count == 2:
                self.sh2.update_cell(y, i+1, arr[i])    
                
            elif self.count == 3:
                self.sh3.update_cell(y, i+1, arr[i])
                
            elif self.count == 4:
                self.sh4.update_cell(y, i+1, arr[i])
                
            elif self.count == 5:
                self.sh5.update_cell(y, i+1, arr[i])
                
            elif self.count == 6:
                self.sh6.update_cell(y, i+1, arr[i])
                
                
                
            if self.count == self.n-1:
                self.count = 0
            else:
                self.count += 1
                
            
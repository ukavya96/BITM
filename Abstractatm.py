from abc import ABC, abstractmethod
class Abstractatm(ABC):
    def __init__(self,Phone_num,Bank,Password):
        self.Phone_num=Phone_num
        self.Bank=Bank
        self.Password=Password
        
    def display_details(self):
         pass
                 

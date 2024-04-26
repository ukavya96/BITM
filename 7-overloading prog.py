class Location:
    def __init__(self,L1,L2):
        self.L1=L1
        self.L2=L2
    def __add__(self,other):
        return f"{self.L1+other.L1/2}+{self.L2+other.L2/2}i"
   

    def __eq__(self,other):
       if (other,L3):
         return self.L1 == other.L1 and self.L2 == other.L2
       else:
         return False
L1=Location(123456,157392)
L2=Location(391215,215739)
L3=L1+L2
print(L3)      
if (L1 == L3):
    print("Your location")  
else:
    print("Yes i have return")
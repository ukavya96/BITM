class Human:
    def __init__(self,hobby,food):
        self.fav_hobby=hobby
        self.fav_food=food
    def display_info(self):
        print(f"He plays{self.fav_hobby}, and he likes{self.fav_food}")
class sanjay(Human):
    def __init__(self,hobby,food,language):
        super().__init__(hobby,food)
        self.fav_language = language 
    def display_info(self):
        super().display_info()
        print(f"Language he speak {self.fav_language}")
user = sanjay("Games","Biriyani","Tamil")
user.display_info()
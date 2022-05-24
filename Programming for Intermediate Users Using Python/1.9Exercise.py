

class ClubMembers:
    def __init__(self,name,birthday,age,favoritefood,goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favoritefood = favoritefood
        self.goal = goal
    
    def display(self):
        print("Name: " + self.name)
        print("Birthday: " + self.birthday)
        print("Age: " + self.age)
        print("Favorite Food: " + self.favoritefood)
        print("Goal: " + self.goal)

class Clubofficers(ClubMembers):
        def __init__(self,name,birthday,age,favoritefood,goal,position):
            self.position = position
            ClubMembers.__init__(self,name,birthday,age,favoritefood,goal)
        def display1(self):
            print("Name: " + self.name)
            print("Birthday: " + self.birthday)
            print("Age: " + self.age)
            print("Favorite Food: " + self.favoritefood)
            print("Goal: " + self.goal)
            print("Position: " + self.position)

m_1 = ClubMembers("Tom", "January 16", "14", "Ice cream", "To be Happy")
o_4 = Clubofficers("Vera", "June 22", "16", "Beef Stroganoff", "To be the world's greastest chef", "Treasurer")



m_1.display()
o_4.display1()
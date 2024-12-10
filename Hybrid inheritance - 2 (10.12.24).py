class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class Manager(Employee):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.eid = eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print(f"Employee ID:{self.eid}")

class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept = dept
    def displayDeveloperInfo(self):
        print(f"Department:{self.dept}")

class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid = eid
        self.dept = dept
        self.teamsize = teamsize
    def displayTeamLeaderInfo(self):
        self.displayManagerInfo()
        self.displayDeveloperInfo()
        print(f"Team Size:{self.teamsize}")

emp = TeamLeader("Hema",32,345,"IT",10)
emp.displayTeamLeaderInfo()

class 
            

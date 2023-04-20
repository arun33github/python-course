class Student:
    def __init__(self,name,reg_no,dept,grade):
        self.name=name
        self.reg_no=reg_no
        self.dept=dept
        self.grade=grade

    def ishonrian(self):
        if self.grade in ["A","A+"]:
            print(self.reg_no+"is honorable student")
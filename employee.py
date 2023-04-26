class Employee:
    def __init__(self,employee_id,emp_salary,emp_exp,emp_dob):
        self.employee_id=employee_id
        self.emp_salary=emp_salary
        self.emp_exp=emp_exp
        self.emp_dob=emp_dob
        self.bonus=0
        print("Employee Records created !!")

    def salary_cal(self):
        self.emp_salary=(self.emp_salary*0.05 +self.emp_salary)
        print(f"salary incremented successfully{self.emp_salary}")

    def standard_bonus(self):
       # self.bonus=(self.emp_salary*0.10)

        if self.emp_exp>5:
            self.bonus=self.emp_salary*0.20


        else:
             self.bonus=(self.emp_salary*0.10)    
        print(f"bonus={self.bonus}")    
        

      

    # def dummy(self):
    #    print(f"inside dummy{self.bonus}")
        























        

from employee import Employee

print("welcome to Employee Records !! :")
emp_list=[]
for i in range(5):
    emp=Employee(input("employee_id :"),int(input("emp_salary :")),int(input("emp_exp :")),input("emp_dob :"))
    emp_list.append(emp)
for empl in emp_list:
    # print(empl.employee_id)
    empl.salary_cal()
    empl.standard_bonus()
    

   


# emp1=Employee(input("employee_id :"),input)
# emp2=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp3=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp4=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp5=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp6=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp7=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp8=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp9=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
# emp10=Employee(input("employee_id\nemp_salary\nemp_exp\nemp_dob:"))
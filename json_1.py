import json
from tabulate import tabulate

def emp_details(): 
    print("you have choosen employee Registration module !")
    employee_name=input("enter a name : ")
    employee_age=input("enter employee age :")
    employee_dept=input("enter a department :")
    employee_add=input("enter address :")
    tem_dict={
        "name":employee_name,
        "age":employee_age,
        "department":employee_dept,
        "address":employee_add
    }

    with open("file.json") as f:
        data=json.load(f)
    data["emp_details"].append(tem_dict)
    with open("file.json","w") as f:
        json.dump(data,f,indent=4)

    print("Employee details Registered successfully !!")


def view_details(): 
    with open("file.json","r") as f:
        data=json.load(f)

    print("s_no\temployee_name\temployee_age\temployee_dept\temployee_add")
    s_no=1
    employees=[]
    for emp in data["emp_details"]:
        # print(emp)s_no=1
        # print(f"{str(s_no)}\t{emp['name']}\t\t{emp['age']}\t\t{emp['department']}\t{emp['address']}")
        # temp_list=[s_no,emp['name'],emp['age'],emp['department'],emp['address']]
        # employees.append(temp_list)
        # s_no+=1
    # print(employees)
    # print(tabulate(employees,headers=["S.no","Name","age", "deparment","Location"]))
        temp_list=[s_no,emp["name"],emp['age'],emp['department'],emp['address']]
        employees.append(temp_list)
        s_no+=1
        print(employees)
        print(tabulate(employees,headers=["s_no","name","age","department","address"]))
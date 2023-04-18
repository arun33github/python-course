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

    # print("s_no\temployee_name\temployee_age\temployee_dept\temployee_add")
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
        # print(employees)
    print(tabulate(employees,headers=["s_no","name","age","department","address"])) 


    
def update_details(): 
    view_details()
    with open("file.json","r") as f:
        data=json.load(f)
        s_no=1
        choice=input("what you want to update(serial number):")
    for emp in data ["emp_details"]:
      if str(s_no)==choice: 
          print("what do you like to edit:\n1.name\n2.age\n3.department\n4.address\n5.all")
          choice_2=input("Enter your choice_2 : ")
          if choice_2=="1":
              name=input("enter a employee name:")
              emp["name"]=name
              print("employee details updated successfully:")

          elif choice_2=="2":
              age=input("enter employee age:")
              emp["age"]=age
              print("employee details updated successfully:")


          elif choice_2=="3":
              department=input("enter a department:")
              emp["department"]=department
              print("employee details updated successfully:")
              
          elif choice_2=="4":
              address=input("enter a updated address:")
              emp["address"]=address
              print("employee details updated successfully:")
              
          elif choice_2=="5":
               name=input("enter a employee name:")
               age=input("enter employee age:")
               department=input("enter a department:")
               address=input("enter a updated address:")
               print("employee details updated successfully:")
          else:
             print("invalid choice")
             break
      s_no+=1

    with open("file.json","w") as f:
        json.dump(data,f,indent=4)



               

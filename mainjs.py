import json_1


print("welcome to Employee Registration management!")


while True:
    print("you can perform below operations!:")
    print("1.registrtation\n2.view\n3.update\n4.delete")
    choice=input("Enter your operation:")

    if choice=="1":
        json_1.emp_details()

    elif choice=="2":
        print("you have chosen view employee details module!:")
        json_1.view_details()

    elif choice=="3":
        print("you have chosen update module!:")
        json_1.update_details()

    elif choice=="4":
        print("you have chosen delete module!:")
        json_1.delete_details()

        

    if_continue=input("do you want to continue (y/n)? :")
    if if_continue=="y":
        continue
    else:
        break

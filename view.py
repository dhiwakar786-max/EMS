from model import Employee , Address
from service import Service

class Employee_View:   

    service = Employee_Controller()
    while True :
        print("____EMPLOYEE MANAGEMENT SYSTEM_____")
        print("1.Add a Employeee Detail ")
        print("2.Display a Employee Detail")
        print("3.Update a Employee Detail")
        print("4.Delete a Employee Detail")
        print("5.Exit")
        choice = int(input("Enter the choice:"))
    
        if choice == 1 :
            name = input('Enter The Empolyee Name  :')

            if service.validate_employee_name(name):
                   pass
            else:
                   found=False
                   while(found==False):
                        print("Invalid name")
                        name=input("Enter employee name:")
                        if service.validate_employee_name(name):
                               found=True
                               
            emp_ID = int(input('Enter employee id   :'))
            age = int(input('Enter employee age    :'))
            if service.validate_employee_age(age):
                   pass
            else:
                   found=False
                   while(found==False):
                        print("Invalid age")
                        name=input("Enter employee age:")
                        if service.validate_employee_age(age):
                               found=True
                   
            salary = float(input('Enter employee\'salary  :'))
            email = input("Enter employee email id:")
            if service.validate_employee_email(email):
                   pass
            else:
                   found=False
                   while(found==False):
                        print("Invalid email")
                        name=input("Enter employee email:")
                        if service.validate_employee_email(email):
                               found=True
            doorno=int(input("Enter  door no:"))
            street=input("Enter street name : ")
            city=input("Enter  city:")
            pincode=int(input("enter pincode:"))
            address=Address(doorno,street,city,pincode)
            
            emp=Employee(name,emp_ID,age,salary,email,address)
            service.create(emp)
            print("Employee details added succesfully")
            
        elif choice == 2 :
                if service.display_employee_detail():
                        print("No employee details available")
                else:
                        choice_id=int(input("Enter the employee id:"))
                        employee=service.emp_details(choice_id)
                        print("Employee name :",employee.get_emp_name())
                        print("Employee ID:",employee.get_emp_id())
                        print("Employee age:",employee.get_emp_age())
                        print("Employee salary:",employee.get_emp_salary())
                        print("Employee email id :",employee.get_emp_email())
                        add = employee.get_emp_address()
                        print("Employee doorno:",add.get_emp_doorno())
                        print("Employee street: ",add.get_emp_street())
                        print("Employee city:",add.get_emp_city())
                        print("Employee pincode:",add.get_emp_pincode())
        elif choice == 3 :
                update_id=int(input("Enter the employee id :"))
                update_emp=service.update_employee_details(update_id) 
                print("1.Update Employee Name")
                print("2.Update Employee Age")
                print("3.Update Employee Salary")
                print("4.Update Employee Email id ")
                print("5.Update Address")
                ch=int(input("Enter the choice:"))
                if ch==1:
                        valname=input("Enter the name to update:")
                        service.update_employee_name(update_emp,valname)   
                        print("Name updated succesfully")
                elif ch==2:
                        valage=int(input("Enter the age to update:"))
                        service.update_employee_age(update_emp,valage)
                        print("age updated succesfully")
                elif ch==3:
                        valsal=float(input("Enter the salary to update:"))
                        service.update_employee_salary(update_emp,valsal)
                        print("salary updated succesfully")

                elif ch==4:
                        valemail=input("Enter employee email")
                        service.update_employee_email(update_emp,valemail)
                        print("Employee email updated succesfully")
                elif ch==5:

                        valadd=input("Enter the address:")
                        service.update_employee_address(update_emp,valadd)
                        print("Address updated succsefully")
                else:
                        print("Enter the valid choice")
                  
        elif choice == 4:
            del_id=int(input("Enter the employee id:")) 
            service.delete_employee_detail(del_id)
            print("Employeee detail removed s(uccefully")
            
        elif   choice==5:
                break      
        else:
                print('Give the correct input please ---..........')

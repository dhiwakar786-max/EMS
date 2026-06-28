from model import Employee , Address
from service import Service

class View:   

    service = Service()
    while True :
        print("____EMPLOYEE MANAGEMENT SYSTEM_____")
        print("1.add a employeee")
        print("2.display a employee")
        print("3.update a employee")
        print("4.Delete a employee")
        print("5.Exit")
        choice = int(input("enter the choice:"))
    
        if choice == 1 :
            name = input('enter empolyee name  :')
            emp_ID = int(input('enter employee id   :'))
            age = int(input('enter employee age    :'))
            salary =float(input('enter employee\'salary  :'))
            doorno=int(input("Enter  door no:"))
            street=input("Enter street name : ")
            city=input("Enter  city:")
            pincode=int(input("enter pincode:"))
            address=Address(doorno,street,city,pincode)
            
            emp=Employee(name,emp_ID,age,salary,address)
            service.create(emp)
            print("Employee details added succesfully")
            
        elif choice == 2 :
                if service.display():
                        print("No employee details available")
                else:
                        choice_id=int(input("Enter the employee id:"))
                        employee=service.emp_details(choice_id)
                        print("Employee name :",employee.get_emp_name())
                        print("Employee ID:",employee.get_emp_id())
                        print("Employee age:",employee.get_emp_age())
                        print("Employee salary:",employee.get_emp_salary())
                        add = employee.get_emp_address()
                        print("Employee doorno:",add.get_emp_doorno())
                        print("Employee street: ",add.get_emp_street())
                        print("Employee city:",add.get_emp_city())
                        print("Employee pincode:",add.get_emp_pincode())
        elif choice == 3 :
                update_id=int(input("Enter the employee id :"))
                update_emp=service.update_details(update_id) 
                print("1.update name")
                print("2.update age")
                print("3.update salary")
                print("4.Update address")
                ch=int(input("enter the choice:"))
                if ch==1:
                        valname=input("enter the name to update:")
                        service.update_name(update_emp,valname)   
                        print("Name updated succesfully")
                elif ch==2:
                        valage=int(input("Enter the age to update:"))
                        service.update_age(update_emp,valage)
                        print("age updated succesfully")
                elif ch==3:
                        valsal=float(input("enter the salary to update:"))
                        service.update_salary(update_emp,valsal)
                        print("salary updated succesfully")
                elif ch==4:

                        valadd=input("Enter the address:")
                        service.update_address(update_emp,valadd)
                        print("Address updated succsefully")
                else:
                        print("enter the valid choice")
                  
        elif choice == 4:
            del_id=int(input("enter the employee id:")) 
            service.delete(del_id)
            print("employeee detail removed s(uccefully")
            
        elif   choice==5:
                break      
        else:
                print('give the correct input please ---..........')



class Employee:

    def __init__(self,name,id,age,salary):
        self.emp_name   = name
        self.emp_id     = id
        self.emp_age    = age
        self.emp_salary = salary

    def get_emp_name(self):
        return self.emp_name

    def set_emp_name(self, value):
        self.emp_name = value

    def get_emp_id(self):
        return self.emp_id

    def set_emp_id(self, value):
        self.emp_id = value

    def get_emp_age(self):
        return self.emp_age

    def set_emp_age(self, value):
        self.emp_age = value

    def get_emp_salary(self):
        return self.emp_salary

    def set_emp_salary(self, value):
        self.emp_salary = value

       
    def display(self):
        print("Employee name:",self.emp_name)
        print("Emplouee id:",self.emp_id)
        print("Employee age:",self.emp_age)
        print("Employee salary :",self.emp_salary)
    
lis=[]
while True :
    print("____EMPLOYEE MANAGEMENT SYSTEM_____")
    print("1.add a employeee")
    print("2.display a employee")
    print("3.update a employee")
    print("4.Delete a employee")
    print("5.Exit")
    choice=int(input("enter the choice:"))
    
    if choice == 1 :
        name = input('enter empolyee name  :')
        emp_ID = int(input('enter employee id   :'))
        age = int(input('enter employee age    :'))
        salary =float(input('enter employee\'salary  :'))
        emp=Employee(name,emp_ID,age,salary)
        lis.append(emp)
        print("Employee details added succesfully")
            
    elif choice == 2 :
        if  len(lis)==0:
              print("No employee details available")
        else:
            choice_id=int(input("Enter the employee id:"))
            for emp in lis:
            
                if choice_id==emp.get_emp_id():
                    print("Employee name :",emp.get_emp_name())
                    print("Employee ID:",emp.get_emp_id())
                    print("Employee age:",emp.get_emp_age())
                    print("Employee salary:",emp.get_emp_salary())
                
    elif choice == 3 :
            update_id=int(input("Enter the employee id :"))
            for emp in lis:
                if update_id==emp.get_emp_id():
                    print("1.update name")
                    print("2.update age")
                    print("3.update salary")
                    ch=int(input("enter the choice:"))
                    if ch==1:
                        valname=input("enter the name to update:")
                        emp.set_emp_name(valname)    
                        print("Name updated succesfully")
                    elif ch==2:
                        valage=int(input("Enter the age to update:"))
                        emp.set_emp_age(valage)
                        print("age updated succesfully")
                    elif ch==3:
                        valsal=float(input("enter the salary to update:"))
                        emp.set_emp_salary(valsal)
                        print("salary updated succesfully")
    elif choice == 4:
        del_id=int(input("enter the employee id:")) 
        for emp in lis:
            if del_id==emp.get_emp_id():
                lis.remove(emp)
                print("employeee detail removed succefully")
            
    elif   choice==5:
         break     
            
    else:
                print('give the correct input please ---..........')




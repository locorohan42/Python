#Rohan Abraham
#This is the driver file that tests the classes
import RohanAbraham_assign_11_Employee_Classes


def test():
    #Test the retail item class
    print("*******Employee Test*******")
    my_employee = RohanAbraham_assign_11_Employee_Classes.Employee("John Fish", 116)
    print("Employee: ", my_employee)
    print(my_employee.get_name() + " " + str(my_employee.get_number()))
    #Demonstrate getters

    my_employee.set_name("Rohan Abe")
    my_employee.set_number(17)
    print("Employee: ", my_employee)
    #Demonstrate setters work properly
    print()

    #Test the ProductionWorker class
    print("*******Production Worker Test*******")
    my_production_worker = RohanAbraham_assign_11_Employee_Classes.ProductionWorker("Jack Bronsky", 116, 1, 14.44)
    print("Production Worker: ", my_production_worker)
    print(str(my_production_worker.get_shift_number()) + " " +  str(my_production_worker.get_hourly_pay_rate()))
    #Demonstrate the getters work

    my_production_worker.set_name("Rohan Abe")
    my_production_worker.set_number(17)
    my_production_worker.set_hourly_pay_rate(22.5)
    my_production_worker.set_shift_number(2)
    print("Production Worker: ", my_production_worker)
    #Demonstrate setters work properly
    print()

    #Test the ShiftSupervisor class
    print("*******Shift Supervisor Test*******")
    my_shift_supervisor = RohanAbraham_assign_11_Employee_Classes.ShiftSupervisor("Jack Dorsey", 126, 50000, 0)
    print("Shift Supervisor: ", my_shift_supervisor)
    print(str(my_shift_supervisor.get_annual_salary()) + " " + str(my_shift_supervisor.get_annual_production_bonus()))
    #Demonstrate the getters work

    my_shift_supervisor.set_name("Rohan Abe")
    my_shift_supervisor.set_number(1337)
    my_shift_supervisor.set_annual_salary(60000)
    my_shift_supervisor.set_annual_production_bonus(10000)
    print("Shift Supervisor: ", my_shift_supervisor)
    #Demonstrate setters work properly
    print()

test()

def main():
    name = input("Enter the name of an employee: ")
    number = int(input("Enter the number of an employee: "))
    shift_number = int(input("Enter the shift number of an employee (1 for day 2 for night): "))
    hourly_pay = float(input("Enter the hourly pay of an employee: "))

    worker = RohanAbraham_assign_11_Employee_Classes.ProductionWorker(name,number,shift_number,hourly_pay)
    print(worker)
    print()

    name1 = input("Enter the name of an employee: ")
    number1 = int(input("Enter the number of an employee: "))
    salary = float(input("Enter the salary of an employee: "))
    bonus = float(input("Enter the bonus of an employee: "))

    worker1 = RohanAbraham_assign_11_Employee_Classes.ShiftSupervisor(name1,number1,salary,bonus)
    print(worker1)

main()

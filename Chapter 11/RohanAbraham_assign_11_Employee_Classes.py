#Rohan Abraham
#Program demonstrates inheritance showing the relationship between the employee
#base class and the production worker and shift supervisor derived classes

class Employee:
    #Class holds info about an employee
    def __init__(self, name, number):
        #Initializer method that sets attributes
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name
        #Update the name

    def set_number(self, number):
        self.__number = number
        #Update the __number

    def get_name(self):
        return self.__name
        #Return the __name

    def get_number(self):
        return self.__number
        #Return the __number

    def __str__(self):
        return "Employee name: " + self.__name + " Employee Number: " + str(self.__number)
        #Returns the classes information as a string

class ProductionWorker(Employee):
    #Class holds infor about a ProductionWorker employee
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        #Initialize the attributes
        Employee.__init__(self, name, number)
        #Call the base classes Initializer method

        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate
        #Initialize derived class attributes

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
        #Set the shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate
        #Set the hourly pay rate

    def get_shift_number(self):
        return self.__shift_number
        #Return the shift number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
        #Return the hourly pay

    def __str__(self):
        return "Employee name: " + ProductionWorker.get_name(self) + " Employee Number: " + str(ProductionWorker.get_number(self))+ " Shift Time: " + str(self.__shift_number) + " Hourly Pay: "+ str(self.__hourly_pay_rate)
        #Returns the classes information as a string

class ShiftSupervisor(Employee):
    #Class holds infor about a shift supervisor employee
    def __init__(self, name, number, annual_salary, annual_production_bonus):
        #Initialize the attributes
        Employee.__init__(self, name, number)
        #Call the base classes Initializer method

        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus
        #Initialize derived class attributes

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
        #Set the annual salary

    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = annual_production_bonus
        #Set the bonus pay

    def get_annual_salary(self):
        return self.__annual_salary
        #Return the salary

    def get_annual_production_bonus(self):
        return self.__annual_production_bonus

    def __str__(self):
        return "Employee name: " + ShiftSupervisor.get_name(self) + " Employee Number: " + str(ShiftSupervisor.get_number(self))+ " Annual Salary: " + str(self.__annual_salary) + " Annual Bonus: "+ str(self.__annual_production_bonus)
        #Returns the classes information as a string

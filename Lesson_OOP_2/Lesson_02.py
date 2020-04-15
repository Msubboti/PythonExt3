from datetime import datetime, date

class Employee:
    def __init__(self, name, surname, email, phone_number, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone_number
        self.salary = salary

    def work(self):
        return 'I come to the office.'

    def check_salary(self, current_date=datetime.now()):
        if type(current_date) is int:
            return self.salary * current_date
        else:
            mountly_salary = 0
            func = lambda x: date(current_date.year, current_date.month, x)
            a = [func(item) for item in range(1, current_date.day + 1)]
            for dates in a:
                if datetime.isoweekday(dates) == 6 or datetime.isoweekday(dates) == 7:
                    pass
                else:
                    mountly_salary += self.salary
            return mountly_salary


    def __str__(self):
        return "{}: {} , {}".format(self.__class__.__name__, self.name, self.surname)

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

class Recruiter(Employee):
    def __init__(self, name, surname, email, phone_number, salary, hired_this_month):
        super().__init__(name, surname, email, phone_number, salary)
        self.hired_this_month = hired_this_month

    def work(self):
        return 'I come to office and start hiring'



class Programmer(Employee):
    def __init__(self, name, surname, email, phone_number, salary, tech_stack, closed_this_month):
        super().__init__(name, surname, email, phone_number, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month
    def work(self):
        return 'I come to office and start coding.'

    def __eq__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return len(self.tech_stack) == len(other.tech_stack)
        else:
            return self.salary == other.salary
    def __lt__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return len(self.tech_stack) < len(other.tech_stack)
        else:
            return self.salary < other.salary

    def __gt__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return len(self.tech_stack) > len(other.tech_stack)
        else:
            return self.salary > other.salary

    def __add__(self, other):
        self.tech_stack = tuple(set(self.tech_stack + other.tech_stack))
        self.closed_this_month = self.closed_this_month + other.closed_this_month
        return  self

if __name__ == "__main__":

    emplo1 = Employee('Ivan', 'Gromov', 'nokia3310_Snake2@ukr.net', 650, 20)
    # Method 'work' is returned 'I come to the office.'
    print(emplo1.work())
    # Method 'check_salary' is answering, how many money will Ivan get for 15 days?
    print("_______How many money will {} get for 15 days?______".format(emplo1.name))
    print(emplo1.check_salary(15))
    print("______The {}'s salary from beginning of month.______".format(emplo1.name))
    print(emplo1.check_salary())

    print("\n________Calling method work() and check method __str__ of class Programmer________\n")
    empl2= Programmer('Sergii', 'Efremov', 'morojenko_v_stakane@mail.com', 765, 15, ('Java', 'C++', 'CSS', 'HTML'), 2)
    """empl2 is instance of class Programmer, method 'work' 
        was modified and is working not as in parent class.
        method will return 'I come to office and start coding.' """
    print(empl2.work())
    # method __str__ was modified.
    # Information about object will include occupation: name and surname.
    print(empl2)

    empl4 = Programmer('Vasiliy', 'Zverev', 'chihuahua@gmail.com', 654, 12, ('Python', 'CSS', 'PHP', 'HTML', 'DB'), 5)

    print("\n________Two employee is compared by value of salary ({} VS {})________\n".format(empl4.surname, empl2.surname))
    # Compare two Programmer by the list of technology

    print(empl4 > empl2)


    empl3= Recruiter('Svetlana', 'Ternova', 'svetic84@gmail.com', 850, 12, 5)
    print("\n________What does {} do at work?________\n".format(empl3.name))
    print(empl3.work())
    print(empl3)

    # Possibility to compare employee by the value of salary is added.
    print("\n________Does {} get lower salary as {}?________\n".format(empl2.name, emplo1.name))
    print(empl2 < emplo1)
    print("\n________Does {} get higher salary as {}?________\n".format(empl3.name, emplo1.name))
    print(empl3 >= emplo1)
    print("\n________Does {} get higher salary as {}?________\n".format(empl3.name, empl4.name))
    print(empl3 > empl4)

    # Creating New Programmer which is include tech stack of two other employee
    print("\n________Here are {}'s skills before learning with {}.________\n".format(empl4.name, empl2.name))
    print(empl4.tech_stack)
    empl4 = empl4 + empl2
    print("\n________Here are {}'s skills after learning with {}.________\n".format(empl4.name, empl2.name))
    print(empl4.tech_stack)
    print("\n________Their completed tasks should be summarize.________\n")
    print(empl4.closed_this_month)


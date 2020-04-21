"""

Module defines base class Employee,
this class is parent for other classes of the program.

"""

from datetime import datetime, date



class Employee:
    """

    This class defines employees by
    the parameters (name, surname, email, phone, salary).

    """

    def __init__(self, name, surname, email, phone_number, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone_number
        self.salary = salary
        self.valid_email()
        self.save_emeil()


    def save_emeil(self):
        with open(r'email.txt', 'a') as f:
            f.write(self.email + "\n")
        f.close()

    def valid_email(self):
        file = open(r'email.txt', 'r')
        for line in file:
            print(line)
            if self.email in line:
                raise ValueError('Email has already existed.')
            else:
                pass
        file.close()


    @staticmethod
    def work():
        """
        Function "work" returns string
        :return: I come to the office.
        """
        return 'I come to the office.'

    def check_salary(self, current_date=datetime.now()):
        """
        Method will calculate value of salary for fixed days,
        if number of days is defined as argument when method was called

        :param current_date: if number of days is not defined,
        method takes current date and will calculate salary
        from beginning current month till today.

        :return: Result will be a value of salary as numeric

        """
        monthly_salary = 0
        int_current_date = isinstance(current_date, int)
        if int_current_date:
            monthly_salary = self.salary * current_date
        else:
            func = lambda x: date(current_date.year, current_date.month, x)
            list_days = [func(item) for item in range(1, current_date.day + 1)]
            for one_day in list_days:
                if datetime.isoweekday(one_day) == 6 or datetime.isoweekday(one_day) == 7:
                    pass
                else:
                    monthly_salary += self.salary
        return monthly_salary

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

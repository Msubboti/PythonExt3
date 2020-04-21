"""
This module include classes Programmer and Recruiter
which are child classes for Employee

"""

from .employee import Employee


class UnableToWorkException(Exception):
    pass

class Recruiter(Employee):
    """

    Class Recruiter is child class for Employee,
    it has additional property "hired_this_month"
    which is defined how many new employee was hired by this Recruiter

    """
    def __init__(self, name, surname, email, phone_number, salary, hired_this_month):
        super().__init__(name, surname, email, phone_number, salary)
        self.hired_this_month = hired_this_month

    def work(self):
        """

        Method work was changed for instance of class Recruiter.
        It returns string as well, but string is little bit different.

        :return: String : I come to office and start hiring

        """
        return 'I come to office and start hiring'


class Programmer(Employee):
    """

    Class Programmer is child class for Employee,
    it has additional property "tech_stack" and "closed_this_month", which are defines:

    "tech_stack" - list of bugs which were assigned on this employee
    "closed_this_month" - number of bugs which were closed in this month

    """
    def __init__(self, name, surname, email, phone_number, salary, tech_stack, closed_this_month):
        super().__init__(name, surname, email, phone_number, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month

    def work(self):
        """
        Method work was changed for instance of class Programmer.
        It returns string as well, but string is little bit different.

        :return: String : I come to office and start coding.
        """
        return 'I come to office and start coding.'

    def __eq__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            expression = len(self.tech_stack) == len(other.tech_stack)
        else:
            expression = self.salary == other.salary
        return expression

    def __lt__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            expression = len(self.tech_stack) < len(other.tech_stack)
        else:
            expression = self.salary < other.salary
        return expression

    def __gt__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            expression = len(self.tech_stack) > len(other.tech_stack)
        else:
            expression = self.salary > other.salary
        return expression

    def __add__(self, other):
        self.tech_stack = tuple(set(self.tech_stack + other.tech_stack))
        self.closed_this_month = self.closed_this_month + other.closed_this_month
        return self


class Candidate:
    """
    The class includes information about candidate,
    such as name, contact information, skills and grade of main skill.
    """
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException('I am not hired yet, lol')


class Vacancy:
    """
    Class includes information about available vacancy.
    There are: Title of vacancy, competencies and required level of skill.
    """
    def __init__(self, title, main_skill, main_skill_grade):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

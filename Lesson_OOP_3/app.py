"""

Module for running program.
Listing is checking possibility of parent and child classes.

"""


from models.position import Programmer, Recruiter, Candidate, Vacancy

if __name__ == "__main__":

    # Creating instances of class Programmer
    VASILII = Programmer('Vasyliy', 'Kornev', 'stark96@mail.com', "+380669995465",
                         20, ('Java', 'PHP', 'C++', 'Python', 'Delphi'), 3)

    SVETLANA = Programmer('Svatlana', 'Tarasenko', 'svetlana.tarasenko@cloud.com', '+380671325487',
                          18, ('HTML', 'CSS', 'Python', 'Assembler', 'SQL', 'Java'), 2)

    # Creating instances of class Recruiter
    ANNA = Recruiter('Anna', "Rogova", 'rogalic84@gmail.com', '+30999998563', 15, 3)

    # Creating instances of class Candidates
    CANDIDATE_PHP_1 = Candidate('Vitaliy Smirnov', 'smirnow.vitaliy@icloud.com',
                                ('PHP', 'C#', 'C++', 'SQL'), 'PHP', 'Middle')
    CANDIDATE_PHP_2 = Candidate('Andrii Zubarev', 'Zubarev85@gmail.com',
                                ('Python', 'C++', 'PHP', 'HTML', 'CSS'), 'PHP', 'Middle')

    CANDIDATE_JAVA_1 = Candidate('Alisa Gurova', 'gurova.alise@ukr.net',
                                 ('Assembler', 'Ruby', 'Lua', 'Java'), 'Java', 'Senior')

    # Creating instances of class Vacancy

    PHP_MIDDLE_VASILII_DEP = Vacancy("Junior+/Middle PHP Developer", 'PHP', 'Middle')

    JAVA_SENIOR_SVETLANA_DEP = Vacancy("Java developer: JavaFx, Web, "
                                       "Selenium, OOP", 'Java', 'Senior')

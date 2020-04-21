Time:	2020-04-21 21:47:45.118315	Type of error: UnableToWorkException

Traceback (most recent call last):
  File "D:/Python/Git/PythonExt3/Lesson_OOP_3/app.py", line 46, in <module>
    Condidate1.work()
  File "D:\Python\Git\PythonExt3\Lesson_OOP_3\models\position.py", line 101, in work
    raise UnableToWorkException('I am not hired yet, lol')
models.position.UnableToWorkException: I am not hired yet, lol
 

Time:	2020-04-21 21:47:50.914446	Type of error: ValueError

Traceback (most recent call last):
  File "D:/Python/Git/PythonExt3/Lesson_OOP_3/app.py", line 45, in <module>
    20, ('Java', 'PHP', 'C++', 'Python', 'Delphi'), 3)
  File "D:\Python\Git\PythonExt3\Lesson_OOP_3\models\position.py", line 48, in __init__
    super().__init__(name, surname, email, phone_number, salary)
  File "D:\Python\Git\PythonExt3\Lesson_OOP_3\models\employee.py", line 26, in __init__
    self.valid_email()
  File "D:\Python\Git\PythonExt3\Lesson_OOP_3\models\employee.py", line 40, in valid_email
    raise ValueError('Email has already existed.')
ValueError: Email has already existed.
 


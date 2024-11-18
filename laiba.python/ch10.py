#class
class Emplyee:
  language="English"#This is a class atributes
  salary=100000
laiba=Emplyee()
laiba.name="laiba"#This is a instance atributes
print(laiba.language,laiba.salary,laiba.name)  
Areeba=Emplyee()
Areeba.name="Areeba"
print(Areeba.language,Areeba.salary,Areeba.name)  
#Metod and self parameters
class Emplyee:
  language="English"
  salary=100000
  def change_language(self):
    self.language="Urdu"
    print(f"The language is {self.language}.and the salary is {self.salary}")
laiba=Emplyee()
laiba.name="laiba"
print(laiba.language,laiba.salary,laiba.name)  
laiba.change_language()

#static method
class Emplyee:
  language="English"
  salary=100000

  @staticmethod
  def greet():
    print("good morning")
laiba=Emplyee()
laiba.name="laiba"
print(laiba.language,laiba.salary,laiba.name)  
laiba.greet()



#init
class Employee:
    language = "English"
    salary = 100000

    def __init__(self, name, language, salary):
        print("Good morning")
        self.name = name
        self.language = language
        self.salary = salary

    def get(self):
        print(f"The language is {self.language} and the salary is {self.salary}.")

# Creating an Employee instance with correct arguments
areeba = Employee("areeba", "css", 12000)

# Accessing instance attributes
print(areeba.language, areeba.salary)

# Calling the get method
areeba.get()
# print(__name__)

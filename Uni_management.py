from abc import ABC, abstractmethod
class Base(ABC):

    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def detail(self):
        return f"My name is {self.name} and my id is {self.id}"
    
    @abstractmethod
    def get_role(self):
        pass

class Student(Base):
    
    def __init__(self,gpa,year,name,id):
        super(). __init__(name,id)
        self.__gpa=gpa
        self.year=year

    def get_gpa(self):
        return self.__gpa
    
    def update_gpa(self,new_gpa):
        self.__gpa=new_gpa

    def get_role(self):
        return "I am enroll as a Student"
    
class Teacher(Base):

    def __init__(self,name,id,salary,specialization):
        super().__init__(name,id)
        self.__salary=salary
        self.specialization=specialization

    def get_salary(self):
        return  self.__salary
    
    def increase_salary(self,increment):
        if increment<0:
            print("The number yo enter is invalid")
        else:
            self.__salary+=increment
    def get_role(self):
        return "I am enroll as a Teacher"
    
class Course:

    def __init__(self,course_name,teacher):
        self.course_name=course_name
        self.teacher=teacher
        self.students=[]

    def add_student(self,name):
        self.students.append(name)
       
        
    def remove_student(self,remove):
        self.students.remove(remove)

    def __repr__(self):
        return self.students
    
    def list_of_Student(self):
        return self.students

class Aggregation:
    
    def __init__(self,courses):
        self.courses=courses
        self.list=[]
        
    def add_coures(self,course):
        self.list.append(course)
        
            
           

    def  __repr__(self):
        return str(self.list)
    
class Department:

    def __init__(self,department,aggregation):
        self.department=department
        self.list_of_course=aggregation
    

    # def __repr__(self):
    #     return str(self.list_of_course.list)
    def list_courses(self):
        return self.list_of_course.list
    
s=Student(3.5,2025,"Ammar",121)
t=Teacher("Ahsan",123,10000,"MSE")
c=Course("Python",t)
a=Aggregation("Python")
d=Department("BSCS",a)

print("**** The courses offer to a Students ****")
a.add_coures("Java")
a.add_coures("Calculus")
a.add_coures("Physics")
a.add_coures("Data Science")
a.add_coures("AI")
print(d.list_courses())
print(f"Teacher name:{c.teacher.name}","***",f"Course:{c.course_name}")
c.add_student("Ammar")
c.add_student("Ahmed")
print(f"****Number of Student for this course****:{c.students}")

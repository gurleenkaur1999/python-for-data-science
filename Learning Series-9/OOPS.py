class Student:
    school='Ubc'

simran=Student()
simran.school='Langara'
simran.school

class help:
 code='red'
 @classmethod
 def change_code(cls,new_code):
   cls.code=new_code

help.change_code("blue")
help.code

class Car:
  brand='toyota'

obj1=Car()
obj1.brand
ob2=Car()
ob2.brand

#Create another object c2
#Assign a variable color = "Red" to this object only
#Print c2.color and try printing c1.color (what happens?)

c2=Car()
c2.color='red'
c2.color

ob2.color

#Create object s1
#Assign s1.name = "Alice"
#Call s1.display_name()

class student:
 name=""
 def print_name(self):
   print(self.name)

s1=student()
s1.name="gur"

s1.print_name()

#Create object e1 and call e1.show_company()

#Change Employee.company = "Microsoft"

#Call e1.show_company() again

class corporation:
  company="IBM"
  def show_company(self):
   print(self.company)
e1=corporation()
e1.show_company()
e1.company="Microsoft"
e1.show_company()

h1=help()
h1.code="red"

help.change_code("blue")
h1.code
h2=help()
h2.code
  
#Q7. Shared class variable
#Create class Counter with count = 0
#Create 2 objects c1 and c2

#Increase Counter.count manually

#Print c1.count and c2.count


class counter:
  count=0

c1=counter()
c1.count

c2=counter()
c2.count

counter.count=counter.count+1

c1.count
c2.count

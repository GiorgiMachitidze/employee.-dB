from employee import Employee
from db import conn

user1 = Employee("John", "Doe", 30)
user2 = Employee("Alice", "Smith", 25)
user3 = Employee("Michael", "Johnson", 35)
user4 = Employee("Sarah", "Brown", 28)
user5 = Employee("Sarah", "Brown", 28)
# user1.save()
# user2.save()
# user3.save()
# user4.save()
# user5.save()
# print(user1 > user2)
# user1.delete(4)
# print(Employee.get_employee(name = "John"))
# print(Employee.get_employee(name = "Alice", surname = "Smith"))
conn.commit()
conn.close()

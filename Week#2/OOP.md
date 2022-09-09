# Object Oriented Programming in Python:
Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects. Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects.

### **Main Concepts of Object-Oriented Programming (OOPs):**
* Class
* Objects
* Polymorphism
* Encapsulation
* Inheritance

## **`Class:`**
A class is a blueprint for the object.

We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, a parrot is an object.

The example for class of `car` can be :
```python
class Python:
```
Here, we use the class keyword to define an empty class Car. From class, we construct instances. An instance is a specific object created from a particular class.

## **`Object:`**
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

The example for object of car class can be:
```python
Tesla = Car()
```
## **`__init__:`**
The Default __init__ Constructor in C++ and Java. Constructors are used to initializing the object’s state. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

```python
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('Zain')
p.say_hi()
```
## **`Creaton of Classes and Objects:`**
```python
class Customer:
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
        print("customer created")
    def update_membership(self,new_membership):
        print("Calculating costs")
        self.membership_type=new_membership
    def __str__(self):
        return self.name +" "+self.membership_type
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    def __eq__(self,other):
        if self.name==other.name and self.membership_type==other.membership_type:
            return True
        return False
customers=[Customer('Zain','Silver'),Customer('Ali','Gold')]
print(customers[0].name)
Customer.print_all_customers(customers)
print(customers[0]==customers[1])
```

## **`__hash__ method:`**

Python hash() function is a built-in function and returns the hash value of an object if it has one. The hash value is an integer which is used to quickly compare dictionary keys while looking at a dictionary.
Objects hashed using hash() are irreversible, leading to loss of information.
hash() returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def age(self):
        return self.age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)
members = {
    Person('Zain', 21),
    Person('Ali', 21)
}
```

## **`__repr__ vs __str__ Method:`**
The `__str__` method returns a string representation of an object that is human-readable while the `__repr__` method returns a string representation of an object that is machine-readable.

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'


person = Person('Zain', 'Ali', 22)
# use str()
print(person)

# use repr()
print(repr(person))
```
## **`Encapsulation in Python:`**
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables. A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
```python
class Base:
	def __init__(self):
		self._a = 2

class Derived(Base):
	def __init__(self):
  
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

print("Accessing protected member of obj1: ", obj1._a)

print("Accessing protected member of obj2: ", obj2._a)
```
## **`Inheritance in Python:`**
Inheritance is the capability of one class to derive or inherit the properties from another class. 

**Benefits of inheritance are:**
It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
```python
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
 
 class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
  ```
## **`Polymorphism in Python:`**
The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.
```python
def add(x, y, z = 0):
	return x + y+z

print(add(2, 3))
print(add(2, 3, 4))
```

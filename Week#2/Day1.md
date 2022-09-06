# Python:
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. We can use it for Machine Learning, Web Development, AI and much more. We can also use it for automation, to increase productivity and save time. 

- ## Printing anything to console:

> We use `print()` command to display anything in the terminal.
```python
print("Hello World")
```
- ## Variables:
> We use ***variables*** to store any kind of data values.
```python
age = 12
name = "Zain Ali Shah"
weight = 65.6
student = True
```
- ## Getting input from user:
> We use `input()` to recieve any kind of input from the user. The user has to type the input in the console. We can save this input into a variable to use it later in our program.
```python
input("What is your your name? ")
```
- ## Typecasting:
> We have three kinds of data values.
> * Integers
> * Strings
> * Boolean
> We use typecasting to convert one of these data values into other.
* Integers to string:
```python
temp = 69
temp2 = str(temp)
print(temp2)
```

* String to integer:
```python
temp = "69"
temp2 = int(temp)
print(temp2)
```
For more, click [here]!

[here]: https://www.programiz.com/python-programming/type-conversion-and-casting

- ## Strings:
> We can type any kind of text in enclosed `"` or `'` and assign it to a variable. Any integer, or text enlosed in quotations will be considered a text.
```python
f_name = "Zain Ali"
l_name = "Shah"
```
> We can also use ***concatenation*** to join two strings.
```python
print(f_name + l_name)
```
> We can use various methods to manipulate strings.
>
> `upper()` converts all alphabetical characters in a string to uppercase.
>
> `lower()` converts all alphabetical characters in a string to lowercase.
>
> `find()` takes a sub-string as an argument, finds it within the main string, and returns the index of where that sub-string starts. If it could not find the sub-string within the string, it returns -1.
>
> `index()` is the same as find() but raises an error if the sub-string is not found.
>
> `replace()` takes two sub-strings as arguments and replaces all occurences of the first sub-string within the main string with the second sub-string.

For more, click [here]!

[here]: https://www.w3schools.com/python/python_strings_methods.asp

- ## Operators :
- #### ***Arithmetic Operators:***
> These are used to perform mathematical operations.
>
> `+` is used to add numbers.
>
> `-` is used to subtract numbers.
>
> `*` is used to multiply numbers.
>
> `%` is used for modulus.
>
> `**` is used to raise a number to a power.
>
> `//` is used to divide numbers and then round the result down to nearest integer.

- #### ***Assignment Operators:***
> We use `=` to assign values.

- #### ***Comparision Operators:***
> These operators return `True` or `False` after comparing two entities.
>
> `==` checks for equality and returns True if the objects are same, else returns False.
>
> `>` checks if the first object is greater than the second.
> > 
> `<` checks if the first object is lesser than the second.
> 
> `!=` checks for inequality and returns True if the objects are different, else returns False.
> 
> `<=` returns True if the first object is lesser than or equal to the second object, else returns False.
> 
> `>=` returns True if the first object is greater than or equal to the second object, else returns False.


- #### ***Logical Operators:***
> These operators are used to combine `True` or `False` expressions.
> 
> `and` returns True if both expressions are true, else returns False.
> 
> `or` returns True if atleast one of the expressions is true, else returns False.
> 
> `not` inverts the result of a boolean expression.

- #### ***Identity Operators:***
> Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
> 
> `is` returns true if both variables are the same object.
> 
> `is not` 	returns true if both variables are not the same object.

- #### ***Membership Operators:***

> Membership operators are used to test if a sequence is presented in an object.
> 
> `in` returns True if a sequence with the specified value is present in the object.
> 
> `not in` returns True if a sequence with the specified value is not present in the object.

- ## Python Conditions:

> Python supports the usual logical conditions from mathematics and control flow of the program using `if` statements.
```python
if expression_1:
    # code to run if expression_1 is true
elif expression_2:
    # code to run if expression_1 is false but expression_2 is true
else:
    # code to run if expression_1 and expression_2 are both false
```
- ## Python Sequences:
> In Python programming, sequences are a generic term for an ordered set which means that the order in which we input the items will be the same when we access them. Python supports six different types of sequences.
> These are **strings, lists, tuples, byte sequences, byte arrays,** and **range objects**

- #### ***Lists:***
> Python lists are similar to an array but they allow us to create a heterogeneous collection of items inside a list. A list can contain numbers, strings, lists, tuples, dictionaries, objects, etc.
>
> Lists are declared by using square brackets around comma-separated items.

```python
list1 = [1,2,3,4]
list2 = [‘red’, ‘green’, ‘blue’]
list3 = [‘hello’, 100, 3.14, [1,2,3] ]
```
> Lists are mutable which makes it easier to change and we can quickly modify a list by directly accessing it.
```python
list = [10,20,30,40]
list[1] = 100
print( list)
```
> There are different methods that can be used on lists.
> 
> `append()` takes a value as an argument and appends it at the end of the list.
> 
> `insert()` takes an integer value for the index and a value, and stores the value at the specified index.
> 
> `remove()` takes a value as an argument and removes it from the list.
> 
> `pop()` takes the index position as the argument and removes the value at that index.
> 
> `clear()` removes all elements from a list.
> 
> `reverse()` reverses the order of elements within the list.

- #### ***Tuples:***
> Tuples are also a sequence of Python objects. A tuple is created by separating items with a comma. They can be optionally put inside the parenthesis () but it is necessary to put parenthesis in an empty tuple.
>
> A single item tuple should use a comma in the end.

```python
tup = ()
print( type(tup) )
tup = (1,2,3,4,5)
tup = ( “78 Street”, 3.8, 9826 )
print(tup)
```
> Tuples are also immutable like strings so we can only reassign the variable but we cannot change, add or remove elements from the tuple.
> 
> There are different methods that can be used on tuples.
> 
> `count()` takes a value as argument and returns the number of times that value occured within the tuple.
> 
> `index()` takes a value as argument and returns the first index at which it occurs within the tuple. Raises an error if the value is not found

- #### ***Sets:***
> Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable, and unindexed.
```python
set1 = {"abc", 34, True, 40, "male"}
```
> There are different methods that can be used on sets.
> 
> `add()` takes a value as an argument and adds it to the set.
> 
> `remove()` takes a value as an argument and removes it from the set. If the value is not in set, remove() will raise an error.
> 
> `discard()` works the same as remove() but will not raise an error if the value is not found in set.
> 
> `clear()` clears out the set.

- ## Loops:
> Python programming language provides the following types of loops to handle looping requirements. Python provides three ways for executing the loops. While all the ways provide similar basic functionality, they differ in their syntax and condition checking time.
>
- #### ***`While` Loop:***
> 
> In python, while loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.
```python
# Python program to illustrate
# while loop
count = 0
while (count < 3):
	count = count + 1
	print("Hello Zain")
```
- #### ***`For` Loop:***
> The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
```python
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)
```

- #### ***Control Statements:***
> Python provides us with 3 types of Control Statements:
>
> `Continue`
> `Break`
> `Pass`
>
> `break` is used to break out of a loop unconditionally.
> 
> `continue` is used to stop the current iteration of the loop and start the next one.
> 
> `pass` is usually used as a place-holder for actual code so that python interpreter doesn't give an error.

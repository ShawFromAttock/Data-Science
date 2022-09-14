# Modules:
A file containing Python definitions and statements is referred to as a module.  A module is a file that contains Python code; an abc.py file would be a module with the name abc.  We utilise modules to divide complicated programmes into smaller, more manageable pieces. Modules also allow for the reuse of code.  Instead of duplicating their definitions into several applications, we may define our most frequently used functions in a module and import it.

**abc.py**
```python
def temp(name,city):
    result = f("My name is {name}. I live in {city}.")
    print(result)
```
**main.py**
```python
import abc
abc.temp("Zain", "Attock")
```

# Packages:
A package is a folder in python that contains multiple modules. In order for a folder to be recognized as a package, we need to create `__init__.py` file in the folder. Then we can add multiple modules in it. In simpler terms a package is folder that contains various modules as files. 

![alt text](https://www.tutorialsteacher.com/Content/images/python/package.png "Logo Title Text 1")

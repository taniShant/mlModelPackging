# Outlier Package 
### 1.  Makefile-based approach 
#### Builds a sklearn based model pipeline by picking the model defination from a configuration file (defined in model_config.json) and deploy pipeline at runtime 

#### Uses production of wheels using setup.py

Refer json defination at model_config.json

Uses setuptools library (setup.py) to package up our solution

Readme all about the package ...

Inspired by:
* https://towardsdatascience.com/ultimate-setup-for-your-next-python-project-179bda8a7c2c
* https://github.com/MartinHeinz/python-project-blueprint/blob/master/Makefile
* https://stackabuse.com/how-to-write-a-makefile-automating-python-setup-compilation-and-testing/


#### Testing 
Note that if 

```pytest```

does not work, you potentially have to run

```python -m pytest .``` 

in the 'outlier_package' directory. This can be becasue Pytest is not appending to your path correctly.

#### Steps (for using this Makefile-based approach ML model approach )
Create a starter environment.yml
- make create_environment   :- install all lib dependencies listed in environment.yml
- make update_environment   :-Updates the environment, which will create the first lockfile
- make delete_environment   :- deletes conda env 

### 2. A better way : Mange with Poetry (Python dependency management and packaging) 

- Only one configuration file, pyproject.toml ( poetry new my-ML-package )

### 3. Testing 
- use pytest (quite robust) . Looks for files starting with test_ or _test
- refer file test_ detectors.py in my_ml_package/test_ detectors.py

### 4. Analyzing dependencies for security issues 
#### https://pypi.org/ project/safety/ checks against Safety DB
- Safety uses a standardized database containing known Python security issues and then compares any packages found in your solution against this database.  
- For all commercial projects, Safety must be upgraded to use a PyUp API using the key option.

### 4. Logging 
- Log levels 
- In try - exception block logging.error("Unexpected error", exc_info=True)

### 5. Error handling

- try catch - mail (if needed )
- organized in a hierarchy. Raising an exception at a lower level is simply a more specific instance of an exception at a higher level
- can raise exception  raise it at a higher level of the hierarchy and everything still works correctly

BaseException
+-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
...
+-- Warning
...
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning

Strategy (any 1 ) :

1. Log the error but still allow the exception to propagate up the call stack. This can be useful for debugging purposes, as it allows you to log the error message and other details about the exception, while still allowing the calling code to handle the exception as appropriate

2. Add additional context to the exception. For example, I might want to add information about the state of our application when the exception occurred, or about the input that led to the exception being raised.  

3. Want to handle an exception in a higher level of code but still allow lower-level code to handle the exception if it is not appropriate to handle it at the higher level. This is a bit more complex. Eg we can call a function that handles the exception in a bespoke way, say handle_exception:

4. may raise a different exception, perhaps because need to bring together a few different exceptions and deal with them together at a higher level of abstraction.

 
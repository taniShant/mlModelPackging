# Outlier Package 
## Builds a sklearn based pipeline to pick configuratio file (.yml) defined  models and deploy pipeline at runtime

Readme all about the package ...

Inspired by:
* https://towardsdatascience.com/ultimate-setup-for-your-next-python-project-179bda8a7c2c
* https://github.com/MartinHeinz/python-project-blueprint/blob/master/Makefile
* https://stackabuse.com/how-to-write-a-makefile-automating-python-setup-compilation-and-testing/


# Testing
Note that if 

```pytest```

does not work, you potentially have to run

```python -m pytest .``` 

in the 'outlier_package' directory. This can be becasue Pytest is not appending to your path correctly.

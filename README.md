# Outlier Package 
### Builds a sklearn based model pipeline by picking the model defination from a configuration file (defined in model_config.json) and deploy pipeline at runtime 

### Uses production of wheels using setup.py

Refer json defination at model_config.json

Uses setuptools library (setup.py) to package up our solution

Readme all about the package ...

Inspired by:
* https://towardsdatascience.com/ultimate-setup-for-your-next-python-project-179bda8a7c2c
* https://github.com/MartinHeinz/python-project-blueprint/blob/master/Makefile
* https://stackabuse.com/how-to-write-a-makefile-automating-python-setup-compilation-and-testing/


### Testing 
Note that if 

```pytest```

does not work, you potentially have to run

```python -m pytest .``` 

in the 'outlier_package' directory. This can be becasue Pytest is not appending to your path correctly.

### Steps (for using this Makefile-based approach ML model approach )
Create a starter environment.yml
- make create_environment   :- install all lib dependencies listed in environment.yml
- make update_environment   :-Updates the environment, which will create the first lockfile
- make delete_environment   :- deletes conda env 

# a better way : Mange with Poetry (Python dependency management and packaging) 

- Only one configuration file, pyproject.toml ( poetry new my-ML-package )

├── README.md
├── my_ML_package
│   └── __init__.py
├── poetry.lock
├── pyproject.toml
└── tests
    └── __init__.py
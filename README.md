# pytest
##Usage
#### Run all the tests in a file
```
pytest <test_file.py>
```
eg:
```
pytest test_functions.py
```

#### Run a specific test in a file
```
pytest <test_file.py> -k <test_function_name>
```
eg:
```
pytest test_functions.py -k test_post_request
```
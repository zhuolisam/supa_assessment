### How to Use
Install dependencies - pip install -r requirements.txt

Run main file - python main.py

Run test - pytest tests/



### My Own Documentation 
#### Steps Breakdown

1. Prepare data
Seed function is given, we can run seed.py to seed the dataset into a db, simulating a db.

2. Prepare tests
I assume the dates are UTC date.

    * Think of the test case
    * Write pytest tests

3. Implement code

    * The core steps are:
        * extract
        * filter_data
        * sort_data
        * count_consecutive_logins
        * sort_data

#### Features
These are the features I added
* Simulating SQlite as database, can be replaced to other database as well
* Logging
* Unit testing using Pytest
* Github workflows to automate testing

#### Optimization
The tasks looks like a ETL job to me. In the first iteration, I have used pure list and loops iterations to implement the consecutive logins calculate. However, when the data gets larger, loops will be rather slow. Hence, I have used Pandas to implement the function, which has better performance and more built-in data manipulation methods.
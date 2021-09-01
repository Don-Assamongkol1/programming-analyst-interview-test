## Overview

To solve this task, you must use **both** Python and SQL, but feel free to `pip install` whatever library you would like. This task is designed to test your ability to:

- Call REST APIs
- Import and export data as CSVs
- Clean messy data
- Do copy operations in `Pandas` like grouping and joining

Once you have completed the assignment, please email the the Python file(s) and SQL file to paulzakin@bsd.uchicago.edu

### Important

- This task is not restricted in any way. So feel free to use Google, Stack Overflow, textbooks, etc. The only thing you cannot do is ask a friend for help! 

- This task should **not** take you longer than 3 hours. It took that last developer ~ 1 hour to complete it fully. If you exceed three hours, **please stop**. This test is **not** designed to be an all-day assignment. We specifically made a bunch of questions **bonus**.

## Instructions

### Python

1. Using a GET request, pull down appointments.csv and people.csv from these links and convert them into DataFrames:
   
   - [People](https://raw.githubusercontent.com/ipph-development/programming-analyst-interview-test/main/people.csv)
   - [Appointments](https://raw.githubusercontent.com/ipph-development/programming-analyst-interview-test/main/appointments.csv)

2. Replace \n in the address column with a `" "`

3. Extract out the zipcode into a new column called `zipcode` using **regex**. For this test, you can assume that the zipcode will always be a five-digit number. Hint: Pandas has a method called `str.extract`.

4. Bonus: Replace all phone numbers not in this format: `XXX-XXX-XXXX` with the string “INVALID”. For example, 779-477-6793 is valid while 779-477-6793-121 is not.
 
5. Bonus: Replace `weight_in_lbs` below 90 and above 250 with `np.nan`.

6. Bonus: Create a `bmi` column: [formula here](https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html).
   
7. Bonus: Create a `metabolic_syndrome` column which is `True` 
   1. The participant has a `bmi` > 30, 
   2. `has_hypertension` is true
   3. `has_diabetes` is also true
   
8.  Bonus: Create another column, `BMI_by_sex`, which contains the average BMI of each sex. Hint: This will require you to `INNER JOIN` the datasets. Be sure to remove any duplicate `participant_id` from both the person and appointments DataFrame before you do!

9.  Bonus: Export the combined dataset as `combined.csv`.

## Bonus: Python

10. You will working on a simple class hierarchy that has View as a base type which is a simplification of the class-based views OO construct in the Django framework.  Each kind of view offers a bit different functionality, and we can use multiple inheritance in python to compose a new View type from existing ones.  In our case, 
ListView and DetailView extend View
SearchView extends DetailView
SearchResultsView extends ListView and SearchView

Extend the code in the file [views.py](https://raw.githubusercontent.com/ipph-development/programming-analyst-interview-test/main/views.py) to create this class hierarchy. You will not implement any methods, just the hierarchy of classes. The classes will be empty as indiciated by having the *pass* keyword follow the *class* signature declaration. You will not implement any methods.  'views.py` already has driver code to test the class hierarchy.

## Overview

To solve this task, you must use **both** Python and SQL, but feel free to `pip install` whatever library you would like. This task is designed to test your ability to:

- Call REST APIs
- Import and export data as CSVs
- Clean messy data
- Do copy operations in `Pandas` like grouping and joining
- Write SQL

> Important: This task is not timed or “restricted” in any way. So feel free to use Google, Stack Overflow, textbooks, etc. The only thing you cannot do is ask a friend for help! 

## Instructions

### Python

0. Using a GET request, pull down `appointments.csv` and `people.csv` from this [link](https://github.com/ipph-development/programming-analyst-interview-test) 

1. Remove \n from the address column

2. Extract out the zipcode using **regex**

3. “Null out” all phone numbers not in this format: `XXX-XXX-XXXX`. For example, 779-477-6793

4. Remove participants with duplicate `participant_id`.
 
5. “Null out” all `weight_in_lbs` below 90 and above 250

6. Create a `BMI` column: [formula here](https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html)
   
7. Create a `metabolic_syndrome` column which is `True` 
   1. The participant has a BMI > 30, 
   2. `has_hypertension` is true
   3. `has_diabetes` is also true
   
8. Create another column, `BMI_by_sex`, which contains the average BMI of each sex. Hint: This will require you to `INNER JOIN` the datasets 

9.  Export the combined dataset as `combined.csv`.

### SQL

0. Download the `appointments.db` and `people.db` SQLite files from [this link](https://github.com/ipph-development/programming-analyst-interview-test)

Repeat steps #1 through #8, this time using SQL.

10.  Export the combined dataset as `combined.db`
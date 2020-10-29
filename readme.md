## Overview

To solve this task, you must use **both** Python and SQL, but feel free to `pip install` whatever library you would like. This task is designed to test your ability to:

- Call REST APIs
- Import and export data as CSVs
- Clean messy data
- Do copy operations in `Pandas` like grouping and joining
- Write SQL

### Important

- This task is not restricted in any way. So feel free to use Google, Stack Overflow, textbooks, etc. The only thing you cannot do is ask a friend for help! 

- This task should **not** take you longer than 2 hours. It took that last developer ~ 1 hour to complete it fully. If you exceed two hours, **please stop**. This test is **not** designed to be an all-day assignment!

## Instructions

### Python

1. Using a GET request, pull down appointments.csv and people.csv from these links and convert them into DataFrames:
   
   - [People](https://raw.githubusercontent.com/ipph-development/programming-analyst-interview-test/main/people.csv)
   - [Appointments](https://raw.githubusercontent.com/ipph-development/programming-analyst-interview-test/main/appointments.csv)

2. Replace \n in the address column with a `" "`

3. Extract out the zipcode into a new column called `zipcode` using **regex**. For this test, you can assume that the zipcode will always be a five-digit number.

4. Replace all phone numbers not in this format: `XXX-XXX-XXXX` with the string “INVALID”. For example, 779-477-6793 is valid while 779-477-6793-121 is not.
 
5. Replace `weight_in_lbs` below 90 and above 250 with `np.nan`.

6. Create a `bmi` column: [formula here](https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html).
   
7. Create a `metabolic_syndrome` column which is `True` 
   1. The participant has a `bmi` > 30, 
   2. `has_hypertension` is true
   3. `has_diabetes` is also true
   
8.  Create another column, `BMI_by_sex`, which contains the average BMI of each sex. Hint: This will require you to `INNER JOIN` the datasets. Be sure to remove any duplicate `participant_id` from both the person and appointments DataFrame before you do!

9.  Export the combined dataset as `combined.csv`.

### SQL

1. Download the `data.db` file from [this link](https://github.com/ipph-development/programming-analyst-interview-test/blob/main/data.db). This database is simply the combination of the appointments.csv and people.csv you have already worked with above. I recommend exploring and executing SQL against the Sqlite3 dataset using the free GUI [Beekeeper](https://www.beekeeperstudio.io) but the choice is yours.

2. Find the average weight of all `sex assigned at birth` female participants without duplicate `participant_id`. Hint: this will require the use of JOINs and/or subqueries.


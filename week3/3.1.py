#coding: utf-8
import pandas as pd

#first we create two DataFrames with the same index, 'Name'.
# IOW Both dataframes are INDEXED on the value, 'Name' on which we want to merge them.


staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])

student_df = student_df.set_index('Name')

print "STAFF"
print(staff_df.head())
print
print "STUDENTS"
print(student_df.head())
print
print "OUTER MERGE"
print pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
print
print "INNER MERGE"
print pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
print
print "LEFT MERGE" #Collect everyone, but find the students' details as well.
print pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
print
print "RIGHT MERGE"
print pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
print
print "YOU CAN USE COLUMNS AS WELL TO JOIN DATAFRAMES; NOT JUST SHARED INDICES."
print
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
print
print pd.merge(staff_df, student_df, how= 'left', left_on='Name', right_on='Name')
print
print "ADD LOCATION. NOTE: LOCATION_X & LOCATION_Y"
print
print "NOTE: underscore _X is left DataFrame.  underscore _Y is right DataFrame "
print
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

print pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
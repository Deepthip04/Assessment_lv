# -*- coding: utf-8 -*-
"""IA1python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tJnEJ38cAdY9MmNNl2SbpqJ3cWWQOfj5
"""

#1ans
length=float(input('Enter length of the plot in meters:'))
width=float(input('Enter width of the plot in meters:'))
plot_area=length*width
print('The area of the plot is ',plot_area)
if plot_area<2000:
  print('small area')
elif plot_area>2000 and plot_area<4000:
  print('Medium area')
else:
  print('Large area')

#2ans
height=float(input('Enter your height in meters:'))
weight=float(input('Enter your weight in kilograms:'))
BMI=(weight)/(height)**2
if BMI<=40:
  print('you are underweight')
elif BMI>40 and BMI<60:
  print('you are in the right condition')
else:
  print('you are overweight')

#3ans
student_grades={'Deepthi':{'maths':'A','science':'B','social':'A'},
                'priya':{'maths':'B','science':'B','social':'A'}}
#to add a student grades
student_grades['tina']={'maths':'C','science':'B','social':'A'}
#to update a students grade
student_grades['Deepthi']['science']='A'
#to retrieve priya's science grade
print(student_grades['priya']['science'])
print(student_grades)

#4ans
content={'children':{'doraemon','mrbean','shinchan'},'teens':{'natgeo','dicovery','sports'},'adults':{'bhakthi','movies'}}
age=int(input('Please enter your age:'))
if age<18:
  print('your recommended content is :',content['children'])
elif age>18 and age<30:
  print('your recommended content is :',content['teens'])
else:
  print('your recommended content is :',content['children'])

#5ans
subscriber_id=[101,102,103,105,109,110,106,120,122,125]
required_id=[]
for id in subscriber_id:
  if id%2==0:
    required_id.append(id)
print("Even-numbered subscriber id's are",required_id)

#6ans
password='Hello'
user_entered_password=input('Enter password:')
while password!=user_entered_password:
  print('Incorrect password! Try again')
  pass
print('Password matched')

#7ans
survey_data={'Deepthi':{'service':5,'quality':10},'pooja':{'service':8,'quality':5}}
avg_score_for_service=(survey_data['Deepthi']['service']+survey_data['pooja']['service'])/2
avg_score_for_quality=(survey_data['Deepthi']['quality']+survey_data['pooja']['quality'])/2
print(avg_score_for_service)
print(avg_score_for_quality)
if avg_score_for_service>avg_score_for_quality:
  print('Need to improve quality')
else:
  print('Need to improve service')

#8ans
comment=input('Enter a comment:')
count=0
for x in comment:
  if x in ['a','e','i','o','u','A','E','I','O','U']:
    count+=1
print('Total number of vowels in the comment are:',count)

#9ans
import datetime

#10ans
amount=float(input('enter amount deposited:'))
rate_of_interest=float(input('enter rate of interest:'))
time_period=int(input('Enter time in years:'))
try:
  savings_interest=(amount*rate_of_interest*time_period)/100
except ValueError:
  print('Values are wrong')
finally:
  print('savings interest for amount is',savings_interest)

#11ans
voter_id=int(input('please enter your voter_id'))
voter_name=input('Enter your name')
voted_person_id=int(input('Enter the id of person you want to vote:'))
if type(voted_person_id)=='int':
  print('correct info')
else:
  print('wrong info')

#12ans
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
a=int(input('enter first value:'))
b=int(input('enter second value:'))
try:
  res=a/b
except ZeroDivisionError:
  print('Error ocuured!Division not Possible')
finally:
  print('Try again')

#13ans
log_file=open('log_file.txt','w')
daily_status=[]
for x in range(3):
  daily_report=input('Enter your status:')
  daily_status.append(daily_report)
print(log_file.writelines(daily_status))

#14ans
content=open('log_file.txt','r')
print(content)

#15ans
daily_news=open("news.txt",'a')
updates=open("update.txt",'w')
daily_news.append(updates)
content=open("daily_news",'r')
print(content)
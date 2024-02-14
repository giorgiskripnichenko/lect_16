
#----------------- დავალება 15 -----------------
    
# შექმენით csv ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:
# id,name,age,grade,subject_name,marks
# 1,string,0,string,string,0
# 2,string,0,string,string,0
# დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას (id,name,age,grade,subject_name,marks) და თქვენ სტუდენტს დაამატებთ csv ფაილში.
# დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.
# დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს და განახლებულ ქულას.

data = [
    { 
      'id':1,
      'name':'ika',
      'age':23,
      'grade':'economist',
      'subject_name':'fizic',
      'marks':100,
    },
    {
      'id':2,
      'name':'nino',
      'age':25,
      'grade':'economist',
      'subject_name':'math',
      'marks':100,
    }
]

import os,csv
with open ('test1.csv', mode='w',encoding='utf-8',newline='') as file:
    writer = csv.DictWriter(file,delimiter='|',quoting=csv.QUOTE_ALL,fieldnames=list(data[0].keys()))
    writer.writeheader()
    writer.writerows(data)
    file.close()

def addInCsv(data):
  with open ('test1.csv', mode='a',encoding='utf-8',newline='') as file:
    writer = csv.DictWriter(file,delimiter='|',quoting=csv.QUOTE_ALL,fieldnames=list(data[0].keys()))
    writer.writerows( data)
    file.close()

  
def readDromFile(id):
  with open ('test1.csv', mode='r',encoding='utf-8',newline='') as file:
    reader = list(csv.reader(file, delimiter='|'))
    le = 12
    if id == 'all':
      for item in reader:
          print(f'{item[0]:>{le}},{item[1]:>{le}},{item[2]:>{le}},{item[3]:>{le}},{item[4]:>{le}},{item[5]:>{le}}')
      file.close()
    else:
      for item in reader:
          if str(item[0]) == id:
            print(f'{item[0]:>{le}},{item[1]:>{le}},{item[2]:>{le}},{item[3]:>{le}},{item[4]:>{le}},{item[5]:>{le}}')
      file.close()

    

# დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას (id,name,age,grade,subject_name,marks) და თქვენ სტუდენტს დაამატებთ csv ფაილში.

id,name,age,grade,subject_name,marks = input('შეიყვანეთ მონაცემები(გამოყავით მძიმით) id,name,age,grade,subject_name,marks \n ').split(',')   
data = []
dict1 = dict()
dict1['id'] = id
dict1['name'] = name
dict1['age'] = age
dict1['grade'] = grade
dict1['subject_name'] = subject_name
dict1['marks'] = marks
data.append(dict1)
addInCsv(data)

# დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.

idInput = input('შეიყვანეთ ID თუარ შეიყვანთ ფაილის ყველა ინფო დაიბეჭდება \n')
if idInput == '':
   idInput = 'all'
readDromFile(idInput)
      

#/----------------- დავალება 15 -----------------

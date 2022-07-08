students = []
names = []

##############  menu 1
def Menu1(std) :
  students.append(std)
  names.append(x[0])

##############  menu 2
def Menu2() :
  for i in range(0, len(students)):
    if len(students[i]) != 4 :
      grade = (int(students[i][1]) + int(students[i][2])) / 2
      if grade >= 90:
        students[i].append('A')
      elif grade >= 80:
        students[i].append('B') 
      elif grade >= 70:
        students[i].append('C') 
      else:
        students[i].append('D') 

##############  menu 3
def Menu3() :
  print('---------------------------')
  print('name  mid  final  grade')
  print('---------------------------')
  for a,b,c,d in students:
    print(a,'\t',b,'\t',c,'\t',d)
    #출력 코딩

##############  menu 4
def Menu4(std_name):
  for i in range(0, len(students)):
    if std_name in names:
      names.remove(std_name)
      del(students[i])
      print(std_name, 'student inforamation is deleted')
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :  
  choice = input("Choose menu 1, 2, 3, 4, 5 : ")  
  if choice == "1":
    x = input('Enter name mid-score final-score : ').split()
    if len(x) != 3:
      print('Num of data is not 3!')
      continue
    if x[0] in names :
      print("Already exist name!")
      continue
    try:
      if(int(x[1]) <= 0) or (int(x[2]) <= 0):
        raise Exception() 
    except:
      print('Score is not positive integer!')
      continue
    else: Menu1(x)
    
  elif choice == "2" :
      if len(students):
        print('Grading to all students.')
        Menu2()
      else:
        print('No student data!')

  elif choice == "3" :
    flag = True
    if len(students) == 0:
      print('No student data!')
      flag = False 
    for i in range(0, len(students)):
      if (len(students[i])) != 4:
        print('There is a student who didn\'t get grade')
        flag = False
        break
    if flag == True :
      Menu3()
      
  elif choice == "4" :
    if len(students) == 0:
      print('No student data!')
      continue
    name = input('Enter the name to delete : ')
    if name not in names:
      print('Not exist name!')
      continue
    Menu4(name)
      
  elif choice == "5" :
      print('Exit Program!')
      break

  else :
      print('Wrong number. Choose again.')
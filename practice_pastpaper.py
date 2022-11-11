#start=input("How old were you on first day:")
#end=input("how old are you today:")
#print("Congratulations on"+ str(int(end)-int(start)) + "years of service!")

# numlist=[1,2,3,4,5]
# alphalist=['a','b','c','d','e']
# print(numlist is alphalist)
# print(numlist==alphalist)
# numlist = alphalist
# print(numlist is alphalist)
# print(numlist==alphalist)

# employes=['saad','waqas','awais','munawar','israr','shoaib','khan','majid','alex','feroz','bilal','haseeb','jabbar']
# employes.insert(2,'baig')
# print(employes)
# print(employes[:-5])
# print(employes[0:-5])


# import random
# print(random.randint(5,11))
# print(random.randrange(5,13,1))

# i=2
# while (i!=2):
#     continue
# print("hello")

# x='20'
# y=3
# a=x*y
# print(type(a))
# print(a)

# def update_score(current,value):
#     a = current + value
#     return a
# print(update_score(4,5))

# def getname():
#     name=input('your name: ')
#     return name
# def calc_calories(miles,calories_per_miles):
#     calories=miles*calories_per_miles
#     return calories3
# distance =int(input('how many miles this week?'))
# burn_rate=50
# biker = getname()
# calories_burned=calc_calories(distance,burn_rate)
# print(biker,', you have burned about',calories_burned, 'calories')

# def inc_score(score,bonus,points=1):
#     if bonus==True:
#         points = points*2
#     score = score + points
#     return score
# points = 5
# score=10
# new_score=inc_score(score, True, points)
# print(new_score)



# a = 'khan'
# b= 'baig'
# print(a+b)
# b=a
# print(b)

# print('None' is None) #
# print(None is None)
# print (1 is 0)
# print (0 is 0)
# print(0 or 5) # 0 is always consider as false and 5 or any number except 0 is True
# print(0 and 5)
# print(4 or 5)
# print(4 and 5)
# print(bool(-1))
# print(bool(0)) #any non zero is always false

# x=4
# while x >= 1:
#     if x % 4==0:
#         print('Party')
#     elif x-2<0:
#         print('Cake')
#     elif x/3==0:
#         print('Greeting')
#     else:
#         print ('Birthday')
#     x=x-1

# def reverse_name(backward_name):
#     foward_name = ''
#     for index in range(len(backward_name)-1,-1,-1):
#         foward_name+=backward_name[index]
#     return foward_name
# print(reverse_name("daas"))

# x = 4
# while x ==4:
#     valid = False
#     print ('saad')

# employee_number = ""
# parts = ""
# while employee_number =="":
#     valid = False
#     employee_number = input("Enter employee number (ddd-dd-dddd) : ")
#     parts = employee_number.split('-')
#     if len(parts) == 3:
#         if len(parts[0]) == 3 and len(parts[1]) == 2 and len(parts[2]) == 4:
#             if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
#              valid = True
#         print(valid)


# inventory = open("test.txt", 'r')
# eof = False
# while eof == False:
#     line = inventory.readline()
#     if line !='\n':
#         if line !="":
#             print(line)
#         else:
#             print('End of line')
#             eof = True
#             inventory.close()
# x = 20
# y = 4
# a = x / y
# print (a)
# print(type(a))



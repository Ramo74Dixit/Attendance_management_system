#Project
# -------Student database-----------
# Student={1:{'Roll_no':2105051530082,'Name':' Ram MohanDixit','Attendance':80,'Username':'Ramu_123','Password':'123456'},
#         2:{'Roll_no':2105051530080,'Name':'Pryanshu Gupta','Attendance':74,'Username':'pryanshu_123','Password':'123457'},
#         3:{'Roll_no':2105051530081,'Name':'Rahul Pal','Attendance':75,'Username':'rahul_123','Password':'123458'},
#         4:{'Roll_no':2105051530088,'Name':'Rudransh Pratap Singh','Attendance':71,'Username':'rudransh_123','Password':'123459'},
#         5:{'Roll_no':2105051530091,'Name':'Sangram Chauhan','Attendance':85,'Username':'sangram_123','Password':'123460'},
#         6:{'Roll_no':2105051530010,'Name':'Abhi Rathore','Attendance':73,'Username':'abhi_123','Password':'123461'}}
Student={}
count=int(input("kitne hue total admission"))
keys=['Name','Username','Password','Attendance','Rollno']
for i in range(count):
    sub={}
    for x in keys:
        print(x,end='')
        item=input()
        sub[x]=item
    Student[i]=sub
# print(student)
# ----------teacher database----------
Teacher={ 
    1:{'Name':'Mr Atul Kumar Agnihotri','Username':'atulrdx_1234','Password':789456},2:{'Name':'Priyanka Dubey','Username':'priyanka_1234','Password':789456}}
# ---------------------welcome point of code to user--------------------------------------------------
print("----------------------------------------------------------------------------------------------------------")
print('Welcome To Official Portal Of Attendance of Allenhouse Institute of Technology')
# -----------user input to find his type---------------------------------------------------------------
a=int(input("\n\tPress 1 if you are student\n\tPress 2 if your are Teacher\n\t Press 3 if you want to exit"))
# -----------Taking input and matching from database-------------------------------------------
if a==1:
    option=int(input("Press 1 for Sign Up\nPress 12 for Log in \n\t"))
    if option==1:
     print("Hello, New User kindly Enter all proper informations as asked")
     Roll_no=input("Kindly enter your roll no. provided by college")
     Name=input("kindly enter your name")
     Attendance=input("if you are new then write your attendance zero")
     Username=input("kindly Make your ussername at least two letter one underscore and 3 numbers")
     Password=input("Make a 6 number password letters are not allowed only numbers")
    if option==12:
       d=input("Kindly enter your user name")
       for t,s in Student.items():
        if s['Username']==d:
           e=input("Kindly enter your password")
           for A,B in Student.items():
            if B['Password']==e:
                print("------------------------------WELCOME TO OUR ATTENDANCE PORTAL-----------------------------------------------")
                inte=int(input("PRESS 5 IF YOU WANT TO VIEW YOUR ATTENDANCE\n PRESS 6 IF YOU WANT TO EXIT "))
                if inte==5:
                    print("HELLO STUDENT YOUR ATTENDANCE IS :",B['Attendance']) 
                    print("THANK YOU STUDENT FOR VISITING OUR PORTAL ")
                    break
                if inte==6:
                    print("THANK YOU STUDENT, FOR VISITING OUR PORTAL")
                    break
    #     # if e==Student['Roll_no']:
    # print("Hello , your roll no. is", Student['Roll no'])
    # print("your attendance is studnet .attendance")
    # f=input("If you want to exit then Kindly press 3")
    # if f==3:
    #    print("Thank you Student for visiting our portal")
    # # break
if a==2:
    print("Hello Sir\n")
    g=input("Kindly enter your your username")
    for x,y in Teacher.items():
        if y['Username']==g:
            pas=int(input("kindly enter your password"))
            for w,q in Teacher.items():
                if q['Password']==pas:
                    print("--------Welcome sir to Our Portal--------")
                    z=int(input("\n\tPress 1 if you want to View attendance of all students \n\tPress 2 if you want to update attendance\n\tPress 3 if you want to exit"))
                    if z==1:
                        for i,j in Student.items():
                            print("\nUsername :",i)
                            for key in j:
                                print(key + ':',j[key])
                    if z==2:
                        print("Hello Sir")
                        mod=int(input("how much attendance of every student you want to update of any student ")) 
                        up=input("Kindly enter username")
                        for l,m in Student.items():
                            if m['Username']==up:
                                upd=int(m['Attendance']+mod)
                                print(m['Name'],upd)
                    if z==3:
                        print("Thank You For visiting our portal \n")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        break
if a==3:
    print("HAVE A GREAT DAY AHEAD")
    print("THANK YOU FOR VISITING OUR OFFICIAL PORTAL OF ALLENHOUSE INSTITUTE OF TECHNOLOGY")
    print("**********************************************************************************")
    print("--------------------------------COPYRIGHT CLAIM BY ALLENHOUSE INSTITUE OF TECHNOLOGY--------------------------------------------")
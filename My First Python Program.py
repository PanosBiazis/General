#Python 2
print("Hello World")
#this is a comment in python
myVar=60
myVar1="Hello"
myVar=2 #An integer
myVar2=25.54 #A floating point number
myInputVar=input('Enter a number ')
print(myInputVar)
num1=int(input("Enter First number:")) #taking input for first number
num2=int(input("Enter Second number:")) #taking input for second number
sum=num1 + num2     #adding num1 and num2 and storing them in sum
print(sum)      #print sum to the screen
if 5==5:
    print("you successfully learned if statement.")
if 5==3:
    print("you successfully learned if statement.")
else:
    print("Wow!You also learned about else statement.")
if 5==4:
    print("An if statement.Oh!")
elif 4==4:
    print("That's something new.")
elif 4>=9:
    print("Really?")
else:
    print("Not this time")
for num in range(1,11):
    print(num)
range(0,10,2)#range is a step by which the index will change every time the loop executes. by default is 1.range(start,stop,steps)
for num in range(0,1100,100):
    print(num)
for num in range(10):
    print("I'm awesome")
num=0
while(num < 10):
    print(num)
    num=num+1
x=10
print (x*10)
#Download
megethos=int(input("Δώσε το μέθεθος της εγγραφής >"))
time=megethos/20 #MB/sec
print (time)
#Hmeromisthio
imeromisthio=int(input("Δώσε το ημερομίσθιο:"))
misthos=imeromisthio*25
print ("Μισθός=",misthos)
#periferia-emvadon circle
a=float(input('Give the radius of the circle >'))
pi=3.14
periferia=a*2*pi
emvadon=a**2*pi
print('The length of perimeter of the circle is ',periferia)
print('The area of the circle is ',emvadon)
def helloWorld():#def is to declare the function
    print('Hello World')
def addNumbers(num1,num2):
    num1=int(input('Give a number:'))
    num2=int(input('Give another number:'))
    sum=num1+num2
    print('The addition of the two number is ',sum)
    return sum
helloWorld()
addNumbers(num1,num2)
#import is to insert whatever built-in in python fuction you want
import math#math is a module that contains pow and other fuction
math.pow(4,3)#pow() is a fuction to give a number and raised to the power of the second
a=math.floor(4.3)
b=math.floor(10.9)
print (a)
print (b)
a=math.ceil(4.3)
b=math.ceil(10.9)
print (a)
print (b)
#abs() is a built in fuction in python,takes one parameter and returns the absolute value of the value passed
a=abs(10)
b=abs(-10)
print (a)
print (b)
a=math.log(10)
b=math.log(10,9)#logarithm of 10 to the base 9
print (a)
print (b)
a=math.sqrt(9)
b=math.sqrt(16)
print (a)
print (b)
num1='This is a string.'
num2="This is also a string."
num3='''This look somewhat different it is really different you can see multiple lines in this string '''
str="here i am."
str.capitalize()#capitalize() is a function to take the first letter the capitalized and rest small
str="here I Am."
str.count("e")#this function returns the number of occurrences of the substring sprcified as the parameter.e will return 2.
str.count('Am')#will return 1.
a=str.find("h")#to find the position of the letter
print(a)#output is 0 because it starts from 0,so that means the first position!
a=str.find("I")
print(a)
a=str.find("d")#will return -1 because d isn't found in the string
print(a)
str=" "
iter=("I","am","awesome.")
a=str.join(iter)#this function merge strings between strings
print(a)
str="-"
iter=("I","am","awesome.")
a=str.join(iter)#this function merge strings between strings
print(a)
list1=[2,4,5,6,7,2]#this is a listand it can store various type of data like data structures
list2=[4,"hi",6,"Me",78]
print(list1[0])
print(list1[1])
a=list1[1:4]
print(a)
a=list1[0:4]
print(a)
a=list1[0:3]
print(a)
a=list1[:]
print(a)
a=list1[:5]
print(a)
a=list1[2:]
print(a)
list3=[4,55,6,7,8,9,90]
list3[4]=88
list3.append(150)#you can add an extra element 
print(list3)
del list1[3]#you can delete an element
print(list1)
list4=[4,5,6,2,1]
#list4.remove(5)you can delete an element with the same number
print(list4)
list4.remove(5)
tuple1=(2,3,4,5,"Me",8,"C")#tuples are similar with the lists
tuple2=(4,5,6,7,"hi","bye",10)
print(tuple1[0])
print(tuple1[1:4])
#tuples can not be updated or deleted but you can delete the entire tuple
del tuple1
dict1={#dict1 is a dictionary which contains items and keys(strings)
    # 3 items
    'name':'xyz',#name with a value xyz
    'age':25,#age with a value 25
    'hobby':'karate'#hobby with a value karate
    }
print(dict1['age'])
print(dict1)
dict1['name']='Panos'#you can change an existing item
dict1['Profession']='Pilot'#you can add an item
print(dict1)
del dict1['Profession']
print(dict1)
dict1.clear()
print(dict1)
del dict1
#Python 3
print("Hello World")
myVar=60
myVar2="Hello"
myAge=int(input("Give your age >>"))
print(myAge)
#using walrus operator
print(variable:=False)
for num in range(0,101):
    print(num)
#Using lambda function as anonymous function
adder=lambda x,y:x+y
print (adder(1,2))
import math #to import an external python function
math.pow(4,3)
a=math.fabs(10)# fabs() function takes in one parameter and returns its absolute value 
b=math.fabs(-10)
print(a)
print(b)
path= r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/days.txt"#'F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\days.txt'
myFile=open(path,'r')
data1=myFile.read()#to read the whole file
data2=myFile.readline()#to read the line of the file
data3=myFile.readlines()#to read all lines
print(data1)
print(data2)
print(data3)
myFile.close()
myFile=open(path,'a')
myFile.write("Python is amazing.\n")
myFile.close()
import random
print('Random Number 1=>',random.random())
print('Random Number 2=>',random.random())
print(random.randint(3,9))
print(random.randrange(3,9,3))
#shuffle take the content of the list and print it on different place on the list
list5=[5,11,66,22,1]
random.shuffle(list5)
print("Printing shuffled list5",list5)
print(random.choices(list5,weights=(10,20,30,40,50),k=5))
import statistics
scores=[53,0,24,5,6,7,3,12,4,56,7]
a=statistics.mean(scores)
print(a)
b=statistics.median(scores)
print(b)
c=statistics.mode(scores)
print(c)
list_1=[20,40,60,80,100]
list_2=[30,70,90]
print("Low median is of list_1 is ",statistics.median_low(list_1))
print("Low median is of list_2 is ",statistics.median_low(list_2))
print("High median is of list_1 is ",statistics.median_high(list_1))
print("High median is of list_2 is ",statistics.median_high(list_2))
grades=[70,90,50,85,65,83,94]
grades_mean=statistics.mean(grades)
print("variance of data is ",statistics.variance(grades,grades_mean))
grades2=[80,80,80,80,80,80,80]
grades2_mean=statistics.mean(grades2)
print("variance2 of data is ",statistics.variance(grades2,grades2_mean))
stdevgrades=statistics.stdev(grades)
print("The Standard deviation of the list is ",stdevgrades)
import time
current_time=time.time()
print(current_time)
epoch_time=current_time
local_time=time.ctime(epoch_time)
print("The local time is:",local_time)
#try:#executed first in try statement
    #print(language)#Error
#except NameError as e:#to handle the error
    #print("Some error occurred")
language="Python"
try:#executed first in try statement
    print(language)#Error
except NameError as e:#to handle the error
    print("Some error occurred")
#try:
    #code lines
#except:
    #optional break
    #Handling of exeption(if required)
#finally:
    #Code lines...(Always executed)
#try:
    #print(ourVariable)
#except Exception:
    #print("ourVariable is not defined")
#finally:
    #print("Output is printed successfully")
#def print_five_items(data):
#    if len(data) != 5:
#        raise ValueError("The arguement must have five elements")
#    for item in data:
#        print(item)
#print_five_items([5,2])
import re
string="Hello my name is Lyon"
print(re.findall(r"Lyon",string))
string="Hello I live on lane 8 which is near street 42"
print(re.findall(r"\d",string))
#Identifiers
#\d to find decimal digits[0-9].
#\D to find non-decimal digits[^0-9].
#\s to find white space characters like spaces,tabs,non-pritable chaacters.
#\S to find non-space characters.
#\w to find any alphanumeric character.This is the set of all letters and numbers in both lower and uppercase
#\W to find any non-alphanumeric character.
#Modifiers are a set of meta-characters that add more functionality to identifiers.
#'+' is a modifier to get numbers of any length from the string
print(re.findall(r"\d+",string))
if re.search("awesome","Isn't this an awesome view?"):
    print("You are awesome!")
result=re.split(r"s","Awesome")
print (result)
#import mysql.connector
#config = {
#        'user': 'Editor',
#        'password': '6987165039aA@',
#        'host': 'localhost',
#        'port': '3305',
#        'database': 'mysql15'
#    }
#conn = mysql.connector.connect(**config)
#print(conn)
#conn.is_connected()#verify the connection
#cursor=conn.cursor() #return a cursor object.Usng a cursor object,we can execute SQL queries.
#The SQL cursor class instatiates objects that can execute operations such as SQL statements.
#Cursor objects interact with the MySQL server using a MySQLConnection object.
#cursor.close() Using the cursor's close method we can close the cursor object.
#Once we close the cursor object,we cann't execute any SQL statement.
#cursor=conn.cursor()
#cursor.execute("CREATE TABLE People (Name varchar(50),Age int,City varchar(50))")
#cursor.execute("SELECT*FROM mysql15.People") #to view your table (People) on the database (mysql15)
#cursor.execute("INSERT INTO People (Name,Age,City) VALUES ('Jack',26,'Sydney'),('Maxi',32,'New York'),('John',36,'Mexico');") #Insert values to the table
#cursor.execute("CREATE TABLE PROGRAMMINGHUB (category varchar(255),duration varchar(255),level varchar(255))")
#To fetch all rows
#sql_statement="SELECT * FROM PROGRAMMINGHUB"
#cursor.execute(sql_statement)
#output=cursor.fetchall()#to fetch all rows or tuples
#for x in output:
#    print(x)#to fetch all rows
#To update the 3rd row 2nd column
#sql_statement="UPDATE PROGRAMMINGHUB SET duration='90 Hours' where category='Python'"
#cursor.execute(sql_statement)
#conn.commit()#committing the changes you made and save the changes
#sql_query="DELETE FROM PROGRAMMINGHUB where category='Python'"
#cursor.execute(sql_query)
#print("Row(s) deleted successfully!")
#conn.close()#always close the database connection
import tkinter as tk#for graphic User interface(GUI)
win=tk.Tk()#create window
#you can add widgets here
win.geometry("500x200")#the space of the window or frame
b=tk.Button(win,text="Submit")#button widget
b.pack() #using pack() geometry
win.mainloop()#loop the window
root=tk.Tk()
root.geometry("400x400")
label1=tk.Label(root,text="hi,welcome to GUI using Tkinter")#for texting
label1.pack()#generally, placing the widget in the Tkinter frame.
root.mainloop()
root=tk.Tk()
c=tk.Checkbutton(root,text="Python")#check button python
c.pack()
c1=tk.Checkbutton(root,text="C++")#check button c++
c1.pack()
c2=tk.Checkbutton(root,text="C")#check button c
c2.pack()
root.geometry("400x400")
root.mainloop()
class MyClass:#it's a blueprint that contain all data of the objects
    a=20
    b=40
    #default constructor
    def __init__(self) :
        self.py="Welcome to Python!"
    #a method for printing data members
    def print_Py(self):
        print(self.py)
#creating object of the class
obj=MyClass()
#calling the instance method using the object obj
obj.print_Py()
#Accessing variable present inside MyClass
print(MyClass.a)
print(MyClass.b)
class Crow:
    #class attribute
    species="bird"
    #instance attribute
    def __init__(self,name,age):#to initialize the method
        self.name=name
        self.age=age

#instantiate the Crow class
blu=Crow("Blu",10)
woo=Crow("Woo",15)
#access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

#access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))
#The constructor is a method that is called when an object is created.
#This method is defined in the class and can be used to initialize basic variables.
#There are two types of constructors(Parameterized,Non-parameterized).
#definition of the superclass starts here
class Person:
    #initializing the variables
    name=""
    age=0
    #defining constructor
    def __init__(self,personName,personAge):
        self.name=personName
        self.age=personAge

    #defining class methods
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)
    #end of superclass definition

#definition of subclass starts here
class Student(Person):#Person is the superclass and Student is the subclass
    studentId=""

    def __init__(self, studentName, studentAge,studentId):
        Person.__init__(self,studentName,studentAge)#Calling the superclass constructor and sending values of attributes.
        self.studentId=studentId
    
    def getId(self):
        return self.studentId #returns the value of student id 
#end of subclass definition


#Create an object of the superclass
person1=Person("Panos",20)
#call member methods of the objects
person1.showAge()

#Create an object of the subclass
student1=Student("Shaun",22,"102")
print(student1.getId())
student1.showName()

#Overriding is that you can use two methods with the same name but they have different operations
class Animal:
    #properties
        multicellurar=True
        #Eukaryotic means Cells with Nucleus

        eukaryotic=True
        #function breathe
        def breathe(self):
            print("I breath oxygen.")
        #function feed 
        def feed(self):
            print("I eat food.")

class Herbivorous(Animal):
    #function feed
    def feed(self):
        print("I eat only plants.I am vegetarian.")


herbi=Herbivorous()
herbi.feed()
#calling some other function
herbi.breathe()
#A thread is the smallest unit of execution with the independent set of instructions.
#A single process can also have multiple threads.And each thread will do the particular task.
#More than one thread can exist within the same process.
#Within the same process, threads share memory and the state of the process.
#A thread has a starting point,an execution sequence, and a result.
#single threaded one request(thread) at a time
#multi threaded multiple requests(threads) at a time
#The newer threading module provides much more powerful,high-level support for threads.
#This module is used for creating,controlling and managing threads in python.
#threading.activeCount():This returns the number of alive(currently) Thread objects. This is equal to the length of the list that enumerate() returns.
#threading.currentThread():
#This funcion will return the current Thread object, corresponding to the caller's thread of control(which is in the control of the caller currently)
#If the caller's thread of control wasn't created through the threading module(for example the main thread),
#then a dummy thread object with limited functionality is returned.
#treading.enumerate():It'll give you a comlete list of tthread objects that are currently active.
#threading.main_thread():This method returns the main Thread object.
#In normal conditions,the main thread is the thread from which the python interpreter was started.
#threading.stack_size([size]):This method returns the thread stack size utilised when creating new threads.
#The size argument is optional and can be used to set the stack size to be used for creating subsequent threads, and must be 0 or a positive integer (D=default value is 0).
#If changing the thread stack size is unsupported,a RuntimeError is raised.
#If the specified stack size is invalid, a ValueError is raised.
#run():It acts as the entry of the thread.
#start():is used for starting the thread by calling the run()
#isAlive():is used to verify whether the thread is still exeecuting or not
#getName():is used for returning the name of a thread
#setName():is used to set the name of the thread
import threading
#threading.Thread(target=None,name=None,args=())
#target is the callable object to be invoked by the run() method of thread.
#args is the argument tuple for the target invocation.
#def print_hello(num):
#    print("You are an employee",num)
#t1=threading.Thread(target=print_hello,args=(10))
#t1.start()
#t1.join()#we ensure that the main program halts execution of the main thread and waits until the completion of thread t1.
#Once t1 has completed its activity,the main thread (main program) can continue its execution.
#print("End")
def print_one():
    for i in range(2):
        print(1)
def print_two():
    for i in range(2):
        print(2)
if __name__=="__main__":
    #create threads
    t1=threading.Thread(target=print_one)
    t2=threading.Thread(target=print_two)


    #start thread 1
    t1.start()
    #start thread 2
    t2.start()
    #wait until thread 1 is completely executed

    t1.join()
    #wait until thread 2 is completely executed

    t2.join()
    #both threads completely executed
    print("Completed!")
print("Hello World")
myinteger=120
myinteger2=25.725
print(myinteger)
print(myinteger2)
myInput=input("Give a number:")
print(myInput)
myInput2=input("Write something>>")
print(myInput2)
def myAddition(num1,num2):
    num1=int(input("Give a number:"))
    num2=int(input("Give another number:"))
    result=num1+num2
    print("The Addition is ",result)
    return result
myAddition(num1,num2)
list3=["START","",5,"punk","pop","rock","juzz"]
print(list3[0])
win2=tk.Tk()
win2.geometry("1920x1080")
win2.title("Ending")
win2.configure(bg="orange")#set background color to orange
label2=tk.Label(win2,text="If you want to see what's comming next,Open the ML.py")#for texting
button1=tk.Button(win2,text="Next",command=win2.destroy)#button widget for closing window
button1.pack(side=tk.RIGHT)#place the button in the frame
label2.pack()#generally, placing the widget in the Tkinter frame.
win2.mainloop()#loop the window so that it keeps running and listens for events from user or system
#win2=tk.Tk()#create window object win2
#win2.title("ML.py")#give title of the window
#frame = tk.Frame(win2)#frame object inside the main window
#frame.pack()#place the frame in the main window
#button1 = tk.Button(frame,text="Next",command=win2.destroy)#button widget
#button1.pack(side=tk.LEFT)#place the button in the frame
#win2.mainloop()

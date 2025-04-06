print("test")

io.write("Hello world,from ",_VERSION,"!\n\a")

io.write(
    "Hello world,from ",_VERSION,"!","\n","\a"
)

--[[my first program in lua --]]

-- print("test")

-- Identifiers

-- A Lua identifier is a name used to identify a variable, 
-- function, or any other user-defined item. 

-- An identifier starts with a letter ‘A to Z’ or ‘a to z’ or an 

-- underscore ‘_’ followed by zero or more letters, underscores, 
-- and digits (0 to 9). 

-- Lua does not allow punctuation characters such as @, $, and 
-- % within identifiers. 

-- Lua is a case sensitive programming language. 

-- Thus 'Programming' and 'programming' are two different 
-- identifiers in Lua

local i,j,d,f

d,f,j=5,10,-10

i=j+d*f

print(i)

--Variable definition:

local a,b

--Variable initialization:
a=10

b=30

--Variable assignment:
print("value of a:",a)

print("value of b:",b)

--Variable swap:

b,a=a,b

print("value of a:",a)

print("value of b:",b)

f=70.0/3.0

print("value of f:",f)

-- Lua is a dynamically typed language. 
-- The variables don't have types, only the values have types. 

-- Values can be stored in variables, passed as parameters 
-- and returned as results. 

-- In Lua, though we don't have variable data types, we have 
-- types for the values.

print(type("What is my type")) -->string 

local t=10

print(type(5.8*t)) -->number


print(type(true))-->boolean

print(type(nil))--nil

print(type(type(type(type(type(type))))))-->string

print(type(print))-->function

print(type(type))-->function



--local variable definition
a=100;

--check the boolean condition

if(a<20)
then
   print("a is less than 20")
else
   print("a is greater than 20")
end

print("value of a is :",a)

--local variable definition
a=100;
b=200;

--check the boolean condition
if(a==100)
then
   if (b==200)
   then
      print("a is 100 and b is 200")
   end
end

print("value of a is :",a)

print("value of b is :",b)

a=10
--while loop 
while (a<=20)
do
   print("value of a:",a)
   a=a+1
end

a=10
--repeat loop 
repeat
   print("value of a:",a)
   a=a+1
until(a>15)


--for loop 

for i=10,1,-1
do
   print("value of i:",i)
end


for i=10,20
do
   print("value of i:",i)
end

local bool=true

local count=0

while(bool) 
do
   print("value of counter is :",count)
   count=count+1
   if(count==100)
   then
      print("value of counter is :",count)
      bool=false
   end
end

-- A function is a group of statements that together perform a task

--    You can divide up your code into many different functions. 
   
--    How you divide up your code among different functions is up 
--    to you, 
   
--    but logically the division, usually unique, is so each function 
--    performs a specific task.

local function max(num1,num2,result,result2)
   if(num1> num2)
   then
     result=num1
     result2=num2
     io.write("the maximum of the two numbers is "..result.."\n")
     io.write("the minimum of the two numbers is "..result2.."\n")
   else
     result=num2
     result2=num1
     io.write("the maximum of the two numbers is "..result.."\n")
     io.write("the minimum of the two numbers is "..result2.."\n")
   end
   return result,result2
end

-- If a function uses arguments, 

--    it must declare the variables that accept the values of the 
--    arguments. 
   
--    These variables are called the formal parameters of the 
--    function. 
   
--    The formal parameters behave like other local variables 
--    inside the function. 
   
--    They are created upon entry into the function and destroyed 
--    upon exit. 
   
--    These are some most important points you should 
--    remember while you use Function Arguments.

local num1,num2,result,result2

io.write("Write a number >> ")

num1=io.read()

io.write("Write another number >> ")

num2=io.read()

local maxofnum=max(num1,num2,result,result2)

print(maxofnum)

-- String is a sequence of characters. 

-- String can be initialized with three forms which includes - 

-- * Characters between single quotes 

-- * Characters between double quotes 

-- * Characters between [[ and ]]

local string1="Lua"

local string2='Tutorial'

local string3=[["Lua tutorial"]]

print("\"String 1 is\"",string1)

print("\"String 2 is\"",string2)

print("String 3 is",string3)

-- Many methods can be used to manipulate Strings. 

-- Let's discuss some of those 
-- * string.upper(argument) 

-- Returns a capitalized representation of the argument.

-- ¢ string.lower(argument) 
-- Returns a lower case representation of the argument. 
-- ¢ string.gsub(mainString,findString,replaceString) 

-- Returns a string by replacing occurrences of findString with 
-- replaceString. 

--¢ string.find(mainString,findString,optionalStartIndex,optio 
-- nalEndIndex) 

-- Returns the start index and end index of the findString in the 
-- main string and nil if not found.

-- ¢ string.reverse(arg) 

-- Returns a string by reversing the characters of the passed 
-- string. 

-- ¢ string.format(...) 
-- Returns a formatted string. 
-- ¢ string.char(arg) and string.byte(arg) 

-- Returns internal numeric and character representations of 
-- input argument.

-- ¢ string.len(arg) 
-- Returns a length of the passed string. 
-- ¢ string.rep(string, n)) 

-- Returns a string by repeating the same string n number 

-- ¢  ..

-- This operator concatenates two strings.


-- Arrays are an ordered arrangement of objects. 

-- They may be a one-dimensional array containing a 
-- collection of rows, 

-- or a multi-dimensional array containing multiple rows and 
-- columns. 

-- In Lua, arrays are implemented using indexing tables with 
-- integers. 

-- The size of an array is not fixed. 

-- It can change based on our requirements, subject to memory 
-- constraints.


-- Single Dimensional Array
local array = {"Lua","Tutorial"}

for i=0,2 
do
   print(array[i])
end

-- Multi-Dimensional Array 

-- Multi-dimensional arrays can be implemented in two ways. 

-- * Array of arrays 

-- + Single dimensional array by manipulating indices 

-- Let's see an example.

local array2={}

for i=1,3
do
   array2[i]={}
   for j=1,3
   do
      array2[i][j]=i*j
   end
end

--Accessing the array

for i=1,3
do
   for j=1,3
   do
      print(array2[i][j])
   end
end


-- Iterator is a construct that enables you to traverse through 
-- the elements of the collection or container. 

-- In Lua, these collections often refer to tables, which are used 
-- to create various data structures like arrays. 

-- A generic for iterator provides the key value pairs of each 
-- element in the collection.

local array3={"Lua","Tutorial"}

for key,value in ipairs(array3)
do
   print(key..":"..value)
end

-- The above example uses the default ipairs iterator function 
--    provided by Lua. 
   
--    In Lua we use functions to represent iterators. 
   
--    Based on the state maintenance in these iterator functions, 
--    we have two main types - 
   
--    + Stateless Iterators 
   
--    + Stateful Iterators


--Stateless Iterators

local function square(iteratorMaxCount,currentNumber)
   if (currentNumber < iteratorMaxCount)
   then
      currentNumber = currentNumber + 1
      return currentNumber, currentNumber * currentNumber
   end
end


for i, n in square, 3, 0
do
   io.write(i, n.."\n")
end

--Stateful Iterators

-- The previous example of iteration using function does not 
--    retain the state. 
   
--    Each time the function is called, it returns the next element 
--    of the collection based on a second variable sent to the 
--    function. 
   
--    To hold the state of the current element, closures are used. 
   
--    Closure retains variable values across functions calls.

local array4={"Lua","Tutorial"}

local function elementIterator(collection)
   local index = 0
   local count = #collection
   -- Return the iterator function
   return function()
      index = index + 1
      if index <= count
      then
         return collection[index]
      end
   end
end

for element in elementIterator(array4)
do
   print(element)
end

-- I/O library is used for reading and manipulating files in Lua. 

-- There are two kinds of file operations in Lua namely, 

-- ¢ Implicit file descriptors 

-- ¢ Explicit file descriptors 

-- For the following examples, we will use a sample file test.lua 
-- as shown below. 

-- -- sample test.lua 
-- -- sample2 test.lua 

-- A simple file open operation uses the following statement. 

-- file = io.open (filename [, mode])


-- "r" 

-- Read-only mode and is the default mode where an existing 
-- file is opened. 

-- "w" 

-- Write enabled mode that overwrites the existing file or 
-- creates a new file.

-- "a"

-- Append mode that opens an existing file or creates a new 
-- file for appending. 

-- "r+" 

-- Read and write mode for an existing file.

-- "w+" 
-- All existing data is removed if a file exists or a new file is 
-- created with read write permissions. 

-- "a+" 

-- Append mode with read mode enabled that opens an 
-- existing file or creates a new file.


--Implicit File Descriptors

-- Implicit file descriptors use the standard input/ output 
-- modes. 

-- Or using a single input and single output file. 

-- When you run the program, you will get an output of the first 
-- line of test.lua file.

--Opens a file in read
local file=io.open("test.lua","r")

if file 
then

--sets the default input file as test.lua
io.input(file)

--prints the first line of test.lua
print(io.read())

--closes the file
io.close(file)

end
--Opens a file in Append mode
local file2=io.open("test2.lua","a")

if file2 
then

--sets the default output file as test.lua
io.output(file2)

--appends a word test to the last line of the file
io.write("--End of the test.lua file")

--closes the file
io.close(file2)

end

--Opens a file in read
local file3=io.open("test.lua","r")

if file3 then
   local line = file3:read()
   --prints the first line of the file
   -- print(file3.read())
   print(line)
   
   --close the open file
   file3:close()
end





--Opens a fle in append mode

local file4=io.open("test.lua","a")

if file4
then
   --appends a word test to the last line of the file
   -- file4.write("--test")
   file4:write("--test")

   --close the open file
   file4:close()

end


-- Other common file methods includes, 

--  file:seek(optional whence, optional offset) - Whence 
-- parameter is "set", "cur" or "end". 

-- It sets the new file pointer with the updated file position 
-- from the beginning of the file. 

-- The offsets are zero-based in this function. 

-- The offset is measured from the beginning of the file if the 
-- first argument is "set"; 

-- from the current position in the file if it's "cur"; 

-- or from the end of the file if it's "end". 

-- The default argument values are "cur" and 0, so the current 
-- file position can be obtained by calling this function without 
-- arguments. 

-- ¢ file:flush() — Clears the default output buffer. 

-- ¢io.lines(optional file name) — Provides a generic for loop 
-- iterator that loops through the file and closes the file in 
-- the end.


-- Problem 
-- Occurs 

-- + 

-- Create 
-- Exception 

-- + 
-- Throw 
-- Exception 
-- + 

-- Handle 
-- Exception 

  

-- Exceptions are run-time anomalies. 

-- They are abnormal conditions that a program encounters 
-- during its execution. 

-- There are two types of exceptions: 

-- * Synchronous 

-- „ Asynchronous (Ex:which are beyond the program's 
-- control, Disc failure etc).

-- Above given is an example of an error 
-- Error handling is quite critical in real-world operations. 

-- It requires the use of complex operations, which includes file 
-- operations, database transactions and web service calls. 

-- There is always a requirement for error handling. 

-- Errors can be of two types which includes, 

-- * Syntax errors 

-- * Runtime errors


-- Syntax Errors 

-- Syntax errors occur due to wrong use of various program 
-- components like operators and expressions. 

-- A simple example for syntax error is shown below. 
-- [ee 

-- As you know, there is a difference between the use of a 
-- single "equal to" and double "equal to". 

-- Using one instead of the other can lead to an error. 
-- One "equal to" refers to assignment. 
-- A double "equal to" refers to comparison. 

-- Let's see an example

-- for a= 1,10 

--    Print(a) 
-- end 

  

-- When we run the above program, we will get the following 
-- output — 

-- Output 
-- lua: test2.lua:2: 'do' expected near 'print' 

-- Syntax errors are much easier to handle than run time errors. 

-- The Lua interpreter locates the error more clearly than in 
-- case of runtime error. 


-- Run Time Errors 

-- function add(a,b) 
-- return a+b 
-- end 

-- add(10) 

  

-- In case of runtime errors, the program executes successfully, 

-- But it can result in runtime errors due to mistakes in input or 
-- mishandled functions. 

-- A simple example to show run time error is shown below. 

-- When we build the program, it will build successfully and 
-- run. 

-- Once it runs, shows a runtime error. 

-- Output 

-- lua: test2.lua:2: attempt to perform arithmetic on local 'b' (a nil 
-- value) 
-- stack traceback: 

-- test2.lua:2: in function 'add' 

-- test2.lua:5: in main chunk 

-- [C]: ?

--lua luapl.lua
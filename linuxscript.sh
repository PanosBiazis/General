#!/bin/bash
# Author: [Panos Biazis]
# . "/media/panos/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/linuxscript.sh"
# chmod +x "/media/panos/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/linuxscript.sh"
# clear

echo "Hello World!"

for i in {1..5}; do
echo "Iteration $i"
done

echo "Goodbye World!"

var="Hello"

echo $var


num=10

echo $num

# Create a variable
greeting="Hello, World!"

# Access the variable
echo $greeting

# Create another variable
name="Alice"

# Use both variables
echo "$greeting My name is $name."

# Define a variable
number=10

# Check the condition
if [ $number -eq 10 ]; then
    echo "The number is 10."
else
    echo "The number is not 10."
fi

setterm --foreground red --background green --cursor on --clear # Set the terminal to red text on green background and turn on cursor and clear screen


# For loop example
for i in {1..5}; do
    echo "Iteration number: $i"
done

# While loop example
count=1
while [ $count -le 5 ]; do
    echo "Count is: $count"
    ((count++)) # Increment the count
done

# Define a function
greet() {
    echo "Hello, $1!"
}

# Call the function with an argument
greet "World"


# Start a Wayland application
# gtk3-demo &



# name="null"

echo "Give your name: "

read name

echo "Your name is: $name"

echo -n "Give a number: " # -n means do not print a newline

read number

echo "You gave the number: $number"

# echo "$name"

# exit 0
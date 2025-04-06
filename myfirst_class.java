/**
 *
 * 
 */

package myJavaproject;

import java.util.Scanner;

import myJavaproject.myfirst_class.Student1;

//import java.util.*; to import all classes of a package
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
/**
 * 
 */

class myAccount {
	private String name;//screenshot variable

	public void setName(String name){
		this.name=name;
	}

	public String getName(){
		return name;
	}
}//end myAccount class

class Phone{
	String name;
	String ID;
	public Phone(String newName, String newID){
		this.name=newName;
		this.ID=newID;
	}
	void disPhone(){
		System.out.println("Name of the phone: "+name+ " ID code: "+ID);
	}
}

class SmartPhone extends Phone{
	String smartname;
	String smartID;
	public SmartPhone(String newName, String newID,String newSmartName,String newSmartID) {
		super(newName, newID);
		this.smartname=newSmartName;
		this.smartID=newSmartID;
	}

	void disSPhone(){
		System.out.println("Name of the smartphone: "+smartname+ " SmartID code: "+smartID);
	}
	
}


class Car{
	String Colour="White";
}

/*class ThisClass{
	//Access control modifiers are keywords which are used to restrict  the scope of the class,data members,methods or constructors.
	int myNumber2=10;//default access control modifier,accessible in the same package
	public int thisNum=10;//accessible everywhere
	private int myNumber=20;//accessible in the same class
	protected int Mynumber=55;//accessible only using inheritance and it can be accessed of all packages
}*/

class LearningConstructor {
  String name;
  String type;

  public LearningConstructor(String newName, String newType) {
    System.out.println("Hi! I am a constructor :D");
    this.name = newName;
    this.type = newType;
  }
  void display(){
	System.out.println("Name:"+name+ "Type:"+type);
  }
}

class AnotherClass {
	public void add(int num1,int num2){
		System.out.println(num1+num2);
	}
}

/**
 * ParentClass
 */
class ParentClass {
	public void oldMethod(){//overriding
		System.out.println("Parents rock.");
	}
	
}

/**
 *  ChildClass
 */
class  ChildClass extends ParentClass {//inheritance
	public void oldMethod(){//overriding
		System.out.println("Children rock.");
	}
	
}
//File:Student.java
class Student implements Student1 {//interface
	private String name; //private data members
	private int roll_no;
	public void setName(String newName){
		//public methods
		name=newName;
	}

	public void setRollNo(int roll){
		roll_no=roll;
	}

	public void dispName(){
		System.out.println(name);
	}

	public void dispRoll(){
		System.out.println(roll_no);
	}
	
public interface Student1{
	public void dispName();
	public void dispRoll();
}

}

//File:myfirst_class.java
public class myfirst_class extends AnotherClass{//inheritance

	/**
		 * 
		 */
	public interface Student1 {//interface

	}

	/**
	 * 
	 */
	public myfirst_class() {
		
	}

	/**
	 * @param args
	 */
	
	public static void hello() {
		System.out.println("hello");
	}
	
	public static int sum(int num1,int num2) {
		return num1 + num2;
	}

	public static void dontOverloadMe(){//Overloading
		System.out.println("Please,don't.");
	}

	public static void dontOverloadMe(String laugh){//Overloading
		System.out.println("Oops! Couldn't hold it for long. "+laugh);
	}

	static void div(int num){
		if(num == 0)
		throw new ArithmeticException("Division by 0.");
		else
		System.out.println(20/num);
	}
	
	public static void main(String[] args) {
		System.out.println("HI WORLD");/* hi
		wow*/
		// wow again
		System.out.println("Hi world again");
		System.out.print("Welcome to ");
		System.out.println("Java programming");
		int score=100;
		String name="James";
		boolean decision=true;
		System.out.println(score);
		System.out.println(name);
		System.out.println(decision);
		int scoreplus=200;
		int Add;
		Add=score+scoreplus;
		score=3*score;
		System.out.println(Add);
		if (Add > score) {
			System.out.println(Add);
		}
		if (Add < score) {
			System.out.println(score);
		}
		if (Add == score) {
			System.out.println(score);
			System.out.println(Add);
		}
		else {
			System.out.println(score);
		}
		for (int i=1;i<6;i++) {
			System.out.println("Times executed:"+i);
		}
		int i=1;
		do {
			System.out.println(i+" Times run");
			i=i+1;
		}while(i<6);
		while (i<12) {
			System.out.println(i);
			i++;
		}
		int numberArray[]=new int[10];
		String stringArray[]=new String[10];
		numberArray[0]=100;
		numberArray[1]=101;
		numberArray[2]=numberArray[0]+numberArray[1];
		System.out.print("Give a number:");
		Scanner sc=new Scanner(System.in);
		numberArray[3]=sc.nextInt();
		System.out.println(numberArray[3]);
		System.out.print("Write something:");
		Scanner character=new Scanner(System.in);
		stringArray[0]=character.next();
		System.out.println(stringArray[0]);
		Car objectMercedes=new Car();
		System.out.println(objectMercedes.Colour);
		hello();
		int add=sum(2,4);
		int add2=sum(3,6);
		System.out.println(add);
		System.out.println(add2);
		//Constructor is a method which has the same name as the class
		LearningConstructor learning1 = new LearningConstructor("Hi ", "Default");
		learning1.display();
		/*Inheritance is when a class derives some properties from another class.
		Just like human beings inherit features from their parents.
		The class which inherits the properties is known as child class.
		And the class from which the properties are inherited is known as the parent class.
		To inherit properties of a class,extends keyword is used.
		class ParentClass{
			body
		}
		class ChildClass extends ParentClass{
			body
		}
		A child class inherits all the members of the parent class
		An object created of type child class can be used to access all the members of the parent class.
		The constructr is never inherited.*/
		myfirst_class obj1=new myfirst_class();//obj1 of type myfirst_class
		obj1.add(3,5);//Calling add method inherited from AnotherClass
		/* Overloading is when two or more methods in a class have same name.
		 * But have different parameters.
		 * The parameters can differ with respect to the number of parameters or type.
		 * Overloading prevent us writing multiple methods which perform the same task.
		 * We can overload the methods and manipulate the type of parameters that they accept.
		 */
		dontOverloadMe();
		dontOverloadMe("HaHaHaHa");
		/*Overriding is when two or more methods in separate classes having child-parent relationship have the same name.
		 *And also same parameters.
		 *But,the two methods aren't written in the same class.
		 *The methods which overrides the previous one is written in a child class.
		 *This enables us to provide specifications while implementing the same function in a child class.
		 *It is important to note that overriding takes place when method declared in the parent class is rewritten in a child class with same parameters.
		 */
		ParentClass obj2=new ChildClass();
		obj2.oldMethod();
		//calling method oldMethod
		//In OOP(Object Oriented Programming),polymorphism is a way to perform a single action in different ways.
		/*In Java,polymorphism can be viewed as the capability of methods to do different things based on the object that it is acting upon.
		 * Method overloading falls into polymorphism.
		 * As it allows us to define a thing and use it in different manners.
		 * Method overriding also allows us to use the same method in defferent ways.
		 * Thus,Method overriding falls into polymorphism.
		 * Polymorphism is of two types (Static,Dynamic)
		 * Static polymorphism also known as compile-time polymorphism is achieved through method overloading.
		 * At compile time,Java knows which method to invoke by checking the method signatures thus it's known as compile time polymorphism.
		 * Whereas dynamic polymorphism or run time polymorphism is achieved through method overriding.
		 * In case of method overriding the method to call is determined at runtime,thus it is known as runtime or dynamic polymorphism.
		 */
		/*Abstraction is a process of hiding the implementation details from the user and providing only the functionality.
		 * In other words,it's a process of hiding background details and focusing on the essential details.
		 * In java,abstraction can be achieved using interfaces and abstract classes
		 * public abstract class ClassName{
		 * 		Members
		 * }
		 * 
		 * public class Anyclass extends ClassName{
		 * 		Members
		 * }
		 * 
		 * An abstract method is a method which only has the declaration of the method no body.
		 * To declare an abstract method public abstract returnType methodName();
		*/
		/*Encapsulation is concept in OOP which describes the idea of bundling variables and methods together.
		 * It brings the idea of data hiding to the table.
		 * The variables in the class can only be accessed through the methods declared inside the class.
		 * The variables are declared as private and methods to access them as public so that they can be accessed from outside the class.
		 * Then only these methods can be used to set or get the values of the variables.
		 * Encapsulation provides a protected space for data members and restricts access outside the class. 
		 */
		Student obj3=new Student();
		obj3.setName("Rocket");
		//Calling method setName
		obj3.dispName();
		obj3.setRollNo(30);
		/*Interface acts as a reference for the other classes.
		 * An interface is a collection of abstract methods and constants.
		 * These methods and constants can be used by classes implementing the interface.
		 * Interfaces're used to  achieve coplete abstraction.
		 * Also,interfaces can be used to achieve multiple inheritance in java,which is not possible otherwise.
		 * To decare an interface ,the keyword interface is used.
		 * public interface InterfaceName{
		 * 		Members
		 * }
		 * An interface is abstract,there isn't need to use the abstract keyword to declare the interface.
		 * Also,the methods declared inide the interface don't need the keyword abstract.They're abstract by default.
		 * And the methods in an interface are public by default.
		 * 
		 */
		obj3.dispRoll();
		/*To use the interface we have defined we need to implement it
		 * Interfaces're implemented and not extended
		 * We use the keyword implements to do so.
		 * A class can implement more than one interface at a time
		 * public class ClassName implements InterfaceName{
		 * 		Member definitions
		 * }
		 */
		/*Library is a place which contains tons of books and resourceswhich we can go and access.
		 * Package in java is a groop of similar types of classes,interfaces and sub-packages.
		 * Packages allow us to maintain our code and improves efficiency by promoting reusability.
		 * A class once writtten in a package can be used repeatedly, there's no need to write the same class again.
		 * To use a package we use the keyword import.
		 * import
		 * packageName.subPackageName.className;
		 * There're two types of packages(Built-in,User-defined) 
		 * built-in packages:
		 * java.util:contains classes related to time,scanner,array manipulation,data-structures, etc.
		 * java.io:contains classes required for input/output operations.
		 * java.lang:contains classes which are fundamental to the design of java language like object.
		 * java.awt:contains the common GUI elements.
		 */
		/*package cartoon;
		 * 
		 * public class Tom{
		 * 		body
		 * }
		 * 
		 * Now,if we want to access the class Tom present in the package cartoon,we can write 
		 * import cartoon.Tom;
		 * And then go on to access the methods and variables of the class TOM like the way we usually do.
		 */
		/* Ther're two types of exceptions (Checked,Unchecked)
		 * A checked exception is an exception which occurs at compile time,these are also known as compile time exceptions.
		 * An unchecked exception is an exception which occurs at the time of execution,these are also known as runtime exception.
		 * Logical errors or programming bugs come under unchecked exceptions.
		 * Errors aren't exceptions.
		 * In programming,errors are something which is out of user's control or programmer's control and cannot be handle like exceptions.
		 * Try,catch and finally are used to handle exceptions in java.
		 * The try block is used to enclose the block of code which might throw an exception.
		 * The try block is always followed by catch or finally block.
		 * The catch block is used to handle the exception.
		 * It's always used after a try block.
		 * There can be multiple catch blocks followed by a try block.
		 * try{
		 * code
		 * }
		 * 
		 * catch(exception_name e){
		 * 		catch block
		 * }
		 * In Java,finally block always follows a try or catch block.
		 * This is the block of code which is executed irrespective of whether the execution is handled or not.
		 * try{
		 * 	try block
		 * }
		 * 
		 * finally{
		 * 		finally block
		 * }
		*/
		try{
			int a=10/0;
			System.out.println(a);
		}
		catch(Exception e){
			System.out.println(e);
		}
		finally{
			System.out.println("Division by zero.");
		}
		/*
		 * The throw keyword is used to explicitly throw an exception.
		 * The syntax of the throw exception
		 * throw new exception;
		 */
		div(5);
		/*
		 * Java allows  us to perform operations on files.
		 * We can read contents of a file and even write some content to the file through a java program.
		 * we need to import java.io
		 * CREATE A FILE
		 * createNewFile() method returns a boolean value which tells whether the file was successfully created or not.
		 */
		File file=new File("lazyMe.txt");//instantiating new object
		try{
			boolean NewFile=file.createNewFile();//create new file
			System.out.println("Successful?"+NewFile);
		}

		catch(Exception e){
			System.out.println("Oops! Some problem occured.");
		}
		/*WRITE A FILE
		 * FileWriter-It can be used to write int and string to the file.It is preferred when the number of writes is less.
		 * BufferedWriter-It uses a buffer to write into files.It is used in case the number of writes is more.It improves the performance.
		 * FileOutputSteam-FileWriter and BufferedWriter are used to write text to files.FileOtStream is used to write raw data to the files.
		 */
		FileOutputStream writeFile=null;
		String myText="Let's write something in this file.";
		try{
			file=new File("lazyMe.txt");//new File object
			writeFile=new FileOutputStream(file);//FileOutputstream object
			byte[] byteData=myText.getBytes();//string to bytes conversion
			writeFile.write(byteData);//writing converted byteData to file
			System.out.println("Successful.");
		}
		catch(IOException ioe){
			System.out.println("OOPs!There was some problem.");
		}
		/*Reading a file
		 * The contents of a file can be read using FileInputStream and BufferedReader.
		 * read() method is used to read the contents of file character by character.
		 */
		try{
			FileInputStream myFile=new FileInputStream("lazyMe.txt");
			int j=0;
			while((j=myFile.read())!=-1){
				//reading every character
				System.out.println((char)j);//printing to the screen
			}
			myFile.close();//closes the file after reading
		}
		catch(Exception e){
			System.out.println(e);
		}
		/*Deleting a file
		 * delete() method of File class is used to do so.
		 * delete() method returns a boolean value based on whether the file was deleted or not.
		 */
		file=new File("lazyMe.txt");//file to be deleted
		boolean deleteMe=file.delete();//delete method
		System.out.println("Deleted?"+deleteMe);
		Phone objPhone=new Phone("Universe v0","vo1023");
		objPhone.disPhone();
		SmartPhone objSPhone=new SmartPhone("Universe v1","000143SAFEW","V1 ULTRA","001V1UDT");
		objSPhone.disSPhone();
		System.out.println("Welcome to java Programming again.");
		//comment
		/*comment but you can write in multiple lines */
		System.out.print("Well  done!\n");
		System.out.println("\"in quotes\""); //print "in quotes"
		System.out.println("\t");
		System.out.println("\r");
		System.out.println("\\");
		System.out.printf("%s%%n%s%n", "Welcome to", "Java programming!");
		Scanner input = new Scanner(System.in);
		int number1;
		int number2;
		int sum;
		System.out.println("Enter first number: ");
		number1 = input.nextInt();//reads the first number from user
		System.out.println("Enter second number: ");
		number2 =  input.nextInt();//reads the second number from user
		sum = number1 + number2;//adds both numbers
		System.out.println("The sum is "+ sum);//prints the result
		System.out.printf("Sum is %d%n", sum);//prints the result using printf function
		//input.close();//closes the scanner object
		if (number1 == number2)
		System.out.println(number1+" and "+number2+" are equal.");
		System.out.println("or");
		System.out.printf("%d == %d%n", number1, number2);
		if (number1 != number2) 
		System.out.printf("Number one is %d and Number two is %d.", number1, number2);
		if (number1 < number2)
		System.out.printf("Number one is smaller than Number two.\n");
		if (number1 > number2)
		System.out.printf("Number one is greater than Number two.\n");
		if (number1 >= number2) 
		System.out.printf("Number one is greater or equal to Number two.\n");
		if (number1 <= number2) 
		System.out.printf("Number one is smaller or equal to Number two.\n");	
		/*
		
		 */
		System.out.println("* * * * * * * * * * * * *");
		System.out.println(" * * * * * * * * * * * * ");
		System.out.println("* * * * * * * * * * * * *");
		System.out.println(" * * * * * * * * * * * * ");
		System.out.println("* * * * * * * * * * * * *");
		System.out.println(" * * * * * * * * * * * * ");
		System.out.println("* * * * * * * * * * * * *");
		System.out.println(" * * * * * * * * * * * * ");
		System.out.println("* * * * * * * * * * * * *");
		System.out.println(" * * * * * * * * * * * * ");
		System.out.println("* * * * * * * * * * * * *");
		System.out.println(" * * * * * * * * * * * * ");
		System.out.println("* * * * * * * * * * * * *");
		myAccount Account = new myAccount();//new Account object created with class name "Account"
		Scanner input2 = new Scanner(System.in);//Create an object to read keyboard input
		System.out.printf("Initial name is: %s%n%n",Account.getName());//Initial name of account holder
		System.out.println("Please enter your full name: ");//Enter your full name
		String Fullname= input2.nextLine();//Reads the full name
		Account.setName(Fullname);//get the fullname to Account
		System.out.println("");
		System.out.printf("Name in object myAccount is: %n%s%n",Account.getName());//Initial name of account holder
		//input2.close();//close the input stream
		sc.close();//close the scanner
		character.close();//close the character stream
		input2.close();//close the input2 stream
		input.close();//close the input stream
	 }
}

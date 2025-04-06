/* Header files are files contining functions,variables,data-type definitions and constants that can be used within the programs.
	We use a preprocessor directive #include to include a header file.
	The preprocessor are the directives which tell the compiler to pre-process the contents of the header file.*/
#include <iostream>//is a header file for inputs and outputs
#include <cstring>
#include <string>
#include <cstdlib> //for exit() function
#include <cstdio> //for printf() function
#include <ctgmath>//for math functions
#include <cmath>//for math functions
#include <ctime>//for time functions
#include <iomanip>// for setprecision,setw functions to control output/input formatting
#include <fstream>//for file handling operations

using namespace std;
 /* run this program using the console pauser or add your own getch, system("pause") or input loop */
// we can use names for objects and variable from the standard library
int g=20;//global
int greater(int num1,int num2){
	//local variable declaration
	int result;
	if (num1 > num2){
		result = num1;
	}
	else{
		result = num2;
	}
	return result; //this is how we return values from functions
}

int Addition(int num1,int num2,int result){
    std::cout << "Give a number:";
    cin >> num1;
    std::cout << "Give another number:";
    cin >> num2;
    result=num1+num2;
    std::cout << "The Addition is " << result<< endl;
    return result,num1,num2;
}

class Addition{
	public:
	int num1,num2,sum;
	void getData(){
		std::cout << "Enter first number:" ;	
		cin>>num1;
		std::cout << "Enter second number:" ;
		cin>>num2;  
	} 
	void showResult() {
        sum = num1 + num2;
        cout << "\nSum of two numbers =" << sum << endl;
    }
};

	class Student{
		public:
			int roll_number;
			string name;
			void getInfo(int roll,string nam){
				roll_number = roll;
				name = nam;
			}
			void showInfo(){
				std::cout<<"Name:"<<name<<"\nRoll Number:"<<roll_number<<"\n";
			}
	};

	class Heydestructor{
		public:
			string name;
			Heydestructor(string n) {
				name = n;
				cout<<"Hi ! I am "<<name<<endl;
				}
			~Heydestructor(){
				cout<<"The object was deleted.";
			}
	};

	class Heyconstructor2{
		public:
			int num;
			Heyconstructor2(int n){ //parameterized constructor
			num=n;
			std::cout<<"Hi! For the "<<num<<" time."<<"\n";
	}
	};

	class Heyconstructor{
		public:
			Heyconstructor(){
				std::cout<<"Hi! I'm a constructor"<<"\n";
			}
	};

class BaseClass{
	public:
		int sum;
		void add(int num1,int num2){
			sum=num1+num2;
		}
		
};

class DerivedClass : public BaseClass{
	public:
	void showSum(){
		std::cout<<"Sum is: "<<sum;
	}
};


class Hello{
	public:
	virtual	void hello(){
			std::cout<<"Hello from the Base.";
		}
};

class HelloAgain:public Hello{
	public:
		void hello(){
			std::cout<<"Hello from the Sub.";
		}
};

class hello{
	public:
		void hello1(){
			std::cout<<"Hello";
		}

		void hello1(string name){
			std::cout<<"Hello "<<name;
			
		}
};


void Hello() {
    cout << "Hello" << endl;
}

void Hello(string name) {
    cout << "Hello " << name << endl;
}


class OhAbstraction{
	private:
		string name;//private variable
		public:
		 void getName(string newName){
			name=newName;
		 }
		 void showName(){
		 std::cout<<"Name:"<<name;
		 }
};

class Student1{
	public:
	virtual void name()=0; //pure virtual function, must be implemented in derived classes.
};

class Rahul: public Student1{
	public:
	void name(){
		std::cout<<"Rahul";
	}
};

void divideZero(int num){
	if (num==0){
		throw "Division by O Exception";
	}
}


int main(int argc, char** argv) {
	cout << "Hello World!\n";//for output and << to see the output
	string firstName = "John\n";
	cout << firstName;
	int gameScore=0;
	cout<<gameScore;
	cout<<"\n";
	int g=10;//local
	cout<<g;
	cout<<"\n";
	string name;
	cout<<"Enter your name:";
	cin>>name;//give input
	cout<<"Name entered is:"<<name;
	int x,y;
	int sum;
	cout<<"\nType a number:";
	cin>>x;
	cout<<"Type another number:";
	cin>>y;
	sum=x+y;
	cout<<"Sum is:"<<sum;
	cout<<"\n";
	int age;
	cout<<"Give your age>";
	cin>>age;
	if (age >= 18){
		cout<<"You are eligible to vote";
	}
	else{
		cout<<"Nope,you cannot vote";
	}
	char grade;
	cout<<"\nGive your grade>";
	cin>>grade;
	switch(grade){
		case 'A':
			cout<<"Excellent!";
			break;
		case 'B':
			cout<<"Well done";
			break;
		case 'C':
			cout<<"Good";
			break;
		case 'D':
			cout<<"You passed";
			break;
		case 'F':
			cout<<"Better try again";
			break;
		default :
			cout<<"Invalid grade";
	}
	cout<<"\n";
	cout<<"Your grade is "<<grade;
	cout<<"\n";
	/*char grade2='D'; (local variable declaration)
	switch(grade2){
		case 'A':
			cout<<"Excellent!"<<end1;
			break;
		case 'B':
			cout<<"Well done"<<end1;
			break;
		case 'C':
			cout<<"Good"<<end1;
			break;
		case 'D':
			cout<<"You passed"<<end1;
			break;
		case 'F':
			cout<<"Better try again"<<end1;
			break;
		default :
			cout<<"Invalid grade"<<end1;
	}
	cout<<"Your grade is "<<grade2<<end1; */
	for (int a=10; a<20; a=a+1) {
		cout<<"for loop value of a: "<<a;
		cout<<"\n";
	}
	int a=10;
	while (a<20) {
		cout<<"while loop value of a: "<<a;
		a++;
		cout<<"\n";
	}
	do {
		cout<<"do while loop value of a: "<<a;
		a=a+1;
		cout<<"\n";
	}while (a<20);
	int roll_no[5];
	roll_no[0]=45;
	roll_no[1]=89;
	roll_no[2]=16;
	roll_no[3]=10;
	roll_no[4]=23;
	int roll_no2[5]={45,89,16,10,23};
	for (int i=0;i<5;i++){
		cout<<"Element at index "<<i<<" is "<<roll_no[i];
		cout<<"\n";
	}
	int number=100;
	int number2=200;
	int ret;
	//calling  a function to get the greater value.
	ret = max(number,number2);
	cout<<"Greater value amongst the two is:"<<ret;
	cout<<"\n";
	char greeting[6]={'H','E','L','L','O','\0'};
	char greeting2[]="Hello";
	string name2="John";
	cout<<name2;
	cout<<"\n";
	/*string str1="Hello";
	string str2="World";
	string str3;
	int len;
	//copy str1 into str3
	strcpy(str3,str1);
	cout<<"strcpy(str3,str1):"<<str3;
	cout<<"\n";
	//concatenates str1 and str2
	strcat(str1,str2);
	cout<<"strcat(str1,str2):"<<str1;
	cout<<"\n";
	//total lenght of str1 after concatenation
	len=strlen(str1);
	cout<<"strlen(str1):"<<len;
	cout<<"\n"; */
	// Declare and initialize strings
    const char* str1 = "Hello";
    const char* str2 = "World";
    char str3[10];  // Make sure it has enough space to store "Hello"

    // Copy str1 into str3
    strcpy(str3, str1);
    std::cout << "strcpy(str3, str1): " << str3 << "\n";

    // Concatenate str1 and str2
    char str1Concatenated[20];  // Make sure it has enough space to store "HelloWorld"
    strcpy(str1Concatenated, str1);
    strcat(str1Concatenated, str2);
    std::cout << "strcat(str1, str2): " << str1Concatenated << "\n";

    // Total length of str1 after concatenation
    int len = strlen(str1Concatenated);
    std::cout << "strlen(str1): " << len << "\n";
	int a2=5;
	int *b2=&a2;
	std::cout<<b2<<"\n";//print address of a2
	int a3=5;
	int *b3=&a3;
	std::cout<<*b3<<"\n";//print the value of a3
	std::cout<<&a2<<"\n";//print the address of a2
	int a4=95;
	int *b4=&a4;
	std::cout<<*b4<<"\n";
	std::cout<<b4<<"\n";
	std::cout<<&a4<<"\n";
	std::cout<<&b4<<"\n";
	Student student1;//object of type student
	student1.getInfo(45,"Rahul");//Accessing member function
	student1.showInfo();//Accessing member function
	cout<<"\a";
	system("pause");
	/*1.strcpy(s1,s2):Copies string s2 into string s1
	  2.strcat(s1,s2):Concatenates string s2 onto the end of string s1
	  3.strlen(s1):Returns length of string s1
	  4.strcmp(s1,s2):Compares strings s1 and s2 or in other words return 0 if s1 and s2 are the same,
	  less than 0 if s1<s2,
	  greater than 0 if s1>s2.
	  5.strchr(s1,ch):Returns a pointer to the first occurrence of character ch in string s1
	  6.strrchr(s1,ch):Returns a pointer to the first occurrence of string s2 in string s1
	*/
	/*class className{
		Access Specifier:
		Members
	};*/
	/*A constructor is a function which has the same name as the class
	class Heyconstructor{
		Heyconstructor(){ //constructor
		//statements
		}
	}
	Every time an object is created , the constructor is called.
	A constructor is used to provide initial values to the class fields when an object is created.
	Every class has a constructor.
	If we don't write a constructor,the C++ compiler writes one for us which is called default constructor.
	Just like any other function,a constructor may or may not have any parameters.
	If a constructor has parameters it is known as a parameterized constructor.
	A default constructor has no parameters.*/
	Heyconstructor hi;//object
	//We have created a new object.So now our constructor will be called.
	Heyconstructor2 Hi(100); //Another object
	/*A destructor is a function which destructs or deletes an object.
	A destructor is called when an object of the class goes out of scope.
	The name of the destructor is the same as the name of the class.*/
	/*An object during its lietime uses many resources snd occupies memory.
	So the destructor function ensures that the memory and resources are free as soon as the object goes out of scope.
	There cannot be more than one destructors for a class.
	In the same way happens with the destructor in the class when we don't define a constructor manually,the C++ compiler does that part.
	It is known as a default destructor.
	The destructor function is always preceded by a tilde(~).
	A destructor does not take any parameters and also does not have any return type.*/
	Heydestructor hi3("Rahul");
	//Inheritance is when a class derives some properties from another class.
	//The class which inherits these properties is called derived class or sub class.
	//And the class from which the properties are derived is called base class or parent class or super class.
	/*class BaseClass{
		//body
	};
	
	class DerivedClass: access_specifier BaseClass{
		//body
	};
	*/
	//A derived class inherits the members of the base class depending upon the mode of inheritance.
	/*There are three modes of inheritance:
	1. Public inheritance
	2. Private inheritance
	3. Protected inheritance
	Public inheritance means that all public members of the base class are inherited in the derived class.
	Private inheritance means that all private members of the base class are inherited in the derived class.
	Protected inheritance means that all protected members of the base class are inherited in the derived class.
	When a class is derived from another class, the derived class inherits the public and protected members of the base class.*/
	DerivedClass d;//object of type DerivedClass
	//DerivedClass d.add(3,5);//Calling add function inherited from base class
	d.add(3,5);
	d.showSum();//Calling showSum function inherited from base class and displays the result
	/*Classes can inherit from other classes and in different ways. 
	There are four types of inheritance in C++:
	Single,Multiple, Multilevel and Hierarchical.
	SINGLE INHERITANCE
	In this, the derived class inherits only one base class.
	class BaseClass{
		//body
	};

	class DerivedClass :access_specifier BaseClass{
		//body
	};
	MULTIPLE INHERITANCE
	In this, the derived class inherits more than one base class.
	class BaseClass1{
		//body
	};

	class BaseClass2{
		//body
	};

	class DerivedClass :access_specifier BaseClass1,access_specifier BaseClass2{
		//body
	};
	MULTILEVEL INHERITANCE
	In this, the derived class inherits more than one base class.
	In multilevel inheritance there is a chaining of classes.
	class BaseClass1{
		//body
	};

	class DerivedClass1:access_specifier BaseClass1{
		//body
	};

	class DerivedClass2:access_specifier DerivedClass1{
		//body
	};
	HIERARCHICAL INHERITANCE
	In this, the derived class inherits more than one base class.
	In hierarchical inheritance there is no chaining of classes.
	In hierarchical inheritance,more than one derived class are inherited from a single base class.
	That is,a single base class is inherited by more than one derived class.
	There could be as many child classes as we want.
	But all these classes must have only a single parent class.
	class BaseClass{
		//body
	};
	
	class DerivedClass1:access_specifier BaseClass{//DerivedClass inherits BaseClass
		//body
	};
	
	class DerivedClass2:access_specifier BaseClass{//DerivedClass2 inherits BaseClass
		//body
	};
	There are one more type of inheritance exists - Hybrid Inheritance
	Hybrid inheritance is a combination of single, multiple, multilevel and hierarchical inheritance.*/
	/*Overloading suggests that two or more functions with the same name but different parameters should be defined in a single class.*/
	/*Overloading prevents us from writing multiple functions which perform the same task.*/
	Hello();//calling the function
	Hello("Rahul");//calling the function
	/*Overriding happens when the function in the derived class has the same name as the function in the base class along with the same parameters.*/
	HelloAgain h1;//object of type HelloAgain
	h1.hello();//calling the function using object of HelloAgain class
	hello h2;//object of type Hello
	h2.hello1();//calling the function using object of Hello class
	/*In OOP,polymorphism is the ability of an object to take more than one form.polymorphism is a way to perform a single action in different ways. 
	In C++,polymorphism can be defined as the capability of member functions to do different things based on the object that it is acting upon.
	Function overloading falls into polymorphism and so dos function overriding,as it allows us to use the same function in different manners.
	There are two types of polymorphism:
	1. Compile time through function overloading
	2. Run time through function overriding
	*/
	hello h3;//object of type hello
	h3.hello1();//calling the function hello
	h3.hello1("Rahul");//calling the function hello and passing the parameter "Rahul"
	/*HelloAgain h5;
	Hello *h4 = nullptr;
	h4 = &h5;
	h4->hello();//calling the function hello
	h4->hello("Rahul");//calling the function hello and passing the parameter "Rahul" */
	/*Runtime polymorphism cannot be achieved without using pointers and virtual functions.*/
	/*
	Abstraction is a process of hiding the implementation details and showing only the essential features of an object.
	*/
	OhAbstraction oh;
	//oh.name="Rahul";//passing the parameter//error
	oh.getName("Rahul");//passing the parameter
	oh.showName();//calling the function showName()
	cout<<endl;
	/*
	Encapsulation is a concept which describes the idea of buldling data member and member functions togethr.
	It helps in protecting the data members from unauthorized access.
	The variables in the class can only be accessed through the member functions.
	The data members are declared as private.
	The member functions are declared as public.
	Encapsulation provides a protected space for data members and member functions.
	Enapsulation is about hiding data whereas abstraction is about showing only essential features of an object.
	*/
	/*
	An interface is a collection of methods that a class must implement.
	In C++, we use pure virtual classes.
	A pure virtual class contains at least one pure virtual function.
	This function does not have any implementation, it is only declared in the base class.
	All derived classes will override this function.
	We don't need to create objects of the pure virtual class.
	We can create objects of the derived class.
	Interfaces are implemented using abstract classes.
	virtual return_type function_name(argument list) = 0;
	*/
	Rahul ra;//object of type Rahul
	ra.name();//calling the function name()
	//Exception is a event that disrupts the normal flow of the program.
	/*try{
		//body of try block
	}
	catch(exception_name e){
		//body of catch block
	}
	*/
	/*try{
		//body of try block
	}
	catch(exception_name e){
		//body of catch block
	}
	finally{
		//body of finally block
	}*/
	//Try block is used to enclose the block of code which might throw an exception.
	//Catch block is used to handle the exception.
	//Finally block is used to execute the code irrespective of exception.
	/*try {
		int num=40/0; //exception occurs here
	}
	catch(char *e){
		cout<<e<<endl;
	}
	*/
	//throw exception;//we can throw an exception also
	//The control goes out from the current function and goes to the nearest try block.
	divideZero(0);//exception occurs here
	//to open a file we use the open() function
	/*in-read mode
	out-write mode
	app-append mode.It searches for the last character in the file and starts writing from there.
	trunc-truncate mode.It deletes the contents of the file.*/
	//open("my_file.txt",ios::mode); //to open a file using ios class
	fstream newFile;
	char data[500];
	newFile.open("programming.txt",ios::in);//to open a file using fstream class
	newFile>>data;//to read from a file
	newFile.close();//closing the file
	//newFile>>whatever;//to read from a file
	//newFile<<whatever;//to write to a file
	fstream newFile2;
	newFile2.open("programming.txt",ios::in);//to open a file using fstream class again
	char data2[500]="Hello World";
	newFile2<<data2;//to write to a file
	newFile2.close();//closing the file
	return 0;
}

using System;
using System.Globalization;

namespace My_first_program
{
    class Addition{
        int num1,num2;
        public Addition(int number,int number2){
            number=num1;
            number2=num2;
        }
        public int add(int result,int num1,int num2){
            result=num1+num2;
            return result;
        }
        public void showadd(int result){
            Console.WriteLine(result);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            int A=10; //integer
            int B=-50;
            int C=0;
            double a=1.2;
            double b=-10.62;/**/
            double c=0;//decimals
            char cha='b';
            string str="buddy";
            Console.WriteLine("Hello World!");//print hello world
            C=A+B;
            Console.WriteLine(C);//print the sum of A and B
            C=A*B;
            Console.WriteLine(C);//print the product of A and B
            C=A/B;
            Console.WriteLine(C);//print the quotient of A and B
            C=A%B;
            Console.WriteLine(C);//print the remainder of A and B
            c=A+b;//addition of A and b which is in decimal
            Console.WriteLine(c);//print the sum of A and b
            c=c-2;//subtraction of c and 2
            B=(int)(b-a);//subtraction of b and A which is in decimal, then convert it to integer
            Console.WriteLine(B);//print the difference of b and A
            Console.WriteLine(cha+" for "+str);
            //Converting char integers
            char x='a';
            int i=(int)x;
            Console.WriteLine(i);//print the integer value of a
            char y=(char)97;
            Console.WriteLine(y);//print the character value of 97
            string firstname="Panos";//string
            string lastname="Biazis";//string
            string fullname=firstname+" "+lastname;//string concatenation
            Console.WriteLine(fullname);//print the full name
            string word ="Friend";
            char character = word[0];
            Console.WriteLine(character);//print the first character of the word friend
            //word=word.Substring(1);//remove the first character of the word friend
            string sentence2="a equals "+a;//string concatenation with variable
            Console.WriteLine(sentence2);//print the sentence a equals 1.2
            string sentence="a equals "+a.ToString();//string concatenation with variable converted to string
            Console.WriteLine(sentence);//print the sentence a equals 1.2
            int read;
            Console.WriteLine("Give a number:");
            read=int.Parse(Console.ReadLine());//read an integer from the console input and convert it to integer with Parse
            Console.WriteLine("The integer read is "+read);//print the integer read from the console input
            string input = Console.ReadLine(); // read the input as a string
            if (input != null){
            read = int.Parse(input); // parse the integer from the string input
            Console.WriteLine("The integer read is " + read); // print the integer read from the console input
            }
            else {
            Console.WriteLine("Invalid input. Please enter a number.");
            }
            string writestr="Hello World!";//string
            Console.WriteLine(writestr);//print the string Hello World!
            double doubles;
            doubles=double.Parse(Console.ReadLine());
            Console.WriteLine(doubles);//print the double read from the console input
            if(A>B){
                Console.WriteLine("A is greater than B");//print if A is greater than B
            } 
            else if(A<B){
                Console.WriteLine("B is greater than A");//print if B is greater than A
            }
            else{
                Console.WriteLine("A and B are equal");//print if A and B are equal
            }
            int n=5;
            for (int i1=0;i1<n;i1++){
                for (int j=0;j<=i1;j++){
                    Console.WriteLine("*");
                }
                Console.WriteLine(i1);
            }
            while(A<=25){
                A=A+5;
                Console.WriteLine(A);
            }
            System.Console.WriteLine("How many attended today: ");
            int c2=int.Parse(Console.ReadLine());
            string[] students=new string[c2];
            for(int i2=0;i2<c2;i2++){
                Console.WriteLine("Student "+(i2+1)+": ");
                students[i2]=Console.ReadLine();
            }
            for(int i3=0;i3<c2;i3++){
                Console.WriteLine(students[i3]);
            }
            int elements=100;
            int[] numbers=new int[elements];
            for(int i4=0;i4<elements;i4++){
                numbers[i4]=i4;
            }
            for(int i5=0;i5<elements;i5++){
                Console.WriteLine(numbers[i5]);
            }
            int elements2=5;  
            double[] dnumbers=new double[elements2];
            dnumbers[0]=10;
            dnumbers[1]=25;
            dnumbers[2]=(dnumbers[0]+dnumbers[1])/2;
            for (int i3=0;i3<elements2;i3++){
                Console.WriteLine(dnumbers[i3]);
            }
            int elements3=5;
            string[] words=new string[elements3];
            words[0]="Have ";
            words[1]="some ";
            words[2]="fun ";
            words[3]="with ";
            words[4]="C# ";
            for(int i6=0;i6<elements3;i6++){
                Console.WriteLine(words[i6]);
            }
            int c3=-5;
            int x1=5;
            int y1=5;
            while(c3 <= 250){
               c3=c3+ DoMath(x1,y1);
               for(int i4=5;i4<8;i4++){
                c3=c3+DoMath(x1,y1);
               } 
            }
            while (c3 <= 250){
                DoMath2(out x1,out y1);
                c3=c3+x+y;
            }
            int x2=2;
            string y2=null;
            DoMath4(out x2,out y2);
            Console.WriteLine("I have "+x2+" "+y2);
            
        } 
        static int DoMath(int a, int b){
            int variable=52;
            int variable1=a+b+variable;
            variable1=variable1*2;
            return variable;
        } 
        static void DoMath2(out int a,out int b){
            a=15;
            b=3;
        }
        static int DoMath3(int a,int b){
            int variable=52;
            int variable1=a+b+variable;
            variable1=variable1*2;
            return variable;
        }
        static void DoMath4(out int a,out string b){
            int v=15;
            a=v+10;
            b="Friends";
        }
        
    }
}
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

int addf(){
    int a,b,c;
    cout<<"Enter two numbers:\n"<<"1.";
    cin>>a;
    cout<<"2.";
    cin>>b;
    c=a+b;
    cout<<"The sum is: "<<c<<endl;
    return 0;
}

int subf(){
    int a,b,c;
    cout<<"Enter two numbers:\n"<<"1.";
    cin>>a;
    cout<<"2.";
    cin>>b;
    c=a-b;
    cout<<"The sub is: "<<c<<endl;
    return 0;
}

int mulf(){
    int a,b,c;
    cout<<"Enter two numbers:\n"<<"1.";
    cin>>a;
    cout<<"2.";
    cin>>b;
    c=a*b;
    cout<<"The mul is: "<<c<<endl;
    return 0;
}

int divf(){
    int a,b,c;
    cout<<"Enter two numbers:\n"<<"1.";
    cin>>a;
    cout<<"2.";
    cin>>b;
    c=a/b;
    cout<<"The div is: "<<c<<endl;
    return 0;
}

int modf(){
    int a,b,c;
    cout<<"Enter two numbers:\n"<<"1.";
    cin>>a;
    cout<<"2.";
    cin>>b;
    c=a%b;
    cout<<"The mod is: "<<c<<endl;
    return 0;
}

class Math
{
    private:
    void add(){
        addf();
    }

    void sub(){
        subf();
    }

    void mul(){
        mulf();
    }

    void div(){
        divf();
    }

    void mod(){
        modf();
    }

    void linearF(){
       int y,a,x,b;
       cout<<"Enter three numbers:\n"<<"1.";
       cin>>a;
       cout<<"2.";
       cin>>b;
       cout<<"3.";
       cin>>x;
       cout<<"The Solution of Linear function "<<"y"<<"="<<a<<"*"<<x<<"+"<<b<<" ==> y="<<(y=a*x+b)<<"\n";
    }

    public:

    void menu(){
        menu:;
        int choice;
        cout<<"Enter your choice:\n";
        cout<<"1. Add\n";
        cout<<"2. Sub\n";
        cout<<"3. Mul\n";
        cout<<"4. Div\n";
        cout<<"5. Mod\n";
        cout<<"6. Linear function\n";
        cout<<"Select > > > ";
        cin>>choice;
        cout<<"You selected "<<choice<<"\n";
        switch(choice){
            case 1:
                add();
                break;
            case 2:
                sub();
                break;
            case 3:
                mul();
                break;
            case 4:
                div();
                break;
            case 5:
                mod();
                break;
            case 6:
                linearF();
                break;
            default:
                cout<<"Invalid choice\n";
                goto menu;
        }
    }

};


int main(int argc, char** argv) {
    Math operationA;
    operationA.menu();
    system("pause");
    return 0;
}

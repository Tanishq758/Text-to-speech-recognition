#include<iostream>
using namespace std;

class complex{
    int a,b;
public:
    complex(int , int); // constructor declaration

    void printnumber(){
        cout<<"the number is "<<a <<"+"<<b <<"i"<<endl;
   }


};
complex::complex(int x, int y){
    a=x;
    b=y;
}

int main(){
    complex c1(2,3);//explict call
    c1.printnumber();

    complex c2= complex(4,5);//implicit call
    c2.printnumber();

    return 0;
}
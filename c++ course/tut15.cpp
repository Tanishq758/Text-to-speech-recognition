#include<iostream>
using namespace std;

class complex{
    int a;
    int b;
public:
    void setnumber(int v1, int v2){
        a=v1;
        b=v2;
        
    }
    void setnumberbysum(complex o1, complex o2){
        a=o1.a+o2.a;
        b=o1.b+o2.b;
    }
    void printnumber(void){
        cout<<"the complex number is "<<a<<"+"<<b<<"i"<<endl;
    }
    };
int main(){
    complex c1,c2,c3;
    c1.setnumber(1,3);
    c1.printnumber();

    c2.setnumber(2,5);
    c2.printnumber();

    c3.setnumberbysum(c1,c2);
    c3.printnumber();
    
    return 0;
}
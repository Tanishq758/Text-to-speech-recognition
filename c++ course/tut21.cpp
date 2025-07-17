#include<iostream>
using namespace std;
//********************************************************************************************** */
//single inheritence
//********************************************************************************************** */

class base{
    int data1;
    public:
    int data2;
    void setdata();
    int getdata1();
    int getdata2();

};

void base :: setdata(void){
    data1=10;
    data2=20;
}

int base::getdata1(){
    return data1;
}
int base :: getdata2(){
    return data2;
} 
class derieved : public base{
    int data3;
    public:
    void process(){
        data3= data2*getdata1();

    }

    void display(){
        cout<<"value of data 1 "<<getdata1()<<endl;
        cout<<"value of data 2  "<<data2<<endl;
        cout<<"value of data3 "<<data3<<endl;
    }

};



int main(){
    derieved der;
    der.setdata();
    der.process();
    der.display();
    
    return 0;
}
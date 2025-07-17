#include<iostream>
using namespace std;
class employee{
    int id;
    static int count;

public:
    void setdata(void){
        cout<<"enter thee id of the employee"<<endl;
        cin>>id;
        count++;
    }

    void getdata(void){
        cout<<"the id of this employee is "<<id<<endl<<"the value of this employee is "<<count<<endl;
    }


};

int employee :: count;

int main(){
    employee harry,ronit,jerry;
    harry.setdata();
    harry.getdata();
    ronit.setdata();
    ronit.getdata();
    jerry.setdata();
    jerry.getdata();
    
    return 0;
}
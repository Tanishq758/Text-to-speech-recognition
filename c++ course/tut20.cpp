#include<iostream>
using namespace std;
int count=0;
class num{
    public:
    num(){
        count++;
        cout<<"this is the time constructor is called for object"<<count<<endl;
    }
    ~num(){
        cout<<"this is the time destructor is called for object"<<count<<endl;
        count--;
    }

};
int main(){
    cout<<"creating a object n1"<<endl;
    num n1;
    {
        cout<<"entering this block"<<endl;
        cout<<"cretaing two more object"<<endl;
        num n2,n3;
        cout<<"exiting this block"<<endl;
        }
    cout<<"back to main"<<endl;    

    return 0;
}
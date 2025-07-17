#include<iostream>
using namespace std;

int main(){
    int age;
    cout<<"tell us your age"<<endl;
    cin>>age;

    if((age<18)&&(age>0)){
        cout<<"you cannot come to the party";    
    }
    else if(age==18){
        cout<<"grow";
    }
    else{
        cout<<"you can come";
    }
    return 0;
}
#include<iostream>
using namespace std;

int main(){
    int age;
    cout<<"your age ?"<<endl;
    cin>>age;

    switch (age)
    {
    case 18:
        /* code */
        cout<<"you are 18";
        break;
    case 22:
        cout<<"you are 22";
        break;
    
    default:
        cout<<"no special cases";
        break;
    }

    return 0;
}


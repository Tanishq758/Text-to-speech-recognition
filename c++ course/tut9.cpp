#include<iostream>
using namespace std;
struct employee
{
    /* data */
    int eID;
    char favChar;
    float salary;

};


int main(){
    struct employee harry;
    harry.eID=7;
    harry.favChar='c';
    harry.salary=45678;

    cout<<harry.eID<<endl;
    cout<<harry.favChar<<endl;
    cout<<harry.salary<<endl;
    
    return 0;
}
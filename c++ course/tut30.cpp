#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;
int main(){
    string st = "hello bhai";
    ofstream out("tut30.txt");
    out<<st;
 

    string st2;
    ifstream in("tut30c.txt");
    getline(in,st2);
    cout<<st2;
    
    return 0;

}
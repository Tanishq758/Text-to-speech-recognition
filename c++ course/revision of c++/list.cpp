#include<iostream>
#include <list>
using namespace std;

void explain_list(){
    list<int> ls;
    ls.push_back(2);
    ls.emplace_back(3);
    ls.push_front(1);
    ls.emplace_front(5);
    ls.erase(ls.begin());
    for(auto it:ls){
        cout<<it<<" ";
    }
}
int main(){
    explain_list();
    return 0;
}
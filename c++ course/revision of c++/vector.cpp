#include<iostream>
#include <vector>

using namespace std;

void explainvector(){
    // vector delaration 
    vector<int> v;
    v.push_back(1);
    v.emplace_back(2);
    cout<<v[0]<<" "<<v[1]<<endl;
    cout<<endl<<endl<<endl;

// vector and iterator 
    vector<int> vec={1,2,3,4,5,6};
    vector<int>::iterator it=vec.begin();
    it++;
    cout<<*it<<endl;

    vector<int>::iterator it2 =vec.end();
    it2--;
    cout<<*it2<<endl;
    
    cout<<endl;

    vector<int>::reverse_iterator it3 =vec.rend();
    it3--;
    it3--;
    cout<<*it3<<endl;

    vector<int>::reverse_iterator it4= vec.rbegin();
    it4++;
    cout<<*it4;
    cout<<endl;


    // using for loops and printing using iterator 

    for(vector<int>::iterator f_it=vec.begin(); f_it!=vec.end();f_it++){
        cout<<*f_it<<" ";
    }
    cout<<endl;

    // using auto
    for(auto it=vec.begin();it!= vec.end();it++){
        cout<<*it<<" ";
    }

    cout<<endl;

    for(auto it:vec){
        cout<<it<<" ";
    }
    cout<<endl<<endl<<endl;

    // using erase in vector
    // vec.erase(vec.begin()+3);
    // for(auto it:vec){
    //     cout<<it<<" ";

    // vec.erase(vec.begin()+1,vec.begin()+3);
    // for(auto it:vec){
    //      cout<<it<<" ";


    cout<<vec.size();
    cout<<endl;

    v.swap(vec);

    cout<<"v"<<endl;
    for(auto it:v){
        cout<<it<<" "  ;
          }
          cout<<endl;

    cout<<"vec"<<endl;
    for(auto it:vec){
        cout<<it<<" "  ;
          }      



}




int main(){
    explainvector();
    return 0;
}

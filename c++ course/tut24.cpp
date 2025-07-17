#include<iostream>
using namespace std;

class base1{
    public:
        void greet(){
            cout<<"hello world"<<endl;
        }
};

class base2{
    public:
        void greet(){
            cout<<"kaise ho!!"<<endl;
        }
};

class derived : public base1, public base2{
    private:
        int a;
    public:                        //ambiguity resolution
        void greet(){
            base2 :: greet();
        }
    

};
int main(){
    base1 a;
    base2 b;
    derived c;

    a.greet();
    b.greet();
    c.greet();
    return 0;
}
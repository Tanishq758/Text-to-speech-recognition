#include<iostream>
#include<math.h>
using namespace std;

class calculator{
    protected:
        float a;
        float b;
    public:
        void setnumbers(float , float);
        float sum();
        float differnece();
        float multiply();
        float divide();
};

void calculator::setnumbers(float n1, float n2){
    a=n1;
    b=n2;
}

float calculator::sum(){
    return a+b;
}

float calculator::differnece(){
    return a-b;
}
float calculator::multiply(){
    return a*b;
}
float calculator::divide(){
    return a/b;
}

class scientific_calc : public calculator{
    public:
        float root(){
            return sqrt(a+b);
        }
        float powernum(){
            return pow(a,b);
        } 
        float sintheta(){
            return sin(a+b);
        }
        float costhteha(){
            return cos(a+b);
        }
};

class hybridcalc : public scientific_calc{
    public:
        void diplay(){
            cout<<"the value of sum is "<<sum()<<endl;
            cout<<"the value of difference is "<<differnece()<<endl;
            cout<<"the product of is "<<multiply()<<endl;
            cout<<"the division is "<<divide()<<endl;
            cout<<"the square root is "<<root()<<endl;
            cout<<"the power is "<<powernum()<<endl;
            cout<<"the sine is "<<sintheta()<<endl;
            cout<<"the cos is "<<costhteha()<<endl;
             }


};
int main(){
    hybridcalc c;
    c.setnumbers(45.6,6.6);
    c.diplay();
    return 0;
}
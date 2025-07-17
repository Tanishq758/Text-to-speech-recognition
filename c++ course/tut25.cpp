#include<iostream>
using namespace std;

class student{
    protected:
        int roll_number;
    public:
        void set_roll_number(int r){
            roll_number=r;
        } 
        void print_number(){
            cout<<"your number is "<<roll_number<<endl;
        }   
};

class test : virtual public student{
    protected:
        float maths;
        float physics;
    public:
        void set_marks(float m1 , float m2){
            maths=m1;
            physics = m2;
        }
        void print_marks(){
            cout<<"your marks are "<<endl
            <<"maths:" <<maths<<endl
            <<"physics :"<<physics<<endl;
        }

};
class sports : virtual public student{
    protected:
        float score;
    public:
        void set_score(float s){
            score=s;
        }
        void print_score(){
            cout<<"your score is "<<score<<endl;
        }
    };

class result : public test, public sports{
    private:
        float total;
    public:
        
        void display(){
            total= maths+physics+score;
            print_number();
            print_marks();
            print_score();
            cout<<"your total is "<<total<<endl;

        }
};


int main(){
    result tansihq;
    tansihq.set_roll_number(234);
    tansihq.set_marks(98.8,78.8);
    tansihq.set_score(9);
    tansihq.display();
    
    return 0;
}
#include<iostream>
#include<math.h>
using namespace std;
float distance();
class point{
    int x,y;
    public:
    friend float distance(point,point);
    point(int a , int b){
        x=a;
        y=b;
    }
    void displaypoint(){
        cout<<"the point is ("<<x<<","<<y<<")"<<endl;
        }
};

float distance (point x1, point x2){
    int xcor=x2.x-x1.x;
    int ycor=x2.y-x1.y;
    int sqrx=xcor*xcor;
    int sqry=ycor*ycor;
    int sum=sqrx+sqry;
    float dis=sqrt(sum);
    cout<<"the distance between the points is "<<dis<<endl;
}
int main(){
    point p(3,4);
    p.displaypoint();
    point q(5,6);
    q.displaypoint();
    distance(p,q);
    return 0;
    
}
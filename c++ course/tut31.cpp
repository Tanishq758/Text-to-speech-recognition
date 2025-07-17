#include<iostream>
using namespace std;

template <class t>

class vector{
    public:
        t *arr;
        int size;
        vector(int m){
            size=m;
            arr = new t[size];
        }
        t dotproduct(vector &v){
            t d=0;
            for (int i = 0; i < size; i++)
            {
                d+=this->arr[i]*v.arr[i];
            }
            return d;
        }

};

int main(){
    vector<float> v1(3);
    v1.arr[0]=1.1;
    v1.arr[1]=4.4;
    v1.arr[2]=3.3;

    vector<int> v2(3);
    v2.arr[0]=2;
    v2.arr[1]=5;
    v2.arr[2]=1;

    cout<<v1.dotproduct(v2);


    return 0;
}
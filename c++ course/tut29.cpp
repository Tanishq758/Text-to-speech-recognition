#include<iostream>
#include<cstring>
using namespace std;

class CWH{
    protected:
        string title;
        float rating;
    public:
    CWH(string s, float r){
        title=s;
        rating=r;
    }
    virtual void display(){}
};

class CWHVIDEO :public CWH{
    protected:
        float vdlenth;
    public:
        CWHVIDEO(string s, float r, float vdl):CWH(s,r){
            vdlenth=vdl;
        }
        virtual void display(){
            cout<<"this is an amaging video with title "<<title<<endl;
            cout<<"ratings :"<<rating<<"out of 5 stars "<<endl;
            cout<<"length of this video is "<<vdlenth<<"minutes"<<endl;
        }
};

class CWHTEXT :public CWH{
    protected:
        int words;
    public:
        CWHTEXT(string s, float r, int w):CWH(s,r){
            words=w;
        }
        virtual void display(){
            cout<<"this is an amaging video with title "<<title<<endl;
            cout<<"ratings :"<<rating<<"out of 5 stars "<<endl;
            cout<<"no of words used are "<<words<<endl;
        }
};

int main(){
    string title;
    float rating,vlen;
    int words;

    title="django tutorials video";
    rating=4.56;
    vlen=4.78;
    CWHVIDEO  djvideo(title,rating,vlen);


    title="django tutorials text";
    rating=4.34;
    words=455;
    CWHTEXT  djtext(title,rating,words);

    CWH* tuts[2];
    tuts[0]=&djtext;
    tuts[1]=&djvideo;

    tuts[0]->display();
    cout<<endl;
    tuts[1]->display();

    return 0;
}
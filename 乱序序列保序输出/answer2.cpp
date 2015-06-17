#include<iostream>
using namespace std;
int main()
{
    int a[10]={1, 2, 5, 8, 10, 4, 3, 6, 9, 7};
    int book[11];
    memset(book,0,sizeof(book));//簿记数组清0
    int j=1;
    int flag=0;
    for(int i=0;i<10;++i)
    {
        book[a[i]]=1;//来了一个数，簿记
        while(book[j]&&j<11)
        {
            if(flag==1)
                cout<<",";
            else
                flag=1;
            cout<<j;
            j++;
        }
        if(flag==1){
            flag=0;
            cout<<endl;
        }
    }
    return 0;
}

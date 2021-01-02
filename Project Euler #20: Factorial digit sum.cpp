#include <bits/stdc++.h>
using namespace std;

int main(){
    int q,n,x,i,p;
    cin>>q;
    while(q--){
        int c=0;
        cin>>n;
        int a[999999];
        a[0]=1;
        int size=1;
        for(x=2;x<=n;x++){
            for(i=0;i<size;i++){
                p=a[i]*x+c;
                a[i]=p%10;
                c=p/10;
            }
            if(c>0){  
                while(c>0){
                    a[size]=c%10;
                    c/=10;
                    size++;
                }
            }
        }
        long sum=0;
        for(i=size-1;i>=0;i--){
            sum+=a[i];
        }
        cout<<sum<<endl;
    }
    return 0;
}

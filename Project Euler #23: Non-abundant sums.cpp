#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int sum_fac(int x){
    
    int sum = 0;
    
    for(int i=1;i<sqrt(x);i++){
        if(x % i == 0){
            
            if ((x/i) == i){
                sum += i;   
            }

            else{
                sum += i;
                sum += x/i;
            }
        }
    }
    return sum - x;  
}

int check_sum(int abundant[20162],int no,int count){
    
    for(int i=0;i<count;i++){
        for(int j=0;j<count;j++){
            if((abundant[i] + abundant[j]) == no){
                return 1;
            }
            
            if((abundant[i] + abundant[j]) > no){
                break;
            }
        }
    }
    
    return 0;
    
}


int main() {
     
    
    int abundant[20162];
    int count = 0;
    
    abundant[count] = 12;
    count++;
    
    int sum;
    
    for(int i=13;i<20162;i++){
        
        sum = sum_fac(i);
        
        if(sum > i){
            abundant[count] = i;
            count++;
        }
    }
    
    int t,no;
    
    cin>>t;
    
    for(int i=0;i<t;i++){
        cin>>no;
        
        if(no > 20161){
            cout<<"YES"<<endl;
        }else{
            
            
            
            int x = check_sum(abundant,no,count);
            
            if(x == 1){
                cout<<"YES"<<endl;
            }else{
                cout<<"NO"<<endl;
            }
        }
    }
    
    
    return 0;
}

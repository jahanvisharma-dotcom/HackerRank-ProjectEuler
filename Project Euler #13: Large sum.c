#include <stdio.h>

char number[51];
int  ans[60];
int carry = 0;
int j, i;

void sum(void)
{
 
    for(i = 49, j = 0; i >= 0; i--, j++)
    {
        carry = (ans[j] + number[i] - '0')/10;
        ans[j + 1] += carry;
        ans[j] = (ans[j] + number[i] - '0')%10;
    }

}

int main(void)
{
    int N;
    scanf("%d",&N);

    for(int i = 0; i < 60; i++)
        ans[i] = 0;

    while(N > 0)
    {
        scanf("%s", number);
        sum();
        N--;
    }
    
    int k = 1;
    if(ans[j] == 0) j--;
    
    for(i = j ; k <= 10 ; i--)
    {      
        if(ans[i]/10 != 0)
        {
            int temp = ans[i];
            while(temp != 0)
            {
                 temp = temp/10;
                k++;
            }
        }
         else    k++;
     
        printf("%d", ans[i]);
    }
}

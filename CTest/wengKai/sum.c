#include<stdio.h>
void sum(int begin,int end);//声明
int main(){
    sum (1,10);
    return 0;
}
// 定义
void sum(int begin,int end)
{
    int i;
    int sum = 0;
    for(i = begin;i <= end;i++){
        sum+=i;
    
    }
    printf("%d到%d的和是%d\n",begin,end,sum);
}
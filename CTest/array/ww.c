#include<stdio.h>
int search(int key,int a[],int length);
int main(void)
{
    // int a[]= {2,4,5,67,65,2,56,12};
    int a[] = {[1]=2,4,[5]=6};
    int x;
    int loc;
    printf("请输入一个数字:");
    scanf("%d",&x);
    printf("sizeof(a)=%d\n",sizeof(a));
    printf("sizeof(a[0])=%d\n",sizeof(a[0]));
    loc = search(x,a,sizeof(a)/sizeof(a[0]));
    if( loc != -1 ){
        printf("%d在第%d个位置上\n",x,loc);
    }else{
        printf("%d不存在\n",x);
    }
    return 0;
}
int search(int key,int a[],int length){
    int ret = -1;
    int i;
    for( i = 0;i < length;i++){
        if( a[i] == key ){
            ret = i;
            break;
        }
    }
    return ret;
}
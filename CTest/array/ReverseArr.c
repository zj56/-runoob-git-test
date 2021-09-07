#include<stdio.h>
void reverse(int x[],int n);
void main(){
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int i;
    reverse(arr,10);
    // for( i = 0;i < 10 ;i++){
    //     printf("%d\n",arr[i]);
    // }
}
void reverse(int x[],int n){
    int temp ,i ,j ,m;
    m = (n - 1)/2;
    printf("%d",m);
    for( i = 0;i <=m; i++){
        j = n- 1- i;
        temp = x[i];
        x[i] = x[j];
        x[j] = temp;
    }
}
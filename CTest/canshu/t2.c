#include<stdio.h>
void test(int & x){
    x = 1024;
    printf("test内部%d",x);
}
int main(){
    int x = 1;
    printf("first%d",x);
    printf("\n");
    test(x);
    printf("\n");
    printf("first%d",x);
}
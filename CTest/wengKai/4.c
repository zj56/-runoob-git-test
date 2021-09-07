void f(int* p);
int main(void){
    int i =6;
    printf("&i=%p\n",&i);
    f(&i);
    return 0;
}
void f(int* p){
    printf("p=%d",*p);
}
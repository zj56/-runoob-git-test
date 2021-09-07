int max,min;
void max_min_value(int array[],int n);
void main()
{
    int i,number[10];
    printf("enter 3 integer numbers:\n");
    for( i = 0;i < 3;i++){
        scanf("%d",&number[i]);
    }
    max_min_value(number,10);
    printf("\nmax=%d,min=%d\n",max,min);

}
void max_min_value(int array[],int n)
{
    int *p,*array_end;
    array_end = array + n;
    max = min = *array;
    for()
}
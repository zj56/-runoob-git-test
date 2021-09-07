#include<stdio.h>
#include<malloc.h>
int main(void){
    int a[5];//如果int占4个字节的话，则本数组
    /* 总共包含有20个字节  */
    int len;
    int *pArr;
    int i;
    printf("请输入你要存放的元素的个数：");
    scanf("%d",&len);
    pArr = (int *)malloc(4 * len);
    // 效果类似于 int pArr[len];
    /* 动态的构造了一个一维数组，该数组的长度为len 
    int * 表示数组的每一个元素为int类型 ，每一个int为4个字节
    */
   for(i = 0;i < len;i++){
       scanf("%d",&pArr[i]);
   }
    // 对一维数组进行输出
    for(i = 0;i < len;++i){
        printf("%d\n",pArr[i]);
    }
    free(pArr);
    return 0;
}
/* realloc(pArr,100)
 */
/* 动态内存和静态内存的比较
 静态内存由系统自动分配，由系统自动释放
 静态内存是在栈分配
 动态内存是由程序员手动分配，手动释放 
 动态内存是在堆分配*/
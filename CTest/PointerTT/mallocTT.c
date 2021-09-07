#include<stdio.h>
#include<malloc.h>
/* malloc函数的使用 */
/* 
malloc是memory（内存） allocate（分配）的缩写 
*/
int main(void){
    int i = 5;//分配了4个字节，静态分配
    int *p = (int *)malloc(4);
    printf("%d",sizeof(p));
    /* 
        1、要添加malloc头文件
        2、malloc函数只有一个形参，并且形参是整数类型（整型）
        3、malloc（4） 4表示请求系统为本程序分配4个字节
        4、malloc函数只能返回第一个字节的地址
            malloc只返回首字节地址
        5、（char*）malloc(100),100个字节，每个char占1个字节，划分100个变量
            （int*）malloc(100),100个字节，每个int占4个字节，划分25个变量
            所以必须进行强制类型转换
        6、    int *p = (int *)malloc(4);
            分配了12 = 4 + 8个字节
            p本身所占的8个字节内存是静态分配
            而p所指向的内存是动态分配的
        
     */
    free(p);
    /* free(p)表示把p所 ！！！指向的！！！ 内存给释放掉 */
    /* p本身的内存是静态的，p的内存只能在p变量所在的函数运行终止时
    由系统自动释放 */
    printf("同志们好");
    return 0;
}
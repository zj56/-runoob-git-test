// #include<stdio.h>
#define MaxSize 10
typedef struct{
    int data[MaxSize];
    int length;
}SqList;

void InitList(SqList &L){
    L.length = 0;
    for(int i = 0;i<MaxSize;i++)
        L.data[i]=0;
}
//基本操作：在L的i位序处插入元素e
//i=3,arr[2]=e
//arr[]有四个元素arr[3]
//arr[4]=arr[3] arr[3]=arr[2](原始arr【2】数据)
//插入到表尾，for不用循环 O（1）
//插入到表头 O（n）
//平均 O(n/2)即O（n）
bool ListInsert(SqList &L,int i,int e){
    //i的值可能不合法,例如i=9
    if(i<1||i>L.length+1)
        return false;

    //数组可能已经满了
    if(L.length>=MaxSize)
        return false;

    for(int j = L.length;j>=i;j--)
    //data[]的元素
        L.data[j]=L.data[j-1];
    L.data[i-1]=e;
    //数据元素加1
    L.length++;
    return true;
}
//删除操作
// &e 引用数据类型参数,在内存中是同一份数据
bool ListDelete(SqList &L,int i,int &e){
    //判断i的范围
    if(i<1||i>L.length)
        return false;
    //将被删除的元素赋值给e
    e=L.data[i-1];
    //将第i个位置的元素前移
    for(int j=i;j<L.length;j++)
        L.data[j-1]=L.data[j];
    L.length--;
    return true;
}
//时间复杂度O（1）
//由于顺序表的各个元素在内存中连续存储
//因此可以根据起始地址和数据元素的大小立即找到第i个元素
int GetElem(SqList L,int i){
    return L.data[i-1];
}

//按值查找
//在顺序表中查找第一个元素值等于e的值
//并返回其位序
//结构类型struct不能用“==”对比
//如果要笔记结构体，属性分别相等
int LocateElem(SqList L,int e){
    for(int i = 0;i < L.length;i++){
        //最好 O（1）
        //最坏O（n）
        //平均O（n）
        if(L.data[i]==e)
            return i+1;
    }
    return 0;
}
int main(){
    SqList L;
    InitList(L);
    ListInsert(L,1,3);
    //用变量e把删除的元素“带回来”
    int e = -1;
    if(ListDelete(L,3,e))
        
    
    return 0;
}
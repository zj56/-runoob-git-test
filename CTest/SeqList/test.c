#include "SeqList.h"

//测试头尾的插入和删除
void TestSeqList1(){
    SeqList s;
    SeqListInit(&s);
    SeqListPushBack(&s,1);
    SeqListPushBack(&s,2);
    SeqListPushBack(&s,3);
    SeqListPrint(&s);
}
int main(){
    TestSeqList1();
    return 0;

}
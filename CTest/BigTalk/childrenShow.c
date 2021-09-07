#define MAX_TREE_SIZE 100
// 线性表和链表联合存储
typedef struct CTNode/* 孩子节点 */
{
    int child;
    struct CTNode *next;
} *ChildPtr;
/* 表头结构 */
typedef struct{
    int data;
    ChildPtr firstchild;
} CTBox;
typedef struct{
    CTBox nodes[MAX_TREE_SIZE];
    int r,n;
    // 根的位置和节点数
}
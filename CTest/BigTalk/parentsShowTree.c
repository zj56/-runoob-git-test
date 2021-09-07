#define MAX_TREE_SIZE 100
typedef int TElemType;
typedef struct PTNode{
    TElemType data;
    int parent;//双亲位置
   
} PTNode;
// 定义树结构
typedef struct{
    PTNode nodes[MAX_TREE_SIZE];//结点数组
    int r , n;
    /* 根的位置和节点数 */
}PTree;
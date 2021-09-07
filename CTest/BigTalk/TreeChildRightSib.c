typedef struct CSNode{
    int data;
    struct CSNode* firstchild,*rightsib; 
    struct CSNode* parents;
} CSNode,*CSTree;
/* 普通树转位二叉树 */


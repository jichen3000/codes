#include <deque>
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct NodeValues {
    TreeNode *node;
    int val;
    int count;
    NodeValues(TreeNode *n, int v, int c) : node(n), val(v), count(c) {}
};
class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        if (!root) return 0;
        deque<NodeValues> q {NodeValues(root, root->val-2, 1)};
        int res = 1;
        while (q.size()){
            NodeValues cur = q.front(); 
            q.pop_front();
            int count = cur.count;
            if (cur.val + 1 == cur.node->val){
                count ++;
                res = max(res, count);
            } else {
                count = 1;
            }
            if (cur.node->left)
                q.push_back(NodeValues(cur.node->left, cur.node->val, count));
            if (cur.node->right)
                q.push_back(NodeValues(cur.node->right, cur.node->val, count));

        }
        return res;
    }
};

// very simple one
class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        return search(root, nullptr, 0);
    }

    int search(TreeNode* node, TreeNode* parent, int len) {
        if (!node) return len;
        len = (parent && node->val == parent->val + 1) ? len + 1 : 1;
        return max(len, max(search(node->left, node, len), search(node->right, node, len)));
    }

};

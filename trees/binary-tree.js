"use strict";

class BinaryTree {
  constructor(root = null) {
    this.root = root;
  }
}

class BinaryTreeNode {
  constructor(val, right = null, left = null) {
    this.val = val;
    this.right = right;
    this.left = left;
  }
}

/** Question that Megan had in an interview:
 I can clarify: Given two nodes, you need to find their lowest common ancestor
 (basically the ancestor they share that is closest to both of them further
  down on the tree). The input for the function would be the root, and then two
  nodes we are looking for.

                 4
                / \
               2   3a
              /\    /\
             5  3b 1  7a
            /   /\
          7b   9a 6
          /\     /
         9b 11  8
          Input: Node4, Node7b, Node3b
          Output: Node2
*/

class BTree {
  constructor(root) {
    this.root = root;
  }

/**
 * I: root, pNode and qNode
 * 0: node
 * considerations: node can be an ancestor to itself
 */
  LCA(root, pNode, rNode){

  }
}


class BNode {
  constructor(value, right, left, parent) {
    this.value = value;
    this.right = right;
    this.left = left;
    this.parent = parent;
  }
}



/** Question above in reverse:
 * "find the lowest common child of two nodes in a binary tree"
 * The two nodes could not be ancestors of each other, and the binary
 * tree was not necessarily a binary search tree.
 */



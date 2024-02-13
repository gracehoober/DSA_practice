"use strict";

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
  constructor(root = null) {
    this.root = root;
  }

  /**
   * I: root, pNode and qNode
   * 0: node
   * considerations: a node has access to its parent
   * logic:
   *    start and the p and q -> go up the tree making a list of ancestor nodes for both
   *    if the same node is in both lists return that node, include the self nodes in the list,
   *    go until root is hit, if root is hit return rootNode
   */
  LCA(root, pNode, rNode) {

  }
}


class BNode {
  constructor(value, right = null, left = null, parent = null) {
    this.value = value;
    this.right = right;
    this.left = left;
    this.parent = parent;
  }

  /** returns a list of the node's ancestors in order from closest related
   * ancestor (parent) to furthest ancestor (root).
   */
  nodeAncestors() {
    let ancestors = [this];
    let current = this;

    while (this.parent !== null) {
      ancestors.push(current);
      current = this.parent;
    }

    return ancestors;
  }
}



/** Question above in reverse:
 * "find the lowest common child of two nodes in a binary tree"
 * The two nodes could not be ancestors of each other, and the binary
 * tree was not necessarily a binary search tree.
 */


module.exports = { BNode, BTree };
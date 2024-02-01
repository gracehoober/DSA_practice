"use strict";

/** Tree: class for tree */
class Tree {
  constructor(root = null){
    this.root = root
  }
}

/** TreeNode: class for a tree node */
class TreeNode {
  constructor(val, children = []){
    this.val = val
    this.children = children
  }
}

/** sumValues: given a tree whose values are integers, return the sum of the
 * integers.
 */
function sumValues(tree){
  let current = tree.root;
  let queue = [current];
  let sum = [];

  while(queue.length > 0){
    //put current.val into sum
    sum.push(current.val)
    //put current.children into que
    for(let child in current.children){
      queue.push(child)
    }
    //take current out of q
    queue.shift(current)
    //reassign current to next val in q
    current = queue[0]
    queue.push(current)

  }
  return sum.reduce(accrue, val => accrue + val, 0)
}


module.exports = { Tree, TreeNode };
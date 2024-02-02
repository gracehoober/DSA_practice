"use strict";

/** TreeNode: class for a tree node */
class TreeNode {
  constructor(val, children = []){
    this.val = val
    this.children = children
  }
}

/** Tree: class for tree */
class Tree {
  constructor(root = null){
    this.root = root
  }
/** sumValues: given a tree whose values are integers, return the sum of the
 * integers.
 * BFS example:
 *  queue = first in, first out
 */

 sumValues(){
  let current = this.root;
  let queue = [current];
  let sum = [];

  while(queue.length > 0){

    sum.push(current.val)

    for(let child in current.children){
      queue.push(child)
    }

    queue.shift()
    current = queue[0]
    queue.push(current)

  }
  return sum.reduce(accrue, val => accrue + val, 0)
}

/** countEvens: given a tree whose values are integers, return a count of the
 * even values.
 * DFS example = last in, first out
 */
countEvens(){
  let current = this.root
  let stack = [current]
  let countOfEvens = 0;

  while(stack.length > 0){
    if(current.val % 2 === 0){
      countOfEvens++;
    }
    //put children into stack
    for(let child of current.children){
      stack.push(child)
    }
    //make current next value current = stack.pop()
    current = stack.pop()
  }
  return countOfEvens
}

}





module.exports = { Tree, TreeNode };
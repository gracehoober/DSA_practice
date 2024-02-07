"use strict";

/** TreeNode: class for a tree node */
class TreeNode {
  constructor(val, children = []) {
    this.val = val;
    this.children = children;
  }

  /** Returns the sum of all the node and it's children */
  sumValues() {
    let sum = this.val;//1
    console.log(sum, " sum in node")
    for (let child of this.children) {//3
      sum += child.val;
    }
    console.log(sum, " returned sum from node")
    return sum;
  }
}

/** Tree: class for tree */
class Tree {
  constructor(root = null) {
    this.root = root;
  }

  /** sumValues: given a tree whose values are integers, return the sum of the
   * integers.
   * BFS example:
   *  queue = first in, first out
   */
  sumValues() { // 1-2
    let sum = 0;
    if (this.root === null) {
      return sum;
    }
    let current
    let queue = [this.root];

    while (queue.length > 0) {
      current = queue.pop();
      sum += current.sumValues();
      if(current !== this.root){
        sum -= current.val
      }
      for (let child of current.children) {
        queue.push(child);
      }
    }
    console.log(sum," sum from tree")
    return sum;
    //go through entire tree and add to sum
    //when a node is visited add's sum to the total
    //subtract each node's value from the tolal
    //return total
  }

  /** countEvens: given a tree whose values are integers, return a count of the
   * even values.
   * DFS example = last in, first out
   */
  countEvens() {
    let current = this.root;
    let stack = [current];
    let countOfEvens = 0;

    while (stack.length > 0) {
      //make current next value current = stack.pop()
      current = stack.pop();

      if (current.val % 2 === 0) {
        countOfEvens++;
      }
      //put children into stack
      for (let child of current.children) {
        stack.push(child);
      }
    }
    return countOfEvens;
  }

  /** Given a n-ary tree and a number x, find and return the number
   * of nodes which are greater than x.
   */
  numGreater(num) {
    let numberOfNodeVals = 0;
    let current = this.root;
    let stack = [];

    while (stack.length > 0) {
      current = stack.pop();

      if (current.val > num) {
        numberOfNodeVals++;
      }
      for (let child of current.children) {
        stack.push(child);
      }

    }
    return numberOfNodeVals;
  }

}


module.exports = { Tree, TreeNode };
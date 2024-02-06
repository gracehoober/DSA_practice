"use strict";

/** TreeNode: class for a tree node */
class TreeNode {
  constructor(val, children = []) {
    this.val = val;
    this.children = children;
  }
  sumValues(){

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
  sumValues() {
    let current = this.root;
    //console.log(current, "Current")
    let queue = [current];
    //console.log(queue, "Queue")
    let sum = 0;

    while (queue.length > 0) {
      current = queue.pop();
      console.log(queue.length, "number in q")
      sum += current.val;
      console.log(sum, "sum")
      for (let child in current.children) {
        queue.push(child);
        console.log(child, "CHILD")
      }
    }
    return sum;
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
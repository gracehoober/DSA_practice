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
   *
   *  Question: does not work for an empty tree
   */
  sumValues() {// 1-2
    let current = this.root;//1

    let queue = [current];//[1]

    let sum = 0;

    while (queue.length > 0) {
      queue.pop();//[]

      sum += current.val || 0;//sum = 1

      //console.log(current.children, "Children")
      for (let child of current.children) {//2
        queue.push(child);//[2]
      }
      current = queue[queue.length - 1]
      //console.log(current, "current after reassignemnt")
      //console.log(queue, "queue at end of loop")
    }
    console.log(sum, "sum before return")
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
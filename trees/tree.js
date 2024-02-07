"use strict";

/** TreeNode: class for a tree node */
class TreeNode {
  constructor(val, children = []) {
    this.val = val;
    this.children = children;
  }

  /** Returns the sum of all the node and it's children's values integer
   * sumValues returns an integer
   */
  sumValues() {
    let sum = this.val;

    for (let child of this.children) {
      sum += child.val;
    }

    return sum;
  }

  /** Returns the number of even node values in the node and it's children
   * count evens returns an integer
   */
  countEvens(){
    let evens;
    this.val % 2 === 0 ? evens++ : evens = 0;

    for(let child of this.children){
      if(child.val % 2 === 0){
        evens++;
      }
    }
    return evens;
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

    return sum;
  }

  /** countEvens: given a tree whose values are integers, return a count of the
   * even values.
   * DFS example = last in, first out
   */
  countEvens() {
    let countOfEvens = 0;

    if(this.root === null){
      return countOfEvens;
    }

    let current
    let stack = [this.root];
    while (stack.length > 0) {
      //make current next value current = stack.pop()
      current = stack.pop();
      countOfEvens += current.countEvens();

      if(current.val !== this.root && current.val % 2 === 0){
        countOfEvens -= 1;
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
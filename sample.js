 "use strict"
 class Node {
  constructor(value, children = []){
    this.value = value;
    this.children = children
  }
 }

 class Tree{
  constructor(root){
    this.root = root
  }
 }
 // build large tree
  //
  //                  root
  //                    |
  //                    1
  //                /   |   \
  //               2    3    4
  //                       /   \
  //                      5     6
  //                           /
  //                          7
  //                          |
  //                          8
  //

  /** match a queue and stack with BFS and DFS */
 //search for value, print a value, sum of all values

  function BFS(tree, val){// 2
    let current = tree.root//Node1
    let queue = [current] //[ Node2, Node3, Node4]

    while(queue.length > 0){
      if(current.value === val) return true
      //put children of current into q
      for(let child of current.children){
        queue.push(child)
      }
      //remove the current value from q
      queue.shift()
      //change the current value to the first val in the q
      current = queue[0]//Node2
    }

    return false

  }

  function DFS(tree){
    let struct = []
  }
"use strict";

const { BTree, BNode } = require("./binary-tree");

let largeTree;
let emptyTree;

beforeEach(function () {
  /** Creates an empty tree */
  emptyTree = new BTree();

  /** Creates a large tree like:

                 4
                / \
               2   31
              /\    /\
             5  3  1  71
            /   /\
          72   91 6
          /\     /
         93 11  8

 */

  //Create the nodes and their children
  let n8 = new BNode(8, null, null);
  let n11 = new BNode(11, null, null);
  let n93 = new BNode(93, null, null);
  let n6 = new BNode(6, null, n8);
  let n91 = new BNode(91, null, null);
  let n72 = new BNode(72, n11, n93);//n5
  let n71 = new BNode(71, null, null);//n31
  let n1 = new BNode(1, null, null);//n31
  let n3 = new BNode(3, n6, n91);//n2
  let n5 = new BNode(5, n72, null);//n2
  let n31 = new BNode(31, n71, n1);//n4
  let n2 = new BNode(2, n3, n5);//n4
  let n4 = new BNode(4, n31, n2, null);

  //Add each node's parent
  n8.parent = n6;
  n11.parent = n72;
  n93.parent = n72;
  n6.parent = n3;
  n91.parent = n3;
  n72.parent = n5;
  n71.parent = n31;
  n1.parent = n31;
  n3.parent = n2;
  n5.parent = n2;
  n31.parent = n4;
  n2.parent = n4;
  n4.parent = null;

  //Create the tree
  largeTree = new BTree(n4);

});

describe("nodeAncestors", function () {
  it("handles a node near root of tree", function () {
    expect(n31.nodeAncestors()).toEqual([n31, n4]);
  });

  it("handles a leaf node", function () {
    expect(n93.nodeAncestors()).toEqual([n93, n72, n5, n2, n4]);
  });

  it("handles a root node", function () {
    expect(n4).toEqual([n4]);
  });

});

// describe("LCA", function() {
//   it("sums simple trees", function() {
//     expect(smallTree.sumValues()).toEqual(3);
//   });

//   it("sums more complicated trees", function() {
//     expect(largeTree.sumValues()).toEqual(36);
//   });

//   it("sums up an empty tree", function() {
//     expect(emptyTree.sumValues()).toEqual(0);
//   });
// });
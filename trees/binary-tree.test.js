"use strict";

const { BTree, BNode } = require("./tree");

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
  let n4;
  let n31;
  let n2;
  let n5;
  let n3;
  let n1;
  let n71;
  let n72;
  let n91;
  let n6;
  let n93;
  let n11;
  let n8;

  n4 = new BNode(4, n2, n31, null);
  n31 = new BNode(31, n1, n71, n4);
  n2 = new BNode(2, n5, n3, n4);
  n5 = new BNode(5, 72, null, n2);
  n3 = new BNode(3, n91, n6, n2);
  n1 = new BNode(1, null, null, n31);
  n71 = new BNode(71, null, null, n31);
  n72 = new BNode(72, n93, n11, n5);
  n91 = new BNode(91, null, null, n3);
  n6 = new BNode(6, n8, null, n8);
  n93 = new BNode(93, null, null, n72);
  n11 = new BNode(11, null, null, n72);
  n8 = new BNode(8, null, null, n6);

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
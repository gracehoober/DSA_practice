"use strict";

const { BTree, BNode } = require("./tree");

/**

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


beforeEach(function (){
    /** Creates an empty tree */
    let emptyTree = new BTree();

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
    let n4 = BNode(4, n2, n31, null);
    let n31 = BNode(31, n1, n71, n4);
    let n2 = BNode(2, n5, n3, n4);
    let n5 = BNode(5, 72, null, n2);
    let n3 = BNode(3, n91, n6, n2);
    let n1 = BNode(1, null, null, n31);
    let n71 = BNode(71, null, null, n31);
    let n72 = BNode(72, n93, n11, n5);
    let n91 = BNode(91, null, null, n3);
    let n6 = BNode(6, n8, null, n8);
    let n93 = BNode(93,null,null,n72);
    let n11 = BNode(11, null, null, n72);
    let n8 = BNode(8, null, null, n6);
    let largeTree = new BTree(n4);

})

describe("nodeAncestors", function() {
  it("handles an empty tree", function() {
    expect(emptyTree.).toEqual();
  });

  it("returns the ancestors of a single node", function() {
    expect(largeTree).toEqual(36);
  });

  it("", function() {
    expect(emptyTree.sumValues()).toEqual(0);
  });
});

describe("LCA", function() {
  it("sums simple trees", function() {
    expect(smallTree.sumValues()).toEqual(3);
  });

  it("sums more complicated trees", function() {
    expect(largeTree.sumValues()).toEqual(36);
  });

  it("sums up an empty tree", function() {
    expect(emptyTree.sumValues()).toEqual(0);
  });
});
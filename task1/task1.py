#!/bin/python
#transform an sorted array into binary tree
#from builtins import input as raw_input
import random
import time

class TreeNode:
    def __init__(self,key,value,parent=None,left=None,right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.leftChild = left
        self.rightChild = right

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def hasSingleChild(self):
        return (self.leftChild or self.rightChild) and (not self.hasBothChildren())

    def replaceNodeData(self,replaceNode):
        self.key = replaceNode.key
        self.value = replaceNode.value
        self.leftChild = replaceNode.leftChild
        self.rightChild = replaceNode.rightChild

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for value in self.leftChild:
                    yield value 
            yield self.key
            if self.hasRightChild():
                for value in self.rightChild:
                    yield value

class BinarySearchTree:
    '''Binary Tree Object'''
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def _set(self,currentNode,key,value):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._set(currentNode.leftChild,key,value)
            else:
                currentNode.leftChild = TreeNode(key,value,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._set(currentNode.rightChild,key,value)
            else:
                currentNode.rightChild = TreeNode(key,value,parent=currentNode)

    '''inset node'''
    def set(self,key,value):
        if self.root:
            '''set one node'''
            self._set(self.root,key,value)
        else:
            '''set root node'''
            self.root = TreeNode(key,value)
        self.size = self.size + 1

    '''override [] operater'''
    def __setitem__(self,key,value):
        self.set(key,value)

    def _get(self,currentNode,key):
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(currentNode.leftChild,key)
        else:
            return self._get(currentNode.rightChild,key)

    '''get node'''
    def get(self,key):
        if self.root:
            res = self._get(self.root,key)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    '''override [] operator'''
    def __getitem__(self,key):
        return self.get(key)

    '''override in operator'''
    def __contains__(self,key):
        if self.get(key):
            return True
        else:
            return False

    def getMin(self,currentNode):
        min = currentNode
        if min.hasLeftChild():
            min = min.leftChild
        return min

    def _delete(self,deleteNode):
        #remove leaf
        if deleteNode.isLeaf():
            if deleteNode.parent.leftChild == deleteNode:
                deleteNode.parent.leftChild = None
            else:
                deleteNode.parent.rightChild = None
        #remove node with one childNode
        elif deleteNode.hasSingleChild():
            if deleteNode.hasLeftChild():
                if deleteNode.isLeftChild():
                    deleteNode.parent.leftChild = deleteNode.leftChild
                    deleteNode.leftChild.parent = deleteNode.parent
                elif deleteNode.isRightChild():
                    deleteNode.parent.rightChild = deleteNode.leftChild
                    deleteNode.legtChild.parent = deleteNode.parent
                else:
                    deleteNode.replaceNodeData(deleteNode.leftChild)
            else:
                if deleteNode.isLeftChild():
                    deleteNode.parent.leftChild = deleteNode.rightChild
                    deleteNode.leftChild.parent = deleteNode.parent
                elif deleteNode.isRightChild():
                    deleteNode.parent.rightChild = deleteNode.rightChild
                    deleteNode.legtChild.parent = deleteNode.parent
                else:
                    deleteNode.replaceNodeData(deleteNode.rightChild)
        # remove node with both ChildNodes
        # notice successor node has no more than one child(rightChild only)
        #   we search for smallest key node from deleteNode right subtree
        #   the node must be a leftChild of its parent except it's rightChild of deleteNode

        else:
            res = getMin(deleteNode.rightChild) 
            if res.hasRightChild():
                if res.parent == deleteNode:
                    res.parent.rightChild = res.rightChild
                    res.rightChild.parent = res.parent
                else:
                    res.parent.leftChild = res.rightChild
                    res.rightChild.parent = res.parent
            elif res.isLeaf():
                if res.parent == deleteNode:
                    res.parent.rightChild = None
                else:
                    res.parent.leftChild = None
            deleteNode.key = res.key
            deleteNode.value = res.value

    def delete(self,key):
        if self.size > 1:
            deleteNode = self._get(self.root,key)
            if deleteNode:
                self._delete(deleteNode)
                self.size = self.size - 1
            else:
                raise KeyError('key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('key not in tree')

    '''override del operator'''
    def __delitem__(self,key):
        self.delete(key)
        

if __name__ == "__main__":
# get input array
    a = input("Please enter values for your array:")
    print(a)
    a_list = list(map(int,a.split(' ')))
    print(a_list)
    a_list.sort()
    print("the array is:")
    print(a_list)
    tree1 = BinarySearchTree()
    # use array value as value sequence as key
    print("set tree1 value")
    for i,x in zip(range(len(a_list)),a_list):
        tree1.set(i,x)
    print("print tree1 value")
    for i in range(len(a_list)):
        print("key %s value: %s"%(i,tree1[i]))
    # use array value as key and random value as node value
    tree2 = BinarySearchTree()
    random.seed(time.time())
    print("set tree2 value")
    for j in a_list:
        tree2.set(j,random.random())
    for j in a_list:
        print("kdy %s value: %s"%(j,tree2[j]))
# Time Complexity: 
# hasNext: Worst O(N), Amortized O(1) N is total number of integer
# next: O(1)

# Space Complexity: 
# hasNext: O(D) D is for nested depth D
# next: O(1)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.stack = []
        if nestedList:
            self.stack.append(iter(nestedList))
        self.nextElement = None

    # TC : O(1)
    def next(self):
        """
        :rtype: int
        """
        return self.nextElement.getInteger()

    # TC : O(d) - depth of nested list
    def hasNext(self):
        """
        :rtype: bool
        """

        while len(self.stack) > 0:
            iterator = self.stack[-1]
            currentNextElement = next(iterator, None)

            if currentNextElement is None:
                self.stack.pop()
            else:
                self.nextElement = currentNextElement
                if self.nextElement.isInteger():
                    return True
                else:
                    self.stack.append(iter(self.nextElement.getList()))
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
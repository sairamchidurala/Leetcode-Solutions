# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        result = [str(root.val) + ' ']
        
        if root.left:
            result.append(self.serialize(root.left))
        if root.right:
            result.append(self.serialize(root.right))
            
        return ''.join(result)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = list(map(int, data.split()))
        self.index = 0
        
        return self.preorder(data, float('-inf'), float('inf'))
    
    def preorder(self, data, minLimit, maxLimit):
        if self.index >= len(data) or data[self.index] <= minLimit or data[self.index] >= maxLimit:
            return None
        
        head = TreeNode(data[self.index])
        self.index += 1
        head.left = self.preorder(data, minLimit, head.val)
        head.right = self.preorder(data, head.val, maxLimit)
        
        return head
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

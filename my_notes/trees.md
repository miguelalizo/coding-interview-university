# Trees

- [BFS(breadth-first search) and DFS(depth-first search) (video)](https://www.youtube.com/watch?v=uWL6FJhq5fM)
    - BFS notes:
        - level order (BFS, using queue)
        - time complexity: O(n)
        - space complexity: best: O(1), worst: O(n/2)=O(n)
        - code:
        ```
        ```
    - DFS notes:
        - time complexity: O(n)
        - space complexity:
            best: O(log n) - avg. height of tree
            worst: O(n)
        - inorder (DFS: left, self, right)
        - postorder (DFS: left, right, self)
        - preorder (DFS: self, left, right)
        - code:
        ```
        ```

- [Tree Traversal (video)](https://www.coursera.org/lecture/data-structures/
    - Walking a tree:
        - Depth first:
            - Completely travers one sub-tree before exploring a sibling tree
                - In order traversal:
                    -For a binary tree, this gives us the nodes in order!
                    ```python
                    inOrderTraversal(tree):
                        if tree=null:
                            return
                        InOrderTraversal(tree.left)
                        print(tree)
                        InOrderTraversal(tree.right)
                    ```
                    - Pre order traversal:
                    ```python
                    preOrderTraversal(tree):
                        if tree=null:
                            return
                        print(tree)
                        preOrderTraversal(tree.left)
                        preOrderTraversal(tree.right)
                    ```
                    - Post order traversal:
                    ```python
                    postOrderTraversal(tree):
                        if tree=null:
                            return
                        postOrderTraversal(tree.left)
                        postOrderTraversa(tree.right)                        
                        print(tree)
                    ```
            - Note, with recursive calls, we are saving implicitly the order of each call of the respective Traversal into the stack


        - Breadth first search (LevelTraversal):
            - Explore all the nodes at one level before moving onto the next level
            - Uses a queue instead of a stack
            ```python
            LevelTraversal(tree):
                if tree = nu;;:
                    return
                Queue q
                q.Enqueue(tree)
                while not q.Empty():
                    node<-q.dequeue()
                    print(node)
                    if node.left!=null:
                        q.Enqueue(tree.left)
                    if node.right!=null:
                        q.Enqueue(tree.right)
                ```

 - [[Review] Breadth-first search in 4 minutes (video)](https://youtu.be/HZ5YTanv5QE)
    - Breadth first search
        - Used to search graphs and trees
        - Algorithm will progress horizontally before verticalle
        - Data structure used is a first in first out queue
    - Video contains breadth first search algorithm code but figure it out then write it down
        - Time complexity:
            - We will visit each vetrex and explore every edge, therefore O(|v|+|e|)
        - Space complexity

- [[Review] Depth-first search in 4 minutes (video)](https://youtu.be/Urx87-NMm6c)
    - Depth first search
        - Algorithm for searching a graph or tree vertically before continuing horizontally
        - Uses a stack as the data structure
        - Time complexity:
            - We will visit each vetrex and explore every edge, therefore O(|v|+|e|) = same as breadth first search
        - Space complexity


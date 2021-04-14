import random
from collections import deque

from typing import Optional, List, Iterable, Union

# pip install pptree
from ppbtree import print_tree


class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 1

    def __repr__(self):
        return f"AVLNode: {self.value=}, {self.height=}"


class AVLTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return f"AVLTree: {self.root.value=}, {self.root.height=}"

    def __str__(self):
        return " ".join(str(node.value) for node in self.__tree_generator())

    def to_list(self) -> List[int]:
        return [node.value for node in self.gen()]

    def __tree_generator(self) -> Iterable:
        visited = set()

        if self.root is None:
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            node: AVLNode = queue.popleft()

            yield node

            if node.left_child not in visited:
                if node.left_child is not None:
                    queue.append(node.left_child)

            if node.right_child not in visited:
                if node.right_child is not None:
                    queue.append(node.right_child)

    def gen(self):
        if self.root is None:
            return

        queue = [self.root]

        for node in queue:
            yield node

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

    def print_tree(self):
        """
        Print tree with using "print_tree" from "ppbtree" library
        :return: AVLNode
        """
        print_tree(self.root, left_child='right_child', right_child='left_child', nameattr='value')

    def insert(self, value: Union[int, float]) -> None:
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError

        if self.root is None:
            self.root = AVLNode(value)
        else:
            self._insert(value, self.root)

    def get_node_by_value(self, value) -> Optional[AVLNode]:
        if self.root is not None:
            return self._get_node_by_value(self.root, value)
        else:
            return

    def _get_node_by_value(self, node: AVLNode, value) -> Optional[AVLNode]:
        if value == node.value:
            return node

        elif value < node.value and \
                node.left_child is not None:
            return self._get_node_by_value(node.left_child, value)

        elif value > node.value and \
                node.right_child is not None:
            return self._get_node_by_value(node.right_child, value)

        return

    @staticmethod
    def __insert_to_smallest_node_in_subtree(node: AVLNode, adding_node: AVLNode) -> None:
        smallest_node = AVLTree.__get_smallest_node_in_subtree(node)
        smallest_node.left_child = adding_node
        smallest_node.left_child.parent = smallest_node

    @staticmethod
    def __get_smallest_node_in_subtree(node: AVLNode) -> AVLNode:
        while node.left_child:
            node = node.left_child
        return node

    @staticmethod
    def get_height(node: AVLNode) -> int:
        return 0 if node is None else node.height

    @staticmethod
    def _insert_left_child(node: AVLNode, value) -> AVLNode:
        node.left_child = AVLNode(value)
        node.left_child.parent = node
        return node.left_child

    @staticmethod
    def _insert_right_child(node: AVLNode, value) -> AVLNode:
        node.right_child = AVLNode(value)
        node.right_child.parent = node
        return node.right_child

    def _insert(self, value, cur_node: AVLNode) -> None:
        if value < cur_node.value:
            if cur_node.left_child is None:
                left_child = self._insert_left_child(cur_node, value)  # set parent
                self._inspect_insertion(left_child)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                right_child = self._insert_right_child(cur_node, value)  # set parent
                self._inspect_insertion(right_child)
            else:
                self._insert(value, cur_node.right_child)
        else:
            raise ValueError("Value already in the tree!")

    def _inspect_insertion(self, cur_node: AVLNode, path=None) -> None:
        if path is None:
            path = deque()

        if cur_node.parent is None:
            return

        path.appendleft(cur_node)

        left_height = self.get_height(cur_node.parent.left_child)
        right_height = self.get_height(cur_node.parent.right_child)

        if abs(left_height - right_height) > 1:
            path.appendleft(cur_node.parent)
            self._rebalance(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _rebalance(self, parent_node: AVLNode, node: AVLNode, child_node: AVLNode) -> None:
        if node == parent_node.left_child and \
                child_node == node.left_child:
            self._right_rotation(parent_node)

        elif node == parent_node.left_child and \
                child_node == node.right_child:
            self._left_rotation(node)
            self._right_rotation(parent_node)

        elif node == parent_node.right_child and \
                child_node == node.right_child:
            self._left_rotation(parent_node)

        elif node == parent_node.right_child and \
                child_node == node.left_child:
            self._right_rotation(node)
            self._left_rotation(parent_node)

        else:
            raise Exception('_rebalance: nodes configuration not recognized!')

    def _right_rotation(self, node: AVLNode) -> None:  # Нужно перепроверить
        node_parent = node.parent

        left_child = node.left_child
        right_child_of_left_child = left_child.right_child

        left_child.right_child = node
        node.parent = left_child

        node.left_child = right_child_of_left_child

        if right_child_of_left_child is not None:
            right_child_of_left_child.parent = node
        left_child.parent = node_parent
        if left_child.parent is None:
            self.root = left_child
        else:
            if left_child.parent.left_child == node:
                left_child.parent.left_child = left_child
            else:
                left_child.parent.right_child = left_child

        # Set new height
        node.height = 1 + max(self.get_height(node.left_child),
                              self.get_height(node.right_child))
        left_child.height = 1 + max(self.get_height(left_child.left_child),
                                    self.get_height(left_child.right_child))

    def _left_rotation(self, node: AVLNode) -> None:  # Нужно перепроверить
        node_parent = node.parent

        right_child = node.right_child
        left_child_of_right_child = right_child.left_child

        right_child.left_child = node
        node.parent = right_child

        node.right_child = left_child_of_right_child

        if left_child_of_right_child is not None:
            left_child_of_right_child.parent = node

        right_child.parent = node_parent
        if right_child.parent is None:
            self.root = right_child
        else:
            if right_child.parent.left_child == node:
                right_child.parent.left_child = right_child
            else:
                right_child.parent.right_child = right_child

        # Set new height
        node.height = 1 + max(self.get_height(node.left_child),
                              self.get_height(node.right_child))
        right_child.height = 1 + max(self.get_height(right_child.left_child),
                                     self.get_height(right_child.right_child))


if __name__ == "__main__":
    tree = AVLTree()

    lst = list(range(1, 9))
    random.shuffle(lst)

    for i in lst:
        tree.insert(i)
        print(f"        Insert: {i}")
        tree.print_tree()
        print(tree.get_node_by_value(i))
        print(tree)
        print("*************************")

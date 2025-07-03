from typing import Tuple


class Node:
    """Node of a Huffman binary tree."""

    def __init__(self, prob, left=None, right=None, value=None):
        """
        Initialize node.

        Parameters
        ----------
        prob : float
            Probability of the node
        left : Node
            Left node.
        right : Node
            Right node.
        value : Object
            Value of the node.
        """
        self.prob = prob
        self.left = left
        self.right = right
        self.value = value

    def get_children(self):
        """
        Get children of the node.

        Returns
        -------
        Tuple[Node, Node]
            Children of the node.
        """
        return self.left, self.right

    def get_value(self):
        """
        Get value of the node.

        Returns
        -------
        Object
            Value of the node.
        """
        return self.value

    def get_prob(self):
        """
        Get probability of the node.

        Returns
        -------
        float
            Probability of the node.
        """
        return self.prob


def get_tree(probs, values):
    """
    Get a Huffman tree from given probabilities and values.

    Parameters
    ----------
    probs : List[float]
        Probabilities of the nodes.
    values : List[Object]
        Values of the node.

    Returns
    -------
    Node
        Huffman tree from given probabilities and values.
    """
    nodes = [Node(p, value=v) for p, v in zip(probs, values)]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.get_prob())
        first = nodes.pop(0)
        second = nodes.pop(0)
        new_prob = first.get_prob() + second.get_prob()
        nodes.append(Node(new_prob, left=first, right=second))
    return nodes[0]


def get_codes(tree):
    """
    Get codes of given Huffman tree.

    Parameters
    ----------
    tree : Node
        Huffman tree.

    Returns
    -------
    Dict[Object, str]
    """
    nodes = [("", tree)]
    values = {}
    for code, node in nodes:
        if node.get_value() is None:
            nodes.append((code + "0", node.left))
            nodes.append((code + "1", node.right))
        else:
            values[node.get_value()] = code
    return values

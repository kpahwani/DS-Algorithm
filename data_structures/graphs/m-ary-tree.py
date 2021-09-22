class Node(object):
    def __init__(self, value):
        self.children = set()
        self.value = value
        self.total = self.value

    def add_child(self, node):
        node.total += self.total
        if node.total <= self.total:
            self.children.add(node)


class Vaccine(object):
    @classmethod
    def find_outcomes(cls, n, k):
        if (n <= 0) or (k <= 0) or (n > k) or (k > 2 ** (n - 1)):
            return 0
        elif n == k:
            return 1

        cls.N = n
        cls.K = k
        cls.OUT = 0

        root = Node(1)
        child = Node(1)
        root.add_child(child)
        curr_level = 2
        cls.do(child, curr_level)

        return cls.OUT

    @classmethod
    def do(cls, node, level):
        if level == cls.N:
            if node.total == cls.K:
                cls.OUT += 1
            return

        for j in range(1, node.total + 1):
            child = Node(j)
            node.add_child(child)
            cls.do(child, level + 1)


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(Vaccine.find_outcomes(n, k))



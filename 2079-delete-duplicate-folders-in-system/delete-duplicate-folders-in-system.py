class Solution:
    def deleteDuplicateFolder(self, paths):
        class Node:
            def __init__(self):
                self.children = {}
                self.del_mark = False

        root = Node()

        # build trie
        for path in paths:
            cur = root
            for name in path:
                if name not in cur.children:
                    cur.children[name] = Node()
                cur = cur.children[name]

        from collections import defaultdict
        freq = defaultdict(int)

        # serialize subtrees
        def serialize(node):
            if not node.children:
                return ""
            parts = []
            for name in sorted(node.children):
                parts.append(name + "(" + serialize(node.children[name]) + ")")
            key = "".join(parts)
            freq[key] += 1
            return key

        serialize(root)

        # mark duplicates
        def mark(node):
            if not node.children:
                return ""
            parts = []
            for name in sorted(node.children):
                parts.append(name + "(" + mark(node.children[name]) + ")")
            key = "".join(parts)
            if key and freq[key] > 1:
                node.del_mark = True
            return key

        mark(root)

        # collect remaining paths
        res = []

        def collect(node, path):
            for name, child in node.children.items():
                if child.del_mark:
                    continue
                new_path = path + [name]
                res.append(new_path)
                collect(child, new_path)

        collect(root, [])
        return res

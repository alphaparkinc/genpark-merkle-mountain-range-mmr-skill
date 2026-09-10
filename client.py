import hashlib

class MMRAccumulator:
    """
    Merkle Mountain Range (MMR).
    Append-only Merkle tree structure represented as a list of balanced binary peaks.
    """
    def __init__(self):
        self.peaks = [] # list of (height, hash_val)
        self.leaves = []

    def _hash(self, a, b):
        return hashlib.sha256((str(a) + ":" + str(b)).encode("utf-8")).hexdigest()[:16]

    def append(self, item):
        leaf_hash = hashlib.sha256(item.encode("utf-8")).hexdigest()[:16]
        self.leaves.append(leaf_hash)
        curr_node = (0, leaf_hash)

        # Merge peaks of identical height
        while self.peaks and self.peaks[-1][0] == curr_node[0]:
            left = self.peaks.pop()
            parent_hash = self._hash(left[1], curr_node[1])
            curr_node = (curr_node[0] + 1, parent_hash)

        self.peaks.append(curr_node)
        return leaf_hash

    def get_bagged_root(self):
        if not self.peaks:
            return ""
        root = self.peaks[0][1]
        for p in self.peaks[1:]:
            root = self._hash(root, p[1])
        return root

    def peak_count(self):
        return len(self.peaks)

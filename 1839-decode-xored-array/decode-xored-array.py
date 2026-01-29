class Solution:
    def decode(self, encoded, first):
        n = len(encoded) + 1
        arr = [first]

        for e in encoded:
            arr.append(arr[-1] ^ e)  # arr[i+1] = arr[i] XOR encoded[i]

        return arr

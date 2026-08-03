class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        low = 0
        high = r - 1

        while low <= high:
            mid = (low + high) // 2

            if target > matrix[mid][-1]:
                low = mid + 1

            elif target < matrix[mid][0]:
                high = mid - 1

            else:
                break

        if not (low <= high):
            return False

        l, ri = 0, c - 1

        while l <= ri:
            m = (l + ri) // 2

            if target > matrix[mid][m]:
                l = m + 1

            elif target < matrix[mid][m]:
                ri = m - 1

            else:
                return True

        return False
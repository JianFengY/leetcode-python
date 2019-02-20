class Solution:
    """
    https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/774/
    给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
    输入:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    输出:  [1,2,4,7,5,3,6,8,9]
    """

    def find_diagonal_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # result = []
        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return result
        # if len(matrix) == 1 or len(matrix[0]) == 1:
        #     return [x for a in matrix for x in a]
        # # 一共 M + N - 1 条对角线
        # lines = len(matrix) + len(matrix[0]) - 1
        # # 最长的对角线元素个数
        # count = min(len(matrix), len(matrix[0]))
        # for i in range(lines):
        #     if i % 2 == 0:
        #         print(range(i if i < int(lines / 2) and i < len(matrix) - 1 else len(matrix) - 1,
        #                     -1 if i < int(lines / 2) else i - len(matrix[0]), -1))
        #         for j in range(i if i < int(lines / 2) and i < len(matrix) - 1 else len(matrix) - 1,
        #                        -1 if i < int(lines / 2) else i - len(matrix[0]), -1):
        #             print(j, ',', i - j)
        #             # result.append(matrix[j][i - j])
        #     else:
        #         print(range(0 if i < int(lines / 2) else i - len(matrix[0]) + 1,
        #                     i + 1 if i <= int(lines / 2) else len(matrix)))
        #         for k in range(0 if i < int(lines / 2) else i - len(matrix[0]) + 1,
        #                        i + 1 if i < int(lines / 2) else len(matrix)):
        #             print(k, ',', i - k)
        #             # result.append(matrix[k][i - k])
        # return result
        result = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return result
        a = b = 0
        for i in range(len(matrix) * len(matrix[0])):
            result.append(matrix[a][b])
            if (a + b) % 2 == 0:
                if b < len(matrix[0]) - 1:
                    a -= 1 if a is not 0 else a
                    b += 1
                else:
                    a += 1
            else:
                if a < len(matrix) - 1:
                    a += 1
                    b -= 1 if b is not 0 else b
                else:
                    b += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.find_diagonal_order([
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]))
    # print(solution.find_diagonal_order([[6, 9, 7]]))
    # print(solution.find_diagonal_order([[7], [9], [6]]))
    # print(solution.find_diagonal_order([
    #     [1, 2, 3, 0],
    #     [4, 5, 6, 0],
    #     [7, 8, 9, 0]
    # ]))
    # print(solution.find_diagonal_order([
    #     [1, 2, 3, 0],
    #     [4, 5, 6, 0],
    #     [7, 8, 9, 0],
    #     [0, 0, 0, 0]
    # ]))
    # print(solution.find_diagonal_order([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]))
    # print(solution.find_diagonal_order([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]))
    print(solution.find_diagonal_order([[1]]))

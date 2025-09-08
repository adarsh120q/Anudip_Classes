class Solution:
    def generate(self, numRows) :
        list1 = []
        list2 = []
        for i in range(1, numRows+1):
            for j in range(i):
                if i ==1 or i == 2 or j==0 or j==i-1:
                    list2.append(1)

                else:
                    list2.append(list1[len(list1)-1][j] + list1[len(list1)-1][j-1])

            list1.append(list2)
            list2 = []


        return list1

m = Solution()
print(m.generate(5))
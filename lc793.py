class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            ans[i] = st[-1] - i if st else 0
            st.append(i)
        
        return ans
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False

            if preMap[crs] == []:
                return True

            seen.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True


        courses = 0

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        
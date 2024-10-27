class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            preReq[course].append(pre)
        
        output, visited, cycle = [], set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for pre in preReq[course]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output
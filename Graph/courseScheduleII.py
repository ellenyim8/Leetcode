# 210 - Course Schedule II

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # prerequisites: List[List[int]]
        # numCourses: int
        # rtype: List[int]
        
        # adjacency list
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # course has 3 possible states
        # visit -> course has been added to res 
        # visiting -> course not added to res, but added to cycle
        # unvisited -> course not added to res or cycle
        # topological sort
        # dfs

        res = []
        visit = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            # only add course after adding prereqs
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return res

        

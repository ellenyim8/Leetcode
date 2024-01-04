# 433. Minimum Genetic Mutation
from collections import deque 
class Solution:
    def minMutation(self, startGene, endGene, bank):
        # each gene str - node
        # mutation - edge
        def getMutations(gene):
            mutations = []
            for i in range(len(gene)):
                for c in 'ACGT':
                    if gene[i] != c:
                        newGene = gene[:i] + c + gene[i+1:]
                        mutations.append(newGene)

            return mutations

        # set()
        bank_set = set(bank)
        q = deque([(startGene, 0)])
        visit = set()
        # bfs():
        #   q = deque()
        #   push startGene into q
        while q:
            gene, depth = q.popleft()
            if gene == endGene:
                return depth
            
            for newGene in getMutations(gene):
                if newGene in bank_set and newGene not in visit:
                    visit.add(newGene)
                    q.append((newGene, depth + 1))

        return -1


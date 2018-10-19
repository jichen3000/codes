# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_set = set(i for i in range(n))
        mem = {}
        for i in range(n):
            if i in n_set:
                for j in range(n):
                    if i == j:
                        continue
                    know = knows(i,j)
                    mem[(i,j)] = know
                    if know:
                        n_set.discard(i)
                        break
                    else:
                        n_set.discard(j)
                else:
                    for j in range(n):
                        if i == j:
                            continue
                        if (j, i) in mem:
                            know = mem[(j,i)]
                        else:
                            know = knows(j,i)
                            mem[(j,i)] = know
                        if not know:
                            n_set.discard(i)
                            break
                        else:
                            n_set.discard(j)
                    else:
                        return i
        return -1
                        
        
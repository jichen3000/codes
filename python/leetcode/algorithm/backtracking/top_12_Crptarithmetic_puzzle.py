# http://www.geeksforgeeks.org/backtracking-set-8-solving-cryptarithmetic-puzzles/
# not smart one, 
# smart one, will limit the possible number by equations
def solves(add_strs, answer_str):
    letters = set()
    for strs in add_strs+[answer_str]:
        for c in strs:
            letters.add(c)
    letters = list(letters)
    n = len(letters)
    if n > 10: return None

    def is_valid(result):
        nums = [ int("".join([result[c] for c in strs])) for strs in add_strs]
        answer = int("".join([result[c] for c in answer_str]))
        return sum(nums) == answer
        
    def get_possible_num(visited):
        return [i for i, v in enumerate(visited) if not v]
        

    def dfs(result, visited):
        if len(result) == n:
            if is_valid(result):
                results.append(result.copy())
                return True
            else:
                return False
        i = len(result)
        for j in get_possible_num(visited):
            # (letters[i],j).p()
            result[letters[i]] = str(j)
            visited[j] = True
            # if dfs(result, visited):
            #     return True
            dfs(result, visited)
            del result[letters[i]]
            visited[j] = False
    # letters = ['m', 'e', 'd', 'o', 'n', 's', 'r', 'y']
    results = []
    result ={}
    visited = [False] * 10
    # result["m"] = "1"
    # visited[1] = True
    dfs(result,visited)
    return results

if __name__ == '__main__':
    from minitest import *

    with test(solves):
        solves(["send","more"],"money").pp()
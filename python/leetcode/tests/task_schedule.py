from collections import Counter
import heapq 
class Solution(object):
    def leastInterval_brutal(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return len(tasks)
        if len(tasks) == 1:
            return 1
        new_tasks = []
        task_index = 0
        task_dict = {}
        while len(tasks) > 0:
            # print("task_index",task_index)
            if task_index >= len(tasks):
                last_new_index = len(new_tasks) - 1
                # print(task_dict)
                min_v = min([n-(last_new_index-index_in_new) for index_in_new in task_dict.values()])
                for j in range(min_v):
                    new_tasks.append("idle")                    
                task_index = 0
                # print("task_index",task_index)

                
            cur_task = tasks[task_index]
            index_in_new = task_dict.get(cur_task,-1-n)
            # print("diff",n-(len(new_tasks) - 1 - index_in_new))
            if n-(len(new_tasks) - 1 - index_in_new) > 0:
                task_index += 1
            else:
                new_tasks.append(tasks[task_index])
                del tasks[task_index]
                task_dict[cur_task] = len(new_tasks)-1
                task_index = 0
        return len(new_tasks)
    
    def leastInterval_passed(self, tasks, n):
        if n < 1:
            return len(tasks)
        if len(tasks) == 1:
            return 1

        task_count_list = Counter(tasks).most_common()
        # print(task_count_list)
        index = 0
        new_tasks = []
        handled_count = 0
        while handled_count < len(tasks):
            count_index = index % (n+1)
            # print("i,ci",index,count_index)
            if count_index >= len(task_count_list):
                new_tasks.append("i")
                # print("new",new_tasks)
            else:
                cur_task, cur_count = task_count_list[count_index]
                new_tasks.append(cur_task)
                handled_count += 1
                # print("new",new_tasks)
                task_count_list[count_index] = (cur_task, cur_count-1)
            # print("task_count_list",task_count_list)
            if count_index == n:
                for i in xrange(min(n, len(task_count_list)-1),-1,-1):
                    cur_task, cur_count = task_count_list[i] 
                    if cur_count == 0:
                        del task_count_list[i]
                task_count_list.sort(key=lambda x: -x[1])
                # print("cleared task_count_list",task_count_list)

            
            index += 1
        # print(new_tasks)
        return len(new_tasks)

    def leastInterval_using_sort(self, tasks, n):
        task_count_list = Counter(tasks).most_common()
        count_list = [count for v, count in task_count_list]
        times = 0
        while count_list[0] > 0:
            index = 0
            while index <= n:
                if count_list[0] == 0:
                    break
                if index < len(count_list) and count_list[index] > 0:
                    count_list[index] -= 1
                times += 1
                index += 1
            count_list.sort(key=lambda x: -x)
        return times

    def leastInterval_using_queue(self, tasks, n):
        task_counter = Counter(tasks)
        count_list = [-v for v in task_counter.values()]
        heapq.heapify(count_list)
        times = 0
        # count_list.p()
        while len(count_list) > 0:
            index = 0
            tmp_list = []
            while index <= n:
                # index.p()
                # count_list.p()
                # tmp_list.p()
                if len(tmp_list) == 0 and len(count_list) == 0:
                    break
                if len(count_list) > 0:
                    cur_count = heapq.heappop(count_list)
                    if cur_count < 0:
                        cur_count += 1
                        if cur_count < 0:
                            tmp_list.append(cur_count)
                times += 1
                index += 1
                # times.p()
            for v in tmp_list:
                # if v < 0:
                heapq.heappush(count_list, v)

        return times

    def leastInterval(self, tasks, n):
        task_counter = Counter(tasks)
        count_list = task_counter.values()
        count_list.sort(key=lambda x: -x)
        # count_list.p()
        max_val = count_list[0] - 1
        idle_slots = max_val * n
        # idle_slots.p()
        for i in xrange(1,len(count_list)):
            idle_slots -= min(count_list[i],max_val)
            # idle_slots.p()
        if idle_slots > 0:
            return idle_slots + len(tasks)
        else:
            return len(tasks)








if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        tasks = ['G','C','A','H','A','G','G','F','G','J','H','C','A','G','E','A','H','E','F','D','B','D','H','H','E','G','F','B','C','G','F','H','J','F','A','C','G','D','I','J','A','G','D','F','B','F','H','I','G','J','G','H','F','E','H','J','C','E','H','F','C','E','F','H','H','I','G','A','G','D','C','B','I','D','B','C','J','I','B','G','C','H','D','I','A','B','A','J','C','E','B','F','B','J','J','D','D','H','I','I','B','A','E','H','J','J','A','J','E','H','G','B','F','C','H','C','B','J','B','A','H','B','D','I','F','A','E','J','H','C','E','G','F','G','B','G','C','G','A','H','E','F','H','F','C','G','B','I','E','B','J','D','B','B','G','C','A','J','B','J','J','F','J','C','A','G','J','E','G','J','C','D','D','A','I','A','J','F','H','J','D','D','D','C','E','D','D','F','B','A','J','D','I','H','B','A','F','E','B','J','A','H','D','E','I','B','H','C','C','C','G','C','B','E','A','G','H','H','A','I','A','B','A','D','A','I','E','C','C','D','A','B','H','D','E','C','A','H','B','I','A','B','E','H','C','B','A','D','H','E','J','B','J','A','B','G','J','J','F','F','H','I','A','H','F','C','H','D','H','C','C','E','I','G','J','H','D','E','I','J','C','C','H','J','C','G','I','E','D','E','H','J','A','H','D','A','B','F','I','F','J','J','H','D','I','C','G','J','C','C','D','B','E','B','E','B','G','B','A','C','F','E','H','B','D','C','H','F','A','I','A','E','J','F','A','E','B','I','G','H','D','B','F','D','B','I','B','E','D','I','D','F','A','E','H','B','I','G','F','D','E','B','E','C','C','C','J','J','C','H','I','B','H','F','H','F','D','J','D','D','H','H','C','D','A','J','D','F','D','G','B','I','F','J','J','C','C','I','F','G','F','C','E','G','E','F','D','A','I','I','H','G','H','H','A','J','D','J','G','F','G','E','E','A','H','B','G','A','J','J','E','I','H','A','G','E','C','D','I','B','E','A','G','A','C','E','B','J','C','B','A','D','J','E','J','I','F','F','C','B','I','H','C','F','B','C','G','D','A','A','B','F','C','D','B','I','I','H','H','J','A','F','J','F','J','F','H','G','F','D','J','G','I','E','B','C','G','I','F','F','J','H','H','G','A','A','J','C','G','F','B','A','A','E','E','A','E','I','G','F','D','B','I','F','A','B','J','F','F','J','B','F','J','F','J','F','I','E','J','H','D','G','G','D','F','G','B','J','F','J','A','J','E','G','H','I','E','G','D','I','B','D','J','A','A','G','A','I','I','A','A','I','I','H','E','C','A','G','I','F','F','C','D','J','J','I','A','A','F','C','J','G','C','C','H','E','A','H','F','B','J','G','I','A','A','H','G','B','E','G','D','I','C','G','J','C','C','I','H','B','D','J','H','B','J','H','B','F','J','E','J','A','G','H','B','E','H','B','F','F','H','E','B','E','G','H','J','G','J','B','H','C','H','A','A','B','E','I','H','B','I','D','J','J','C','D','G','I','J','G','J','D','F','J','E','F','D','E','B','D','B','C','B','B','C','C','I','F','D','E','I','G','G','I','B','H','G','J','A','A','H','I','I','H','A','I','F','C','D','A','C','G','E','G','E','E','H','D','C','G','D','I','A','G','G','D','A','H','H','I','F','E','I','A','D','H','B','B','G','I','C','G','B','I','I','D','F','F','C','C','A','I','E','A','E','J','A','H','C','D','A','C','B','G','H','G','J','G','I','H','B','A','C','H','I','D','D','C','F','G','B','H','E','B','B','H','C','B','G','G','C','F','B','E','J','B','B','I','D','H','D','I','I','A','A','H','G','F','B','J','F','D','E','G','F','A','G','G','D','A','B','B','B','J','A','F','H','H','D','C','J','I','A','H','G','C','J','I','F','J','C','A','E','C','H','J','H','H','F','G','E','A','C','F','J','H','D','G','G','D','D','C','B','H','B','C','E','F','B','D','J','H','J','J','J','A','F','F','D','E','F','C','I','B','H','H','D','E','A','I','A','B','F','G','F','F','I','E','E','G','A','I','D','F','C','H','E','C','G','H','F','F','H','J','H','G','A','E','H','B','G','G','D','D','D','F','I','A','F','F','D','E','H','J','E','D','D','A','J','F','E','E','E','F','I','D','A','F','F','J','E','I','J','D','D','G','A','C','G','G','I','E','G','E','H','E','D','E','J','B','G','I','J','C','H','C','C','A','A','B','C','G','B','D','I','D','E','H','J','J','B','F','E','J','H','H','I','G','B','D']
        Solution().leastInterval(tasks,1).must_equal(1000)
        tasks = ["A","A","B","B","C","C"]
        Solution().leastInterval(tasks,1).must_equal(6)
        tasks = ["A","A","A"]
        Solution().leastInterval(tasks,1).must_equal(5)

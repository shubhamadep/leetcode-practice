# remember it says at least n spaces, so it can have more in between as well. 
# so when we create max idle_time we use max_freq. once idle_time is used up, we can add all the taks without # idle time. 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        counts = collections.Counter(tasks)
        frequencies = [counts[x] for x in counts]
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
        
        
        
        
        
        
        
        
        
        
        
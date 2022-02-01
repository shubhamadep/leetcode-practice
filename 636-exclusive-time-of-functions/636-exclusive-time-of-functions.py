class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        helper = lambda log: (int(log[0]), log[1], int(log[2])) # to covert id and time to integer
        logs = [helper(log.split(':')) for log in logs]         # convert [string] to [(,,)]
        ans, s = [0] * n, []                                    # initialize answer and stack
        for (i, status, timestamp) in logs:                     # for each record
            if status == 'start':                               # if it's start
                if s: ans[s[-1][0]] += timestamp - s[-1][1]     # if s is not empty, update time spent on previous id (s[-1][0])
                s.append([i, timestamp])                        # then add to top of stack
            else:                                               # if it's end
                ans[i] += timestamp - s.pop()[1] + 1            # update time spend on `i`
                if s: s[-1][1] = timestamp+1                    # if s is not empty, udpate start time of previous id; 
        return ans
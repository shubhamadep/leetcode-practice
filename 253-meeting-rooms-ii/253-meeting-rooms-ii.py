class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        heapm = []

        intervals.sort(key=lambda y: y[0])

        heapq.heappush(heapm, intervals[0][1])

        for i in intervals[1:]:

            if heapm[0] <= i[0]:
                heapq.heappop(heapm)


            heapq.heappush(heapm, i[1])


        return len(heapm)
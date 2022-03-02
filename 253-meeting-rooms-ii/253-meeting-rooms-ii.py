class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals = sorted(intervals, key= lambda x: x[0])
        
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval[1])
            else:
                earliest_end = heap[0]
                current_start, current_end = interval
                if earliest_end <= current_start:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval[1])
        
        return len(heap)
        
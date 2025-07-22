class Solution(object):
    def averageWaitingTime(self, customers):
    #     # max avrage waiting time = k
    #     # output: how many min chef to work on orders so that they can meet k
    #     binary_search(1, len(customers)):
    #     # do you have a more efficient algorithm
    #         can_they_finish(customers, k, num_chef)
   
    # def can_they_finish(customers, max_wait_time, num_chef):
    #     # [1,2] [2,5]
    #     # [1,5] [2,2]
    #     # think from simple to complex data structure
    #     # - array, maybe but a long time implement
    #     # - object/hash_map: even more confused
    #     # - linked list: not gonna work
    #     # - queue, deque: left right append and pop, does not help
    #     # - tree: does not help
    #     # - heap: min-heap, finish_time
    #     heap = [0] * num_chef
    #     wait_time = 0
    #     for arrival, duration in customer:
    #         min_finish_time = heapq.heappop(heap)
    #         if min_finish_time < arrival:
    #             new_finish_time = arrival + duration
    #             heapq.heappush(heap, new_finish_time)
    #             wait_time += duration
    #         else:
    #             new_finish_time = min_finish_time + duration
    #             heapq.heappush(heap, new_finish_time)
    #             wait_time += new_finish_time - arrival
    #     return float(wait_time)/len(customers) <= max_wait_time
        
        

        # go through customers
        # track the actual time going
        # for each customer we substract the actual time and arrival
        curr_time = 0
        wait_time = 0
        # ------
        #.  *
        #       *****
        #      &
        #            &&&&
        # waiting = []
        
        for arrival, duration in customers:
            # actual_time += duration
            # print(actual_time)
            # waiting.append(arrival + actual_time) 
            # print(waiting)
            if curr_time >= arrival:
                finish_time = curr_time + duration
                curr_time = finish_time
                wait_time += finish_time - arrival
            else:
                finish_time = arrival + duration
                curr_time = finish_time
                wait_time += finish_time - arrival

        return float(wait_time) / len(customers)


    #     chef_time = 0
    #     customer_index = 0
    #     wait_time = 0
    #     while customer_index < len(customers):
    #         arrival, duration = customers[customer_index]
    #         if chef_time >= arrival:
    #             chef_time += duration
    #             customer_index += 1
    #             wait_time += chef_time - arrival
    #         else:
    #             chef_time = arrival

    # return wait_time / len(customers)

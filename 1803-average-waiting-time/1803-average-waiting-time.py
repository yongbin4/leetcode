class Solution(object):
    def averageWaitingTime(self, customers):
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


'''
        chef_time = 0
        customer_index = 0
        wait_time = 0
        while customer_index < len(customers):
            arrival, duration = customers[customer_index]
            if chef_time >= arrival:
                chef_time += duration
                customer_index += 1
                wait_time += chef_time - arrival
            else:
                chef_time = arrival

        return wait_time // len(customers)
'''
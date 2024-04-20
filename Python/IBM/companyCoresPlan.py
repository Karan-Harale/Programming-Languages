def minCost(n, k, plans):

    sortedPlans = sorted(plans, key = lambda x: x[3])

    print(sortedPlans)

    count = 0

    totalCost = 0

    for day in range(1, n+1):
        rem = k
        print("day: ",day, "rem: ", rem)

        for plan in sortedPlans:
            count+=1
            print(plan , "count: ",count)

            start , end, core, price = plan

            print(start , end, core, price)


            if start <= day <=end:

                core = min(core, rem)

                print("core: ",core)

                cost = price * core

                print("cost: ", cost)

                rem -= core

                print("rem: ",rem)

                totalCost += cost

                print("totalCost: ",totalCost , "\n")

                if rem == 0:
                    break
    # return totalCost





n = 5
k = 7

plans = [[1, 3, 5, 2],[1, 4, 5, 3],[2, 5, 10, 1]]

print(minCost(n, k, plans))
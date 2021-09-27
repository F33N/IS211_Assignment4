import time
import random


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    timeTaken = end - start

    return [found, timeTaken]


def ordered_sequential_search(a_list, item):
    start = time.time()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            stop = True
        else:
            pos = pos + 1

    end = time.time()
    timeTaken = end - start
    return [found, end - start]


def binary_search_recursive(a_list, item):
    start = time.time()

    found = False
    low = 0
    high = len(a_list) - 1

    while low <= high:
        middle = (low + high) // 2
        if a_list[middle] == item:
            found = True
        elif item < a_list[middle]:
            high = middle - 1
        elif item > a_list[middle]:
            low = middle + 1

    end = time.time()

    return [found, end - start]


def binary_search_iterative(a_list, item):
    start = time.time()

    if len(a_list) > 0:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_iterative(a_list[:midpoint], item)
            else:
                return binary_search_iterative(a_list[midpoint + 1:], item)
    else:
        end = time.time()
        timeTaken = end - start

        return [False, timeTaken]


def main():
    listSizes = [500, 1000, 10000]
    for i in listSizes:
        ss_sum = 0
        oss_sum = 0
        bsr_sum = 0
        bsi_sum = 0
        for j in range(100):
            randomList = random.sample(range(1, 100000), i)

            ss_return = sequential_search(randomList, -1)

            randomList.sort()

            oss_return = ordered_sequential_search(randomList, -1)
            bsr_return = binary_search_recursive(randomList, -1)
            bsi_return = binary_search_iterative(randomList, -1)

            ss_sum = ss_sum + ss_return[1]
            oss_sum = oss_sum + oss_return[1]
            bsr_sum = bsr_sum + bsr_return[1]
            bsi_sum = bsi_sum + bsi_return[1]

        average_ss = ss_sum / 100
        average_oss = oss_sum / 100
        average_bsr = bsr_sum / 100
        average_bsi = bsi_sum / 100

        print("Sequential Search took %10.7f seconds to run, on average" % average_ss)
        print("Ordered Sequential Search took %10.7f seconds to run, on average" % average_oss)
        print("Binary Search Recursive took %10.7f seconds to run, on average" % average_bsr)
        print("Binary Search Iterative took %10.7f seconds to run, on average" % average_bsi)
        print("\n")


if __name__ == "__main__":
    main()
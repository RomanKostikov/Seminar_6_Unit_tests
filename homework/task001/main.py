from homework.task001.task_1 import NumsLists


def main():
    # Create an instance of NumsLists
    num_lists = NumsLists([1, 2, 3], [4, 5, 6])

    # Get the averages of the lists
    averages = num_lists.get_lists_averages()

    # Print the averages
    print(f"The average of list 1 is: {averages[0]}")
    print(f"The average of list 2 is: {averages[1]}")
    # Call the compare_averages method
    num_lists.compare_averages()


if __name__ == "__main__":
    main()

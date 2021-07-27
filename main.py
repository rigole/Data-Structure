# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""def commonElts(list1, list2):

    #list1 = ['a', 'b','c','d']
    #list2 = ['x', 'y','m','z']

    for i in list1:
      for j in list2:
        if i == j:
          return True


list3 = ['a', 'b', 'c', 'd']
    list4 = ['x', 'y', 'r', 'z']

    test = commonElts(list3, list4)
    print(test)

    return False  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script."""
if __name__ == '__main__':
    list4 = ['a', 'b', 'c', 'd']
    #print(list4[2])

    # add elements at the end of the list
    list4.append('e')  # O(1)
    # remove elements at the end of the list
    list4.pop()  # O(1)
    list4.pop()  # O(1)
    # add elements at one index of the list
    list4.insert(0, 'x')
    list4.insert(2, 'alien')    # O(n/2)
    print(list4)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

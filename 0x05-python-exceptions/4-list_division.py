#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i, n in zip(my_list_1, my_list_2):
        try:
            if i / 1 == i or n / 1 == n:
                if n != 0:
                    result = i / n
                    new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
        finally:
            print(new_list)

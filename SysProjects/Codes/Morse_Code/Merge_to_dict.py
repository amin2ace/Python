
# Convert two lists af numeric and alphabet ex. to a dictionary that first list's items are key nad the others are value
def merge(list_as_keys, list_as_values): #could be use another parameter as below comment s--> Straight & r--> Reverse
    # Straight & Reverse will be change keys and values position with each other
    try:
        assert len(list_as_keys) == len(list_as_values)

    except AssertionError:
        print("### Two lists must have the same number of elements ###")

    else:
            my_dict = {}
            for i in range(len(list_as_keys)):
                my_dict[list_as_keys[i]] = list_as_values[i] 
                i += 1  
            return my_dict
        
def main():
    first_list = ['a','b','c']
    a = '.'
    b = '-'
    second_list = [a+b, 2*a+b, 3*b+a]
    print(merge(second_list, first_list))



if __name__ == "__main__": main()
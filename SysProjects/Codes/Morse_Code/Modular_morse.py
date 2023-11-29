


### Make a list of numeric from start to end
def get_list_n(start = 0, end = 9):

    numbers_list = list()
    for i in range(int(start), int(end)+1):
        numbers_list.append(chr(i))
    return numbers_list


### Make a list of alphabet from start to end
def get_list_a(start = 'a', end = 'z'):

    alphabet_list = list()

    for i in range(ord(start), ord(end)+1):
        alphabet_list.append(chr(i))

    return alphabet_list



### Convert two lists af numeric and alphabet ex. to a dictionary that first list's items are key nad the others are value
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



### Encode the given message with a 'key' for cipher ceaser methode or a 'code dictonary' for converting method like morses 
def encode(message, code_table_s = 0, key = 0):

    encoded_message = ""
    if key:
        
        for i in message:
            encoded_message += chr(ord(i) + key)
        return encoded_message

    elif code_table_s:
        for i in message:
            if i == ' ':
                encoded_message += ' '
            else:
                j = code_table_s[i]
                encoded_message += j
                encoded_message += ' '
        return encoded_message

### Decode the given message with a 'key' for cipher ceaser methode or a 'code dictonary' for converting method like morses 
def decode(message, code_table_r = 0, key = 0):
  
    decoded_message = ""
    if key:
        
        for i in message:
            decoded_message += chr(ord(i) - key)
        return decoded_message

    elif code_table_r:
        message = list(message.split('  '))
        lenght_of_list = len(message)
        for a in range(lenght_of_list):
            for i in str(message[a]).split(' '):
                if i == ' ':
                    decoded_message += ' '
                else:
                    j = code_table_r[i]
                    decoded_message += j
            decoded_message += ' '
        return decoded_message




### First Build a dictionary of key and value for converting table
def build_morse_dict(en_or_de):

    list_of_alphabet = get_list_a()
    list_of_numeric = get_list_n()
    list_of_alphabet.extend(list_of_numeric)
    d = '.'
    a = '-'
    alphabet_morse_list = [(d+a), (a+3*d), (a+d)*2, (a+2*d), d, (2*d+a+d), (2*a+d), (4*d), (2*d), (d+3*a),
                           (a+d+a), (d+a+2*d), (2*a), (a+d), (3*a), (d+2*a+d), (2*a+d+a), (d+a+d),
                           (3*d), (a), (2*d+a), (3*d+a), (d+2*a), (a+2*d+a), (a+d+2*a), (2*a+2*d)
    ]
    numeric_morse_list = [5*a, d+4*a, 2*d+3*a, 3*d+2*a, 4*d+a, 5*d, a+4*d,
                          2*a+3*d, 3*a+2*d, 4*a+d]
    
    alphabet_morse_list.extend(numeric_morse_list)
    if en_or_de in 'Ee':
        morse_dict = merge(list_of_alphabet, alphabet_morse_list)
        return morse_dict
    else:
        morse_dict = merge(alphabet_morse_list, list_of_alphabet)
        return morse_dict

### Depending of with methode Encode or decode, does the converting and give the converted message
def convert(message, dict, methode):
    
    final_message = ""
    if methode in 'Ee':
        final_message = encode(message, dict)
    elif methode in 'Dd':
        final_message = decode(message, dict)
    return final_message




def main():
    
    while 1:
        en_or_de = input("Do you want encode or decode? E / D:  ")

        try:
            assert en_or_de in 'EeDd'

        except AssertionError:
            print("Please insert 'e' for encode and 'd' for decode!")

        else:
            builted_dict = build_morse_dict(en_or_de)
            input_message = input("Enter Your Message: ")
            print(convert(input_message, builted_dict, en_or_de))



if __name__ == "__main__": main()

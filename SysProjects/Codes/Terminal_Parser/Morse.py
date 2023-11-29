import argparse

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
### Decode or Encode based on Ceaser cipher methode
def ceaser(message_items, key, en):
    message = ' '.join(message_items)
    if en in 'Ee':
        encoded_text = ""
        for ch in message:
            i = ord(ch) + key
            if i > 127: i -= 95
            encoded_text += chr(i)
        return encoded_text
    elif en in 'Dd':
        decoded_text = ""
        for ch in message:
            i = ord(ch) - key
            if i < 32: i += 95
            decoded_text += chr(i)
        return decoded_text
    else:
        return 0


### Encode the given message with a 'key' for cipher ceaser methode or a 'code dictonary' for converting method like morses 
def encode(message_items, code_table_s = 0, key = 0):
    
    encoded_message = ""
    if key:
        message = ' '.join(message_items)
        for i in message:
            encoded_message += chr(ord(i) + key)
        return encoded_message

    elif code_table_s:
        message = '_'.join(message_items)
        print(message)
        for i in message:
            if i == '_':
                encoded_message += '_'
            else:
                j = code_table_s[i]
                encoded_message += j
                encoded_message += ' '
        return encoded_message

### Decode the given message with a 'key' for cipher ceaser methode or a 'code dictonary' for converting method like morses 
def decode(message_items, code_table_r = 0, key = 0):
    
    decoded_message = ""
    if key:
        message = str(message_items[0])
        for i in message:
            decoded_message += chr(ord(i) - key)
        return decoded_message

    elif code_table_r:
        message = ' '.join(message_items)
        message
        print(message)
        for index, code in enumerate(message):
            #for i in str(message[a]).split(' '):
            if code == '_':
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
def morse(message, dict, en):
    
    final_message = ""
    if en in 'Ee':
        final_message = encode(message, dict)
    elif en in 'Dd':
        final_message = decode(message, dict)
    return final_message




def main():
    args = argparse.ArgumentParser()

    while 1:
        
        args.add_argument("method", help="The cipher method is Ceaser based or Morse based")
        args.add_argument("act", default="e", help="Action to Encodeing or Decoding (e\d)")
        args.add_argument("key", type=int, default=2, help="Number for Ceaser based key (int)")
        args.add_argument("message", nargs="*", help="The message to encode / Encoded message to decode")
  
        inputs = args.parse_args()

        try:
            if inputs.method not in ['ceaser','morse']: raise ValueError
        except ValueError:
            print("method argument takes only ceaser or morse")
        else:
            if inputs.method == "ceaser":
                print(inputs.message)
                print("\n")
                if inputs.act in 'Ee':
                    print(f"Cipher Ceaser:{encode(inputs.message, 0, int(inputs.key))}\n")
                elif inputs.act in 'Dd':
                    print(inputs.message)
                    print(f"Cipher Ceaser:{decode(inputs.message, 0, int(inputs.key))}\n")
            else:
                print(inputs.message)
                print(inputs.act)
                print('\n')
                if inputs.act in 'Ee':
                    print(f"Morse Ceaser:{encode(inputs.message, build_morse_dict(inputs.act), 0)}\n")
                elif inputs.act in 'Dd':
                    print(f"Morse Ceaser:{decode(inputs.message, build_morse_dict(inputs.act), 0)}\n")
        '''try:
            if inputs.method != 'ceaser' and inputs.method != 'morse': raise AssertionError
        except AssertionError:
            print("Please insert 'ceaser' for ceaser cipher and 'morse' for morse cipher!")
        else:
            try:
                if inputs.act not in 'EeDd': raise ValueError
            except ValueError:
                print("Please insert 'e' for encode and 'd' for decode!")
            else:
                builted_dict = build_morse_dict(inputs.act)
                input_message = inputs.message
                if inputs.method == 'morse':
                    print(convert(input_message, builted_dict, inputs.act))
                else:
                    get_key = inputs.key
                    try:    #Cipher key must be a number up 110,000 and positive
                        assert int(get_key) > 0
                    except AssertionError:
                        print("#### The key must be a digit, non zero and positive ####\n")
                    else:
                        cipher_key = int(get_key)
                        ceaser(input_message, cipher_key, inputs.act)
                        ceaser(input_message, cipher_key, inputs.act)
        '''



if __name__ == "__main__": main()

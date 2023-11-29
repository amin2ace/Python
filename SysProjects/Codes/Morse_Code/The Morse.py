
import Merge_to_dict
import Alphabet_list
import Numeric_list
import Encode_Decode_madule

### First Build a dictionary of key and value for converting table
def build_morse_dict(en_or_de):

    list_of_alphabet = Alphabet_list.get_list()
    list_of_numeric = Numeric_list.get_list()
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
        morse_dict = Merge_to_dict.merge(list_of_alphabet, alphabet_morse_list)
        return morse_dict
    else:
        morse_dict = Merge_to_dict.merge(alphabet_morse_list, list_of_alphabet)
        return morse_dict

### Depending of with methode Encode or decode, does the converting and give the converted message
def convert(message, dict, methode):
    
    final_message = ""
    if methode in 'Ee':
        final_message = Encode_Decode_madule.encode(message, dict)
    elif methode in 'Dd':
        final_message = Encode_Decode_madule.decode(message, dict)
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
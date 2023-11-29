
import Merge_to_dict

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

def main():
    first_list = ['a','b','c']
    a = '.'
    b = '-'
    second_list = [a+b, 2*a+b, 3*b+a]

    my_dict = Merge_to_dict.merge_to_dict(second_list, first_list)# lists sequences are important for keys and values

    print(decode(".- ..- ---.  .- ---. ..-  ..- ---.", my_dict))


if __name__ == "__main__": main()

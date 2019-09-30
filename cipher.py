# An encoder/decoder for our spies to secretly send messages.

#encryption_option = raw_input("Would you like to Encode or Decode? ") 
encryption_option = input("Would you like to Encode or Decode? ") 

# should_encode will be true if the user 
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()

# Ask the user for their message and cipher number.
upcase_list = [chr(i) for i in range(65, 91)]
lowcase_list = [chr(i) for i in range(97, 123)]
if should_encode:
    # Your code here!
    user_cipher = int(input('What is your cipher number? '))
    user_message = input('What is your message? ')
    output_message = ''
    for i in user_message:
        if i in upcase_list:
            new_index = upcase_list.index(i) + user_cipher
            if new_index > 25: new_index = (new_index % 25) - 1
            output_message += upcase_list[new_index]
        elif i in lowcase_list:
            new_index = lowcase_list.index(i) + user_cipher
            if new_index > 25: new_index = (new_index % 25) - 1
            output_message += lowcase_list[new_index]
        else:
            output_message += i
    print(output_message)
elif should_decode:
    user_cipher = int(input('What is your cipher number? '))
    user_message = input('What is your message? ')
    output_message = ''
    for i in user_message:
        if i in upcase_list:
            new_index = upcase_list.index(i) - user_cipher
            #if new_index < 0: new_index = ((-1 * new_index) % 25) - 1
            output_message += upcase_list[new_index]
        elif i in lowcase_list:
            new_index = lowcase_list.index(i) - user_cipher
            #if new_index > 25: new_index = (new_index % 25) - 1
            output_message += lowcase_list[new_index]
        else:
            output_message += i
    print(output_message)
else:
    # Print a nice notice that we only support encrypt/decrypt
    # Your code here!
    print('Sorry, we only support encoding and decoding.')

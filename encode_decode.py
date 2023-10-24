#Nicholas Thyssen Code
#Takes in a string version of what user inputed, and then looks at each individual num in string and adds three. (if num is 9, goes to 0).
def encode(code_string):
    answer= ""

    #This goes trough string. Although we know size is always 8, it allows for other sizes to be tested as well.
    for num in code_string:
        val= int(num)

        #This just runs three times so that same code isn't copied three times.
        for i in range(0,3):
            if val == 9:
                val= 0
            else:
                val+= 1

        answer+= str(val)

    return answer

def decode(encoded_string):
    #To be implemented by partner
    return 0

if( __name__ == '__main__'):
    #Will always run until code hits a break
    while True:
        #Pritns menu and gets option from user input
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit \n")
        option= int(input("Please enter an option:"))

        #Will take value of password as a string and encode to the adding each number by 3 rule
        if option == 1:
            encoded_val= encode(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored! \n")

        #This will undo the actions done in encode and takes in the string value of encoded_val
        elif option == 2:
            decoded_val= decode(encoded_val)
            print(f"The encoded password is {encoded_val}, and the original password is {decoded_val}. \n")

        #When 3 is inputed as option code will end as break will take the code out of while loop
        elif option == 3:
            break
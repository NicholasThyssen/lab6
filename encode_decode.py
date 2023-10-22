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
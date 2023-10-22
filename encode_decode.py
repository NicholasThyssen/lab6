def encode(code_string):
    answer= ""
    for num in code_string:
        val= int(num)
        for i in range(0,3):
            if val == 9:
                val= 0
            else:
                val+= 1
        answer+= str(val)
    return answer
print(encode("00009962"))
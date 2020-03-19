#Not sure if str1[0] needs to be mapped to str2[0],
#str1[1] to str2[1] is so forth or if str1[0] is free
#to map to str2[0] or str2[10000].

#This is solving for first senario. 

#Using Python3

def is_one_to_one_mappable(str1, str2):
    if len(str1) != len(str2):
        return("false")

    #Highest unicoode value of ord() is 65535
    marked = [False] * 65536
    mapped = [-1] * 655356

    #Loops through
    for i in range(len(str1)):
        #If char in str1 hasn't been mapped before,
        if mapped[ord(str1[i])] == -1:
            #Check if corresponding char in str2 has been mapped.
            #If yes, then return false.
            if marked[ord(str2[i])] == True:
                return("false")
            #If not, then mark the char in str1 as True (already seen)
            #and mark the ord position as the value of str2. 
            marked[ord(str2[i])] = True
            mapped[ord(str1[i])] = str2[i]

        #If char in str1 has been mapped already,
        #check if it wasn't previously mapped to same char.
        #If it wasn't, then false. 
        elif mapped[ord(str1[i])] != str2[i]:
            return("false")
    return ("true")

print(is_one_to_one_mappable("abc", "bcd"))
print(is_one_to_one_mappable("foo", "boo"))
print(is_one_to_one_mappable("bar", "foo"))
print(is_one_to_one_mappable("bar", "foo"))
  

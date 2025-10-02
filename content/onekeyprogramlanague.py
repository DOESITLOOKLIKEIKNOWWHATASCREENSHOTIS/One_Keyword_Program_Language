caps = 0

def capslock():
    #Get caps form the global workplace
    global caps
    
    #0 is false in python
    if caps:
        caps = 0
    else:
        caps = 1

#Keyboard setup. The second item in the list is if caps == 1.
Keyboard = [
[capslock, capslock],
#Enter, spacebar
["\n", " "],
#Tab
["   ", "   "],
["`", "~"],
["z", "Z"],
["a", "A"],
["q","Q"],
["1","!"],
["x","X"],
["s","S"],
["w", "W"],
["2", "@"],
["c", "C"],
["d", "D"],
["e", "E"],
["3", "#"],
["v", "V"],
["f", "F"],
["r", "R"],
["4", "$"],
["b", "B"],
["g", "G"],
["t", "T"],
["5", "%"],
["n", "N"],
["h", "H"],
["y", "Y"],
["6", "^"],
["m", "M"],
["j", "J"],
["u", "U"],
["7", "&"],
[",", "<"],
["k", "K"],
["i", "I"],
["8", "*"],
[".", ">"],
["l", "L"],
["o", "O"],
["9", "("],
["/", "?"],
[";", ":"],
["p", "P"],
["0", ")"],
["'", '"'],
["[", "{"],
["-", "_"],
["]", "}"],
["=", "+"],
['\\',"|"]
]

#Main
def main():
    #Opens the file to read
    f = open("code.onekey", "r")
    
    #Gets the length of the code 
    length = open("code.onekey", "r")
    
    #The string to write to file when done
    string = ""
    
    #Checks if the line of code is even or odd.
    count = 1
    
    #The location of the list 
    location = 0
    
    #Start a loop for that handles each line of code 
    for x in length.readlines():
        #Strip the line of it's \n 
        currentlineofcode = (f.readline()).rstrip()
        
        
        #Is the line a 1, empty, or a comment?
        if currentlineofcode == "1":
            
            #Is it a even line 
            if count:
                #If the program hits the final location, reset location
                
                location = location + 1
                
                if location  == (len(Keyboard) - 1):
                    location = 0
                
            else:
                
                #Is the location at Keyboard a string?
                if isinstance(Keyboard[location][caps], str):
                    
                    #Appened string with location and if capslock is on.
                    string = f"{string}{Keyboard[location][caps]}"
                else:
                    
                    #That means it's a function SHOULD be a function
                    Keyboard[location][caps]()
            
        #0 is false in python
        if count:
            count = 0
        else:
            count = 1
    #End of for loop
    
    #Create a new file 
    newfile = open("onekeyresult.py", "w")
    
    #Write string.
    newfile.write(string)

#Only run if the user directly opens the file
if __name__ == "__main__":
    main()
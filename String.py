# string
mystr = " Avi is a good boy"
print(mystr)
print(mystr[0:5])           #resolves from 0 to 4 , '5' is negleted
print(mystr[0:5:2])         #resolves from 0 to 4 first and '2' skips every second character
print(mystr[-8:-2])         #resolves also negative order but condition that is large -ve to small -ve value
print(mystr[::-1])          #makes reverse the string and '-2' will skip evrery 2nd value
print(len(mystr))

# String Functions

print(mystr.isalnum())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())           # for more string functions visit "w3school". or search "string function in python "
print(mystr.find("Avi"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))

# escape characters
txt = 'It\'s alright.'                              # \'	Single Quote
print(txt)

txt = "This will insert one \\ (backslash)."        #\\	Backslash
print(txt)

txt = "Hello\nWorld!"                               #\n	New Line
print(txt)

txt = "Hello\rWorld!"                               #\r	Carriage Return
print(txt)
 # And Many
                                                    #\t	Tab
                                                    #\b	Backspace
                                                    #\f	Form Feed
                                                    #\ooo	Octal value
                                                    #\xhh	Hex value
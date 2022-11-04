dict1 = input("word:\t")
dict2 = {"Variable": "Փոփոխական",
         "Declaration": "Հայտարարում",
         "Assignment": "Վերագրում",
         "Data types": "Տվյալների տիպեր",
         "Integer": "Թվային տիպ",
         "String": "Տողային տիպ",
         "Boolean": "Բուլյան տիպ",
         "true": "Ճշմարիտ",
         "else": "Հակառակ դեպքում",
         "array": "Զանգված",
         "if": "Եթե",
         "false": "Կեղծ"}
if dict1 in dict2.keys():
    print(f" word means: {dict2[dict1]}")
else:
    print(f"we cant find the word: [dict1]")

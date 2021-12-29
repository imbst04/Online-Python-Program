'''
Author:     Muhammad Arif Arain
email:      imbst04@gmail.com
'''
# Variables declaration
assignment = "Assignment # 5";
chStar, chEqual,chMultiple = "*", "=", 70;
authorName,authorEmail = "Muhammad Arif", "imbst04@gmail.com";
strSeprator = chStar*int(chMultiple/4) + chEqual*int(chMultiple/2) + chStar*int(chMultiple/4);
strFooter = f"\n\n{chStar*chMultiple} \n\t\t{authorName} ({authorEmail})\n{chStar*chMultiple}";
strAssign = '''Write a Python program which accepts the user's first and last name 
and print them in reverse order with a space between them''';



# Print the Assignment number as header
print(f"\n{strSeprator}");
print("\t\t\t",assignment);
print(f"{strSeprator}\n{strAssign}\n{chStar*chMultiple}\n");

# method to print string in reverse
def StringInReverse(str):
    l = len(str);
    for i in range(l):
        print(str[l-i-1], end=" ");


# Get input from the user 
fName = input("Enter your first name: ");
lName = input("Enter your last name: ");

# Call the function with parameter
print("\nOutput:\n");
StringInReverse(fName);
StringInReverse(lName);



print(strFooter);
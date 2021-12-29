'''
Author:     Muhammad Arif Arain
email:      imbst04@gmail.com
'''
# Variables declaration
assignment = "Assignment # 6";
chStar, chEqual,chMultiple = "*", "=", 70;
authorName,authorEmail = "Muhammad Arif", "imbst04@gmail.com";
strSeprator = chStar*int(chMultiple/4) + chEqual*int(chMultiple/2) + chStar*int(chMultiple/4);
strFooter = f"\n\n{chStar*chMultiple} \n\t\t{authorName} ({authorEmail})\n{chStar*chMultiple}";
strAssign = '''Write a Python program which takes two inputs from user and prints them addition''';



# Print the Assignment number as header
print(f"\n{strSeprator}");
print("\t\t\t",assignment);
print(f"{strSeprator}\n{strAssign}\n{chStar*chMultiple}\n");

# Getting input from user and generating output as adition of two integers
print("Addition of two numbers:")
try:
    n1 = int(input("Enter first Number: "))
    n2 = int(input("Enter second Number: "))

    print("\nAddition of two given numbers is: ", n1 + n2)
except Exception:
    print("Invalid Input!")

print(strFooter);
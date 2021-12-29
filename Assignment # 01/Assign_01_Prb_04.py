'''
Author:     Muhammad Arif Arain
email:      imbst04@gmail.com
'''
# Variables declaration
assignment = "Assignment # 4";
chStar, chEqual,chMultiple = "*", "=", 70;
authorName,authorEmail = "Muhammad Arif", "imbst04@gmail.com";
strSeprator = chStar*int(chMultiple/4) + chEqual*int(chMultiple/2) + chStar*int(chMultiple/4);
strFooter = f"\n{chStar*chMultiple} \n\t\t{authorName} ({authorEmail})\n{chStar*chMultiple}"
strAssign = "Write a Python program which accepts the Radius of a Circle from the user and compute the Area"


# Print the Assignment number as header
print(f"\n{strSeprator}");
print("\t\t\t",assignment);
print(f"{strSeprator}\n {strAssign}\n{chStar*chMultiple}\n");

# Receiving Radius as input from user
PI = 3.1415926535897932384626433832795;

# Getting the input from the user (The radius of a circle)
cRadius = float(input("Enter the Radius of a Circle: "))

# Calculating the area of a circle
cArea = PI * cRadius**2;

# Printing the output after calculating the area
print("Area of a Circle is:  %.2f" %cArea);


# Print the Author name as Footer
print(strFooter);
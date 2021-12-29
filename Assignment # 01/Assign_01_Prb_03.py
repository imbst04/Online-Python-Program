'''
Author:     Muhammad Arif Arain
email:      imbst04@gmail.com
'''
from datetime import datetime

# Variables declaration
assignment = "Assignment # 3";
chStar, chEqual,chMultiple = "*", "=", 70;
authorName,authorEmail = "Muhammad Arif", "imbst04@gmail.com";
strSeprator = chStar*int(chMultiple/4) + chEqual*int(chMultiple/2) + chStar*int(chMultiple/4);
strFooter = f"\n{chStar*chMultiple} \n\t\t{authorName} ({authorEmail})\n{chStar*chMultiple}"
strAssign = "Write a Python program to display the current date and time";


# Print the Assignment number as header
print(f"\n{strSeprator}");
print("\t\t\t",assignment);
print(f"{strSeprator}\n {strAssign}\n{chStar*chMultiple}\n");

print(f"The current Date and Time of your system is:\n{datetime.today()}");

# Print the Author name as Footer
print(strFooter);
'''
Author:     Muhammad Arif Arain
email:      imbst04@gmail.com
'''
import sys
import platform

# Variables declaration
assignment = "Assignment # 4";
chStar, chEqual,chMultiple = "*", "=", 70;
authorName,authorEmail = "Muhammad Arif", "imbst04@gmail.com";
strSeprator = chStar*int(chMultiple/4) + chEqual*int(chMultiple/2) + chStar*int(chMultiple/4);
strFooter = f"\n{chStar*chMultiple} \n\t\t{authorName} ({authorEmail})\n{chStar*chMultiple}"
strAssign = "Write a Python program to get the Python version you are using";


# Print the Assignment number as header
print(f"\n{strSeprator}");
print("\t\t\t",assignment);
print(f"{strSeprator}\n {strAssign}\n{chStar*chMultiple}\n");

# Print the current version of the python I am using...
print("Current Version of Python:");
print(sys.version);
# Print the virsion info
print(sys.version_info);

# Another way to check python version
print(f"\n\n{chStar*70}\nAnoth way to check Python Version");
print(platform.python_version());

# Print the Author name as Footer
print(strFooter);
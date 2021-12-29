'''
Author:     Muhammad Arif Arain
email:      imbst04@gmail.com
'''
# Variables declaration
assignment = "Assignment # 1";
chStar, chEqual,chMultiple = "*", "=", 70;
authorName,authorEmail = "Muhammad Arif", "imbst04@gmail.com";
strSeprator = chStar*int(chMultiple/4) + chEqual*int(chMultiple/2) + chStar*int(chMultiple/4);
strFooter = f"\n\n{chStar*chMultiple} \n\t\t{authorName} ({authorEmail})\n{chStar*chMultiple}";
strAssign = '''Write a Python program to print the following string in a specific format (See the output).
	Twinkle, twinkle, little star,
		How I wonder what you are!
			Up above the world so high,
			Like a diamond in the sky.
	Twinkle, twinkle, little star,
		How I wonder what you are!
''';

# Print the Assignment number as header
print(f"\n{strSeprator}");
print("\t\t\t",assignment);
print(f"{strSeprator}\n{strAssign}\n{chStar*chMultiple}\n");

# Format of a string
print("\n\n Output:\n")
print("\tTwinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\tUp above the world so high,\n\t\t\tLike a diamond in the sky.\n\tTwinkle, twinkle, little star,\n\t\tHow I wonder what you are!")

print(strFooter)
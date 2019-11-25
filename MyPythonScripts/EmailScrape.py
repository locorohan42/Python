#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 412-434-0000, 555-0000, (434) 555-0000, 444-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\))))?
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s | x)
(\d{2, 5}))?
)
''', re.VERBOSE)
# regex for email
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+

''', re.VERBOSE)
# Todo Get text off clipboard
text = pyperclip.paste()
# Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(extractedEmail)
#print(extractedPhone)
# Copy extracted to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' +  '\n'.join(extractedEmail)
pyperclip.copy(results)

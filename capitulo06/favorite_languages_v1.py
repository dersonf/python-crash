#!/usr/bin/python3

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print()

for name in favorite_languages.keys():
    print(name.title())
print()

for name in favorite_languages:
    print(name.title())
print()

for name in favorite_languages:
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
print()

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print()

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, tank you for taking the poll.")
print()

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print()

for language in set(favorite_languages.values()):
    print(language.title())

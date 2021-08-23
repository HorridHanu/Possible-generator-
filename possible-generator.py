#!/usr/bin/python3
#
#  [Program]
#
#  Pg
#  Possible-generator
#
#  [Author]
#  HorridHanu
#
#
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#
#  See 'LICENSE' for more information.




""" Let's do some serious work. This will a mess of code. But ..... Who cares :(  """



from datetime import datetime
from itertools import product
import string
from colorama import Fore



now = datetime.now()
Day = now.today()
# print(Day)

print("\n\n")

print(f'\n{Fore.CYAN}[*] Code By HorridHanu(^_~).')
print(f'{Fore.CYAN}[*] Create All Possible Password.')
print(f"{Fore.RED}\n[+]Info\nThe speed of process depend upon on your particular device!")



print(f'\r\n{Fore.CYAN}[*] If you want to add following just hit Y/[y]! ')




name = input(f"{Fore.WHITE}[*] Enter the file name for creating list: ").lower()
while len(name) == 0 or name == " " or name == "  " or name == "   ":
    print("\r\n[-] You must enter a file name at least!")
    name = input("> Name: ").lower()

Tcharacter = ""
Lowercase = input(f'{Fore.WHITE}* Add Lowercase Characters(Y/[N]): ')
while len(Lowercase) == 0 or Lowercase == " " or Lowercase == "  " or Lowercase == "   ":
    print("\r\n[-] You must enter a command at least!")
    Lowercase = input("[+] Lowercase (Y/[N])")

if Lowercase == "n" or Lowercase == "N":
    print(f'{Fore.RED}[-] Lowercase Not Added!\n')
    Lcharacter = ''
elif Lowercase == "y" or Lowercase == "Y":
    Lcharacter = string.ascii_lowercase
    Tcharacter = Lcharacter
else:
    print(f"{Fore.RED}[-] Not command! Tool Can't Add Lowercase\n")
    Lcharacter = ''


Uppercase = input(f'{Fore.WHITE}* Add Uppercase Characters(Y/[N]): ')
while len(Uppercase) == 0 or Uppercase == " " or Uppercase == "  " or Uppercase == "   ":
    print("\r\n[-] You must enter a command at least!")
    Uppercase = input("[+] Uppercase (Y/[N])")
if Uppercase == "n" or Uppercase == "N":
    print(f'{Fore.RED}[-] Uppercase Not Added!\n')
    Ucharacter = ''
elif Uppercase == "y" or Uppercase == "Y":
    Ucharacter = string.ascii_uppercase
    Tcharacter = Ucharacter + Lcharacter
else:
    print(f"{Fore.RED}[-] Not command! Tool Can't Add Uppercase\n")
    Ucharacter = ''



Digitcase = input(f'{Fore.WHITE}* Add Digit(Y/[N]): ')
while len(Digitcase) == 0 or Digitcase == " " or Digitcase == "  " or Digitcase == "   ":
    print("\r\n[-] You must enter a command at least!")
    Digitcase = input("[+] Digitcase (Y/[N])")
if Digitcase == "n" or Digitcase == "N":
    print(f'{Fore.RED}[-] Digit Not Added!\n')
    Digit = ''
elif Digitcase == "y" or Digitcase == "Y":
    Digit = string.digits
    Tcharacter = Ucharacter + Lcharacter + Digit
else:
    print(f"{Fore.RED}[-] Not command! Tool Can't Add Digit\n")
    Digit = ''



Punctuationcase = input(f'{Fore.WHITE}* Add Punctuation(Y/[N]): ')
while len(Punctuationcase) == 0 or Punctuationcase == " " or Punctuationcase == "  " or Punctuationcase == "   ":
    print("\r\n[-] You must enter a command at least!")
    Punctuationcase = input("[+] Punctuationcase (Y/[N])")
if Punctuationcase == "n" or Punctuationcase == "N":
    print(f"{Fore.RED}[-] Punctuation Not Added!\n")
    Punctuation = ''
elif Punctuationcase == "y" or Punctuationcase == "Y":
    Punctuation = string.punctuation
    Tcharacter = Ucharacter + Lcharacter + Digit + Punctuation
else:
    print(f"{Fore.RED}[-] Not command! Tool Can't Add Punctuation\n")
    Punctuation = ''


Whitespace = input(f'{Fore.WHITE}* Add Whitespace(Y/[N]): ')
while len(Whitespace) == 0 or Whitespace == " " or Whitespace == "  " or Whitespace == "   ":
    print("\r\n[-] You must enter a command at least!")
    Whitespace = input("[+] Whitespace (Y/[N])")
if Whitespace == "n" or Whitespace == "N":
    print(f"{Fore.RED}[-] Whitespace Not Added!\n")
    Whitespace_ = ''
elif Whitespace == "y" or Whitespace == "Y":
    Whitespace_ = string.whitespace
    Tcharacter = Ucharacter + Lcharacter + Digit + Punctuation + Whitespace_
else:
    print(f"{Fore.RED}[-] Not command! Tool Can't Add Whitespace\n")
    Whitespace_ = ''



Hexadecimal = input(f'{Fore.WHITE}* Add Hexdigit(Y/[N]): ')
while len(Hexadecimal) == 0 or Hexadecimal == " " or Hexadecimal == "  " or Hexadecimal == "   ":
    print("\r\n[-] You must enter a command at least!")
    Hexadecimal = input("[+] Hexadecimal (Y/[N])")
if Hexadecimal == "n" or Hexadecimal == "N":
    print(f"{Fore.RED}[-] Hexadecimal Not Added!\n")
    Hexadecimal_ = ''
elif Hexadecimal == "y" or Hexadecimal == "Y":
    Hexadecimal_ = string.hexdigits
    Tcharacter = Ucharacter + Lcharacter + Digit + Punctuation + Whitespace_ + Hexadecimal_
else:
    print(f"{Fore.RED}[-] Not command! Tool Can't Add Hexdigit\n")
    Hexadecimal_ = ''





Octadecimal = input(f'{Fore.WHITE}* Add Octadigit(Y/[N]): ')
while len(Octadecimal) == 0 or Octadecimal == " " or Octadecimal == "  " or Octadecimal == "   ":
    print("\r\n[-] You must enter a command at least!")
    Octadecimal = input("[+] Octadecimal (Y/[N])")
if Octadecimal == "n" or Octadecimal == "N":
    print(f"{Fore.RED}[-] Octadecimal Not Added!\n")
    Octadecimal_ = ''
elif Octadecimal == "y" or Octadecimal == "Y":
    Octadecimal_ = string.octdigits
    Tcharacter = Ucharacter + Lcharacter + Digit + Punctuation + Whitespace_ + Hexadecimal_ +Octadecimal_
else:
    print(f"{Fore.RED}[-] Not command! Tool Can't Add Octadigit\n")
    Octadecimal_ = ''
    # Tcharacter = Ucharacter + Lcharacter + Digit + Punctuation + Whitespace_ + Hexadecimal_ +Octadecimal_

Tcharacter = Ucharacter + Lcharacter + Digit + Punctuation + Whitespace_ + Hexadecimal_ +Octadecimal_



min_lenght = int(input(f'{Fore.CYAN}[+] Enter The Minimum Length: '))
max_lenght = int(input(f'{Fore.CYAN}[+] Enter The Maximum Length: '))

counter = 0


print(f"{Fore.LIGHTMAGENTA_EX}[-] Please Wait While Tool is creating Password List.....")
print(f"{Fore.RED}\n[+]Info\nThe speed of process depend upon on your particular device!")
# print(file)
file_open = open(name + ".txt", 'w')
file_open.write(f"Process executed at:- {Day}")

# globals(Filename)
for i in range(min_lenght, max_lenght):
    for j in product(Tcharacter, repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter += 1




print(f"\n{Fore.RED}[+] Password list is created...".format(counter))
print(f"{Fore.RED}[+] Password list of name " + name + " is saved in current directory..")
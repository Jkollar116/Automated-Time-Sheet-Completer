Author: Jack Kollar
This is my first python project!
# Automated-Time-Sheet-Completer
This code is designed to automate the process of filling out time slots for a particular week in a time attendance system.

It starts by importing the necessary libraries for Selenium web automation and setting up the Chrome driver with specified options. 
It then prompts the user to input their email and password in a secure manner using msvcrt.

Afterwards, it navigates to a login page for a time attendance system and inputs the user's credentials using the send_keys() method from the ActionChains class.
It also selects the user's school from a dropdown menu and submits it.

Once logged in, it navigates to the page where the user can input their time slots. It selects the first week from a dropdown menu and then uses a for loop to input the time slots for each day of that week.

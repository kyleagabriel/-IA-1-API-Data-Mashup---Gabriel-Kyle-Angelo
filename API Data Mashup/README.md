PROJECT DESCRIPTION

This project deals with displaying a product list from a American fake store API, and calculating it's price to local currency (PHP). This scenario is inspired by Filipinos wanting to see international product prices directly in Peso rather than manually having to calculate it.

API USED

Fake Store API: https://fakestoreapi.com/ 
Live Exchange Rate: https://exchangerate.host/

HOW TO SET UP AND RUN LOCALLY

The first step after creating the project folder is to create a virtual environment and activating it. Once this is done, I am now able to download the web framework, Flask, that I used for this product as to not bloat my system.
In Flask, you can run locally by typing python app_name.py in the terminal. Once you run it in the terminal, a local host link will appear which allows you to view and use your website.

HOW THE DATA JOIN WORKS

In order to join the data from the two APIs, I created a function that calls both APIs. I stored this data in an empty list using a for loop wherein the attributes are chosen based on the dictionary I manually created. I connected them by passing the USD price of the item and the exchange rate of USD to PHP in a single variable in which it computes for the exchange rate dynamically based on the passed value from the original USD price of the product.
For example, if I had two different APIs, I would first create a function for the two APIs individually to see their attributes. Once I see their attributes, I can now join them through calling both APIs in one function. As I map the dictionary to fill up the empty list, I connect at least one attribute from each API in one variable so that they work hand in hand with one another rather than just working independent of each other.

KNOWN LIMITATIONS

When listing the products, it only follows the sequence of how its originally listed on the API. You cannot choose a specific product that you want to display, you can only set how much products you want to be displayed.

AI usage note

I used AI to learn the syntax of Flask as this is my first time using this for web development.
I used AI to improve the design of my template and add emojis.
I used AI to work on the JS and error handling as I have never worked with JS ever. This is also the first time I've done error handling in web development, so AI was a big aid for me to be able to do the assignment and learn throughout doing the assignment.
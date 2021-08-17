# Humanitary - A gift shop

Humanitary is a fictional gift shop. It is loosely based on [UNCHR'S webpage](https://sverigeforunhcr.se/stod-oss/gavoshop).
This is an ecommerce website that is based on the ***business-to-customer-model***.

![Responsive](https://i.ibb.co/6J1xTpj/responsive.jpg)

## Purpose of this project
Id Like to start by saying that this has been a challenge for me. My work and school life have been in a constant battle, and I've given it all the time I've had, considering the cirtumstances.

 - To provide an affordable way of giving gifts to those who are in need in other parts of the world.

## Sources of information for this project

 - [Dennis Ivy's videos on django](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg)
 - [Django documentation](https://docs.djangoproject.com/en/3.2/)
 - [Stripe Documentaion](https://stripe.com/docs/payments?payments=popular)
 - [Members of StackOverflow](https://stackoverflow.com/)
 This project wouldn't be possible without them passing on their knowledge, so credit is due where it's due.

## User stories

 - As a **user**, I can  buy gifts.
 - As a **user**, I can add, delete and update items in the shopping cart.
 - As a **user**, I register for an account.
 - As a **user**, I can go through the payment checkout process.
 - As a **logged in user**, I can see my previously ordered items.
 - As a **user**, I can go through the checkout process even I'm **not** logged in.
 - As a **user**, I can subscribe to a newsletter.

## Languages and frameworks used
 - HTML
 - CSS
 - Javascript
 - Django


## Design

The design is made to be easy on the eyes. There for I went with a white, blue and yellow colored theme, as per the image below. The design is, again, loosely based on [UNCHR'S webpage](https://sverigeforunhcr.se/stod-oss/gavoshop).

![enter image description here](https://i.ibb.co/vmXrPsn/screencapture-humanitary-herokuapp-2021-08-17-16-16-01.png)


## Features
**The main features of the site are:**

 - A login and user system
 ![Login page](https://i.ibb.co/MMzwpWF/screencapture-humanitary-herokuapp-accounts-login-2021-08-17-16-41-16.png)
 - A shop where the user can buy gifts
 ![Shop](https://i.ibb.co/2jh1QnD/screencapture-humanitary-herokuapp-shop-2021-08-17-16-42-31.png)
 - A shopping cart that any guest user or logged in user can add or remove items from
 ![Shopping cart](https://i.ibb.co/ZB7ZdM0/screencapture-humanitary-herokuapp-cart-2021-08-17-16-44-22.png)
 - A profile page to display the user's past ordered items.
 ![Profile page](https://i.ibb.co/hdBvFV1/screencapture-humanitary-herokuapp-my-profile-2021-08-17-16-45-01.png)


**Features yet to be implemented, but could be added in the future:**

 - A product description page, where the user could add or remove quantity based on text input.
 - A dashboard page where the user could see all orders, categories (if present) and the ability to update their information.

***-** Features that have not yet been implemented are based on my short timeframe. I work and study fulltime, so some sacrifices had to be made in order to get the site up and running.* 


 ***(I plan to add more features in the future).***


## Testing
Testing was made by me and some of my friends. All features have been tested manually to save me development time.
Features tested were:

 - Login
 - Logout
 - Add, delete and update items in the cart
 - Payment Checkout through ***Stripe***
 - Newsletter subscription form
***(Thus far, everything works as intended)***

## Deployment
The deployment was made to heroku, using ***PostegreSQL*** for database. ***SQLITE3*** was used in development.
It features ***Gunicorn web server*** as that is what heroku uses.

For static and media files, I use the ***AWS3 services***.

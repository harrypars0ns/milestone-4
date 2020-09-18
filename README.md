# Whole Apparel

## Table Of Contents

- General Information
- Demo
- UX and Wireframes
- Features
- Features Left to Implement
- Technologies Used
- Testing and Validation
- Deployment
- Credits
- Acknowledgements

## Demo

A live demo of the website can be found [here](https://a-recipe-book.herokuapp.com/).


## General Information

Full Stack Development Milestone Project.

In 2020 fashion makes up 10% of all carbon emissions in the world.  That is more than the entire airline industry. "Fast Fashion” as  it is now called, is a blight on the environment. Whether that is  in landfills, from carbon emissions or straight up chemical  pollution in our rivers, lakes, seas and air.

Our mission is to  show that there is a way of making and selling clothes where  exploitation doesn't happen anywhere on the supply chain, whether  that is environmental or worker exploitation.

Whole Apparel is a company that sells sustainable, handmade, chemical free and fair trade clothing through our ecommerce website. We buy from local clothes makers all around the world using locally sourced materials and made in traditional ways. The clothes we sell tell a story about the nations and localities that they originate from and we want to emphasise that.

For customers the app allows you to create a profile, browse our items, add them to a cart and checkout. For store owners and superusers there is more functionality. 

This website is the best place to find unique clothes that are 100% sustainable, 100% chemical free and 100% Fair Trade.



## UX

### Strategy

I want to let people realise that they can find clothes that are made ethically, and that they think are beautiful, and want to buy. I want to entice them visually and then let them make a purchase in as few clicks as possible. To entice I will Use nice visually appealing cards that display the clothes with an image and some key information like price and nation of origin. The site should be aesthetically pleasing, simple, professional and minimalist.

### Scope

The function of the site will be to give users an easy way to find beautiful clothes that they know are not damaging to the planet or its inhabitants. The will be able to create a profile, choose clothes, add them to a cart and then make a purchase using a debit or credit card.

For store owners and superusers you will be able to create, read, update and delete clothing with all the necessary fields such as image upload and price changing.

### Structure

The site was designed to be as user friendly as possible. I wanted to make sure that the UX was viable for people with bad eye-sight, people with dyslexia,
those who aren't comfortable using complex websites and the elderly.

The form inputs are clearly labeled and the text on the cards easily readable.

The validation lets you know if you are not inserting a complete item of clothing, correct user information or if your card details are not valid. 

The site is very intuitive so nobody will have trouble accessing all the features. Whether you are web-savvy or a rookie you will have no problems using Whole Apparel’s website. 

### Skeleton

NEEDS CHANGING WITH CORRECT WIREFRAMES
[Wireframe plan 1 - Add/Edit Recipe Form]  (https://github.com/harrypars0ns/a-recipe-book/blob/master/Wireframes/addeditrecipe.jpg)
NEEDS CHANGING WITH CORRECT WIREFRAMES

[Wireframe plan 2 - Read Recipe Page]  (https://github.com/harrypars0ns/a-recipe-book/blob/master/Wireframes/readrecipe.jpg)
NEEDS CHANGING WITH CORRECT WIREFRAMES><><><><><><><><><
<<>.>><_%£$625628y3498y459857y9825y9827y59
[Wireframe plan 2 - Main Recipes Page]  (https://github.com/harrypars0ns/a-recipe-book/blob/master/Wireframes/recipes.jpg)

### Surface

I want my users to be able to look at the clothes displayed in front of them and have absolutely no trouble reading all the information. I don’t want anything to look overloaded with too many items, so plenty of space between items. I chose a plain white background on the site to emphasise a minimalist feel that plays into the “low-impact” branding of Whole Apparel. The simple black text is simple but still looks striking and professional. The most important thing is that the website is nice to look at for everyone including people with bad eye-sight, people with dyslexia and the elderly.

I chose to display the recipes on Bootstrap cards as the high quality image really elicits a positive emotional reaction.
The font sizes have been set to the biggest and most legible they can without sacrificing the usability and aesthetic of the website.

The forms use Crispy Forms which are a nice way of getting quick aesthetically pleasing forms used throughout the site.

## Features

The cards are generated on beautiful Bootstrap cards which is a simple but visually effective way of displaying my products.

The app has a few basic functions, to allow you to: display, create, view, update and delete individual products. You are able to add a chosen quantity products to your cart, edit that within the cart view and then checkout using Stripe.  You are able to create a profile using your own info and edit that information whenever you may need to. This info is saved and inserted automatically in the checkout form. 

When adding new products the form fields contain: the item name, description, type of clothing, cost, nation of origin, the key sustainable trait that it might have (vegan, low-impact, chemical free, naturally dyed etc.) and an image field for uploading and displaying the product.

There is a button in the cart that lets you remove the item without having to use the quantity input box. Using javascript I set this button to set the quantity to 0 and save the form therefore deleting the product from the cart.

For superusers and storeowners there is a button that allows you to completely remove a product from the store and a button that allows you to edit the products information in the database. The current information is already shown in the form fields so you are able to only edit one field if you want.

The forms do have validation, the front end uses html attributes on the inputs such as 'maxlength' and required attributes. The backend validation was done by writing into the views.py that the forms can only be saved once they have been asked IF the form “is_valid” ELSE the form would reset and not submit anything.

The product’s individual pages are laid out simply to make them very easily printable. 

### Features Left to Implement

When I have time, I would like to make: A filtering system on the page that displays all the products so that you can choose to only view certain types of clothes, whether that be a certain category, nation of origin or sustainable trait that you only want to see clothes from. We only have a few products so far so this isn’t necessary right now.

Another great feature to let users set the price range so that  they can view clothes that they can definitely afford.

Scrolling rows where each row is a different category of clothes 	  eg. Hats, Asian, naturally dyed clothes. Similar to a Netflix interface

- Super users would be able to upload their any aspect ratio of their images and it would automatically crop them to a square. Right now you can only upload a square picture while maintaining the organised style of the site. 

A way for customers to tip the makers of the clothes

## Technologies Used

- HTML
- CSS
- Javascript
Python3
Django
Crispy Forms
Stripe
- Git
- Github
- Heroku deployment

- [Bootstrap](https://getbootstrap.com)
    - The project uses **Bootstrap** for aiding placement and responsive design plus components such as cards and some buttons.
- [Google Fonts](https://fonts.google.com/)
    - The project uses the **Google Fonts** typeface 'Exo' in varying weights and sizes.
- [jQuery](https://jquery.com/)
    - The project uses the **jQuery** working with the Javascript.
- [Django](https://www.djangoproject.com/)
    - The project uses the **Django** a framework for building the app.
- [Stripe](https://stripe.com/)
    - The project uses the **Stripe** process the payments using a debit or credit card as well as capturing web hooks.
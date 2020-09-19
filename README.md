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
- Version Control
- User Stories
- Credits
- Acknowledgements

## Demo

A live demo of the website can be found [here](https://whole-apparel.herokuapp.com/).


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

[Wireframe plan 1 - All Products]  (https://github.com/harrypars0ns/milestone-4/blob/master/wireframes/all-products-wireframe.jpg)

[Wireframe plan 2 - Get Product]  (https://github.com/harrypars0ns/milestone-4/blob/master/wireframes/get-product-wireframe.jpg)

[Wireframe plan 3 - Cart Page]  (https://github.com/harrypars0ns/milestone-4/blob/master/wireframes/cart-wireframe.jpg)

[Wireframe plan 4 - Checkout Page]  (https://github.com/harrypars0ns/milestone-4/blob/master/wireframes/checkout-wireframe.jpg)

[Wireframe plan 5 - Add/Edit Product Page]  (https://github.com/harrypars0ns/milestone-4/blob/master/wireframes/add-edit-product-wireframe.jpg)

[Wireframe plan 3 - About Page]  (https://github.com/harrypars0ns/milestone-4/blob/master/wireframes/about-us-wireframe.jpg)


### Surface

I want my users to be able to look at the clothes displayed in front of them and have absolutely no trouble reading all the information. I don’t want anything to look overloaded with too many items, so plenty of space between items. I chose a plain white background on the site to emphasise a minimalist feel that plays into the “low-impact” branding of Whole Apparel. The simple black text is simple but still looks striking and professional. The most important thing is that the website is nice to look at for everyone including people with bad eye-sight, people with dyslexia and the elderly.

I chose to display the clothes on Bootstrap cards as the high quality image really elicits a positive emotional reaction.
The font sizes have been set to the biggest and most legible they can without sacrificing the usability and aesthetic of the website.

The forms use Crispy Forms which are a nice way of getting quick aesthetically pleasing forms used throughout the site.

## Features

The cards are generated on beautiful Bootstrap cards which is a simple but visually effective way of displaying my products.

The app has a few basic functions, to allow you to: display, create, view, update and delete individual products. You are able to add a chosen quantity products to your cart, edit that within the cart view and then checkout using Stripe. You are able to create a profile using your own info and edit that information whenever you may need to. This info is saved and inserted automatically in the checkout form. 

When adding new products the form fields contain: the item name, description, type of clothing, cost, nation of origin, the key sustainable trait that it might have (vegan, low-impact, chemical free, naturally dyed etc.) and an image field for uploading and displaying the product.

There is a button in the cart that lets you remove the item without having to use the quantity input box. Using javascript I set this button to set the quantity to 0 and save the form therefore deleting the product from the cart.

For superusers and storeowners there is a button that allows you to completely remove a product from the store and a button that allows you to edit the products information in the database. The current information is already shown in the form fields so you are able to only edit one field if you want.

The forms do have validation, the front end uses html attributes on the inputs such as 'maxlength' and required attributes. The backend validation was done by writing into the views.py that the forms can only be saved once they have been asked IF the form “is_valid” ELSE the form would reset and not submit anything.

The product’s individual pages are laid out simply to make them very easily printable. 

### Features Left to Implement

Heroku will not send the image files you choose on a new product to the AWS S3 media and static hosting platform. When run locally this feature works fine but when using the deployed site through Heroku your images will not load. This is a MUST if this project is to go live

When I have time, I would like to make: A filtering system on the page that displays all the products so that you can choose to only view certain types of clothes, whether that be a certain category, nation of origin or sustainable trait that you only want to see clothes from. We only have a few products so far so this isn’t necessary right now.

Another great feature to let users set the price range so that  they can view clothes that they can definitely afford.

Using the Google maps API it would be great to have an interactive map that you can view the origins of all of the different clothes.

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

## Testing
 
My first thought when choosing how the user chooses the image for each item was to have a text input that they would paste an image URL into. The app would check if it was a .jpg, .jpeg or .png file format and then put it on the card.
There was a couple issues with this including: some image formats are not jpg, jpeg or png so the app was rejecting perfectly good images, very annoying for the user.
Another issue was that some image links are 1000 characters long. I decided to go for a super secure system of only allowing an image upload and no way of using a url.

You can NOT upload a new image through the deployed site on Heroku, AWS hosts the images that are on the site already so you must upload imgages there if you want them to display properly. If using the local version there is no problem uploading new images.

The Stripe payment system initially gave me some problems. The payment intent was being created but the charge wasn’t going through as I could see in my webhooks on the Stripe dashboard. I also got an error from the model. I fixed this by deleting all migrations eg. users, products, categories and orders etc. I removed all migration files within your project. I went through all of my project app’s migration folders and removed everything inside, except the __init__.py file. After making migrations this fixed my problems and the payments were going through.

The forms do have validation, the front end uses html attributes on the inputs such as 'maxlength' and required attributes. The backend validation was done by writing into the views.py that the forms can only be saved once they have been asked IF the form “is_valid” ELSE the form would reset and not submit anything. I tested this by not filling in certain fields and making sure it didn’t submit. They passed all tests.

The nav-bar and brand logo at the top of all pages created some issues on mobile. The nav would only be all in a row on certain screens, and jumbled up on others. This was fixed by a few media queries and changing the html bootstrap classes to remove some padding from one of the nav links. The brand logo also looked bad on some screens and so had to be fixed with some media queries. They both now look good on all screen sizes and so pass my test.

When creating the price input, it started off as a slider that you would select the number of pounds on the cost slider. This turned out to be terrible UX and would be much improved by making the pricing a straight text-box that only allows a number with a maximum of 2 decimal places. This is a much more precise, quicker and user friendly way of setting the price of a product.
When you add an item, the page used to redirect to the all products page but now goes to the product you have just created or edited. Once saved the pages redirect to where they are meant to and so pass my tests.

Only superusers are allowed to use the remove, edit and create product features I did this my making sure that the user “is_superuser” and displaying the links to those pages if that is TRUE. If they are not a superuser they do not see these links and so would have no way to create, edit or remove a product from the store. I tested this by logging out and trying as an anonymous user, a non ‘super’ user and as a superuser. The links only showed for the super user and so it passes my tests.

When deleting an order through the admin I was getting an error. It was a simple fix by adding an “or 0” to the end of a line of code that would update the total of all line items. This now works fine and so passed my test. 

Images on the cards were all different sizes and so messed up the organisation on the all products page. All images are cropped to the same aspect ratio (a square) so the cards are all the same size and look the same on all screens.

I had a problem where I would have to set the environment variables every time that I opened the workspace in GitPod. I fixed this by creating a gitignore file with a file (env.py) that contained my environment variables and then I set them in the project level settings.py file. I no longer need to export environment variables manually and so it passed my test.
  
I ran the CSS and HTML through the W3C Jigsaw validator with no errors found. The Javascript was run through the JSHint validator with no major issues. The Python was ran through a validator and all issues that could be fixed and didn't break the code were fixed. Checked to be styled like pep8online.com.

The site works across many browsers including: Chrome, Firefox, Safari and Edge.

## Deployment

- My site can be found [here](https://whole-apparel.herokuapp.com/).

I am hosting the site on Heroku on the master branch. I had a already been committing to GitHub before.

I have had huge issues when deploying this project. **Heroku will not send the image files you choose on a new product to the AWS S3 media and static hosting platform**. When run locally this feature works fine but when using the deployed site through Heroku your images **will not load**.

I used the AWS S3 service to host my static and media files as Heroku does not support these. This was done by creating a bucket in AWS and linking it with a policy and creating static user to . 

I have my git repository hosted on Github and the website is hosted on Heroku. I have commits after I've finished a feature or fixed a bug. When I use git push the Github repository is updated and I use git push heroku master to push the updates to Heroku.

The best way to deploy is to link it to your GitHub repo. In the deploy tab in Heroku, under 'Deployment' select github and choose your repo. Then you can set it to automatically depoly every time you use git push.

To deploy on Heroku you have to:
Create an app on the main page of your Heroku dash.
Go to settings, press 'reveal config vars' I used IP (0.0.0.0), PORT (5000), Secret Key
Gitpod has Heroku already installed so just use 'heroku login' in your terminal.
Add a requirements.txt with 'pip3 freeze > requirements.txt'.
Add a Procfile with 'echo web: python app.py > Procfile'.

You must have these environment vars set:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<secret key>`
AWS_SECRET_ACCESS_KEY | `<secret key>`
DATABASE_URL | `<postgres database url>`
EMAIL_HOST_PASS | `<secret key>`
EMAIL_HOST_USER | `<Email address that customers recieve from>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLIC_KEY | `<public key>`
STRIPE_SECRET_KEY | `<secret key>`
STRIPE_WH_SECRET | `<secret key>`
USE_AWS | `<True>`

If you want to run the code locally you can use 'git clone'. Alternatively you 
can download all the files in a .zip file and open 'index.html' in your browser of choice.

## Version Control

I managed version control with GitHub. I mainly used the master branch but I did make a seperate branch at one point to do some testing without editing the master code.

## User Stories

1. As someone who knows nothing about low-impact clothing I want to know why I should buy a piece of low impact clothing make my decision and buy it.

2. As somebody who did’t know fast fashion was a problem I want to use the website to learn about why I should be buying sustainable clothes so that I am a smaller cost on the planet.

3. As a regular customer of Whole Apparel I want my details to be saved when I checkout so that I don’t have to enter them every time.

4. As somebody with a mobile phone I want this to be intuitive on small screens so that I can easily use the website.

5. As a store owner who is not tech savvy I want to be able to add a new product to the database without having to change the code or use the Django admin. So that I can easily add products to my site.

6. As a store owner who is not tech savvy I want to be able to edit a product’s information in the database without having to change the code or use the Django admin. So that I can easily edit product’s info on my site.

7. As somebody with bad eyesight I want to be able to read all text on the screen easily so that I know whether I should buy something.

8. As a superuser I expect that when I edit an item info, I only have to edit the one field that needs updating so I don't have to fill out the whole form.

9. As a superuser entering a new product I expect the form to remind me to fill in all fields before submitting, so that I dont insert an incomplete item into the database.

10. As someone with dyslexia I expect I will be able to read everything on screen.

Full list of user stories in userstories.txt.


## Credits

### Content

I made the layout, buttons and cards using Bootstrap. The forms used crispy forms.
Authorisation was made with Django AllAuth.
The checkout and stripe payment were made using the same system from the Boutique Ado mini project. 

### Media
I used Pexels (stock images) for my images, and font awesome for my icons.

### Acknowledgements

- Thanks to Brian Macharia for all the help he's given me making this. Couldn't have done it without you.
- Thanks to the whole tutor team from CodeInstitute for help with my project.

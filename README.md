# CADWork - Full Stack Django Milestone Project

[![Build Status](https://travis-ci.org/JShad30/CADWork_full_stack.svg?branch=master)](https://travis-ci.org/JShad30/CADWork_full_stack)

## Project Overview

CADWork is a fictional website that allows individuals or businesses looking to have professional CAD designs, measured surveys, or creative designs for their project, pair up with CAD professionals who are willing to carry out their project on a freelance basis.

Users of the site can look through the blog to find out more about the industry, or if you're looking to make a start in CAD design, buy items in the shop!

![CADWork Layout Large](https://user-images.githubusercontent.com/23212520/64134770-86857000-cdd9-11e9-8e7a-dc26d98bafc5.png)

## User Experience/ User Stories

The site has been given a consistent look and feel throughout to give the best user experience possible. Professional fonts and colours have been used in keeping with the professional nature of the site.

### Example uses of site

The basic user stories were drawn up prior to development of this site and can be viewed in the wireframes folder.

#### Creating an account

On the home and about page there are reasons given as to why a user would want to become a member of the site and are sold the benefits of doing so. To register a user would click the 'register' button in the navigation bar, or selected other places around the site. Once signed up they are able to log in, and have access to their personal profile page. From here a user can upload a job, find jobs and upload blogs. The user is advised to set up their personal profile and fill in details to enable them to introduce themselves to other members through the public profile pages. The user is able to update this at any time through by clicking the 'edit profile' button.

Although all users are able to view the jobs and blogs, only by registering can you upload, or be able to comment on them, and then upload files to a job. A user will also need to have an account to be able to purchase items from the shop.

#### Uploading a job

A user wants to upload a job and find a CAD professional to undertake their work for a new house extension. The user would need to register and sign in as described above. From here they would select the 'create a job' button. This takes them to the 'create a job' form from where they can upload details and images. When a job is created it is placed on the job board from where CAD professionals are able to view it, ask questions and once the work is completed, submit files. The job creator will be able to pay for the file.

#### Uploading files to a job

Users are able to upload files to a user

#### User want to read or upload blogs

The blog section is created to allow users to understand more about the industry or to share their insights with others. To view blogs, you do not need to be logged in. On the home page you can directly and read the three most recently uploaded blogs, or click the 'view more' button, which redirects the user to the 'blogs page'. Once here they are able to select any of them and read the whole article. If a user would like to upload a blog they would either need to log in, and navigate to the create a blog section from their personal page. If the user who created the blog is logged in and select a blog they have uploaded they would get to either update/edit or delete the post.

#### Shop/Products

A user can go to the shop/products page of the website if they are starting out in the industry and find a selection of related products. If a user wishes to buy a product they can click on the 'add to basket button'. This adds the products to the cart. The user does not need to be logged in or have an account to be able to purchase the products. 

The items in the shop can only be added by superusers of the site through the admin panel, as CADWork is not a site for users to seel their own products.

## Features

Features are functionality that has been added to different areas of the site.

### Jobs

The jobs section contains functionality that enables users to be able to upload files, and ask questions of the user who uploaded the project. Only the user who created the job or the superuser is able to view the files that have been uploaded. Using 'is_authenticated, the aside view of the page changes depending on who is viewing the job. If it is the creator, then they are able to see the files that have been uploaded. If it's being viewed by the 

### Blog

The blog contains the functionality to be able to upload, update and delete the post. This, as previously mentioned is only available to those users who are logged in. As with the jobs section, the users are able to comment on blogs.

### Shop/Products

As with most products/shops online, the products section gives the users the ability to view products, add to their shopping cart and pay for products.

### Payment systems

There are payment features on the site for the shop, and the ability for two users to be able to pay each other.

## Technology Used

This project was built using different languages, libraries and frameworks. 

### Frontend

The template pages have been written with HTML5 (http://www.html5.com/) and styled with CSS3 (www.css3.com).

The Bootstrap library has been used to style portions of the site, such as the buttons and navigation bar.

The forms have been styled with Crispy forms.

Javascrpt has been used on the home page for the scrolling image at the top of the page (https://www.javascript.com/), as well as the Stripe payment functionality.

### Python

The site has been built using the Python based Django framework (https://www.djangoproject.com/) and is run from the 'manage.py' file which is stored in the outer folder. Within the main folder you can see the list of apps that have been created to deal with the different functionality of the site. These are:

* Home App - This deals with the home page, about page and the contact form.
* Jobs App - Deals with the uploading of a job for a job owner, and the uploading of files and comments for all users.
* Users App - This deals with the sign up, login and reset password functionality.
* Blog App - This deals with the create, edit, delete and the viewing of the blogs
* Shop App - This deals with the viewing of the products/ shop.
* cadwork is the main app file which contains the settings for the site. 

The 'jinja template engine' (http://jinja.pocoo.org/) has been used within the html template pages already described.

### Payment Methods

The products from the shop, if added to the users cart can be paid for through the 'Stripe API'. This is connected to the site with the 'stripe.js' file stored in the 'js' folder within 'static'.

### Data Storage

Database tables were created in the 'models.py' files of the apps.

### Version Control

Git was used throughout the project for version control.

## Testing

I have tested the site on different internet browsers (including Chrome, Firefox and Edge). Using the developer tools in Chrome I tested for different screen sizes, to ensure the site is fully responsive and responds to the different screen breakpoints I set in the CSS file.

The CSS was run through a CSS validator and showed no errors. The javascript/jquery code was validated using jshint and showed no errors.

The site has been tested manually by clicking all anchor links to the pages (both internal and external links) and checking all of the jQuery options, including the drop down item for the navbar, the scrolling images on the home page.

Prior to submitting the project but after it was live I created test users, each to create blogs, jobs, comment and upload comments to them etc.

Test payments were made using the default test credit card number with Stripe. There were issues with the order and payment forms 

## Further Considerations

### Blog

I would add a comments section to the blog allowing other members to add their thoughts. The logic would be handled in a similar manor to the The users would need to be logged in to access this functionality. Using the same methods as with the navbar and using is_authenticated. If the user is authenticated then a button would be placed at the bottom of the blog. To press this would bring up a textbox, which would be contained within a form. When this was submitted the message would appear at the bottom of the blog.

## Deployment

This project has been deployed to both Github and Heroku by using the push command in the terminal.

If you would like to contribute to the project can be cloned or downloaded from the Github link provided below. 

The individual files on Github can be found via https://github.com/JShad30/CADWork_full_stack, and the website can be viewed via ...............https://solar-system-quiz.herokuapp.com/...............

## Credits

### Media

The house extension picture was taken from https://www.bbc.co.uk/news/uk-england-48405569.

All other front page images, and those used as a default for the blogs and jobs were taken from Pixabay 

Images for the products in the shop have been taken from Amazon, Toolstation, Walmart, Athletics Direct, RS Components, dhgate.com and programsfull.org.

The default user face image has been taken from nepad.org.

### Acknowledgements

Throughout the project I received support from the mentor and the tutors. The site functionality, ideas and database structure were discussed with the mentor.

I used the following series to help with the registration and login functionality for the 'users' app, and creating the blog app: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1
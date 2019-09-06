# CADWork - Full Stack Django Milestone Project

[![Build Status](https://travis-ci.org/JShad30/CADWork_full_stack.svg?branch=master)](https://travis-ci.org/JShad30/CADWork_full_stack)

## Project Overview

CADWork is a fictional website that allows individuals or businesses looking to have professional CAD designs, measured surveys, or creative designs for their project, pair up with CAD professionals who are willing to carry out their project on a freelance basis.

Users of the site can look through the blog to find out more about the industry, or if you're looking to make a start in CAD design, buy items in the shop. The site can be viewd here at https://cadwork-full-stack-milestone.herokuapp.com/.

![CADWork Layout Large](https://user-images.githubusercontent.com/23212520/64134770-86857000-cdd9-11e9-8e7a-dc26d98bafc5.png)

## User Experience/ User Stories

The site has been given a consistent look and feel throughout to give the best user experience possible. Professional fonts and colours have been used in keeping with the professional nature of the site.

### Example uses of site

#### Creating an account

On the home and about page there are reasons given as to why a user would want to become a member of the site and are sold the benefits of doing so. To register a user would click the 'register' button in the navigation bar, or selected other places around the site. Once signed up they are able to log in, and have access to their personal profile page. From here a user can upload a job, find jobs and upload blogs. The user is advised to set up their personal profile and fill in details to enable them to introduce themselves to other members through the public profile pages. The user is able to update this at any time through by clicking the 'Update Profile' button in their profile page.

Although all users are able to view the jobs and blogs, only by registering can you upload, or be able to comment on them, and then upload files to a job. A user will also need to have an account to be able to purchase items from the shop.

#### User want to read or upload blogs

The blog section is created to allow users to understand more about the industry or to share their insights with others. To view blogs, you do not need to be logged in. On the home page you can directly and read the three most recently uploaded blogs, or click the 'view more' button, which redirects the user to the 'blogs page'. Once here they are able to select any of them and read the whole article. If a user would like to upload a blog they would either need to log in, and navigate to the create a blog section from their personal page. If the user who created the blog is logged in and select a blog they have uploaded they would get to either update/edit or delete the post. 

#### Uploading a job

A user wants to upload a job and find a CAD professional to undertake their work for a new house extension. The user would need to register and sign in as described above. From here they would select the 'Create New Job' button. This takes them to the 'create a new job' form from where they can upload details and images. When a job is created it is placed on the job board from where CAD professionals are able to view it, ask questions and once the work is completed, submit files.

#### Uploading files to a job

Users are able to upload files to a job by clicking the 'Upload a File' button. They are then redirected to the upload files form. The form requires the user to input a file name, and contains a button for them to be able to input a file. The user who uploads the file is flashed a message to tell them that the job creator is able to see their file.

#### Shop/Products

A user can go to the shop/products page of the website if they are starting out in the industry and find a selection of related products. If a user wishes to buy a product they can click on the 'Add'. This adds the products to the cart. The user does not need to be logged in or have an account to be able to purchase the products. 

The items in the shop can only be added by superusers of the site through the admin panel, as CADWork is not a site for users to sell their own products.

#### Note

I have created a basic terms and privacy page. These are for display only.

## Features

#### Blog

The blog contains the functionality to be able to upload, update and delete the post. This, as previously mentioned is only available to those users who are logged in. As with the jobs section, the users are able to comment on blogs. Users are not able to update or delete posts created by another user. This is handled by the UserPassesTestMixin within the class based views.

#### Jobs

The jobs section contains functionality that enables users to be able to upload files, and ask questions of the user who uploaded the project using either the 'Leave a comment' button or the 'Upload a file' button. Only the user who created the job or the superuser is able to view the files that have been uploaded. The aside view of the page changes depending on who is viewing the job. If it is the creator, then they are able to see the files that have been uploaded. Users are not able to update or delete jobs created by another user. This is handled by the UserPassesTestMixin within the class based views.

#### Shop/Products

As with most products/shops online, the products section gives the users the ability to view products, add to their shopping cart and pay for products.

#### Payment systems

There are payment features on the site for the shop payments.

## Further Considerations

#### Jobs Files

With further development I would stop the job creator being able to access the uploaded file before they had paid for it. For this payment system I would create the ability for two users being able to make payments to each other, or the payment being paid into an escrow account stored by CADWork. When the job owner informs CADWork that they have received the files, the money would then be released to the file creator.

## Technology Used

This project was built using different languages, and frameworks. 

#### Frontend

The template pages have been written with HTML5 (http://www.html5.com/) and styled with CSS3 (www.css3.com).

The Bootstrap framework (https://getbootstrap.com/) has been used to style portions of the site, such as the buttons and navigation bar.

The forms throughout the site have been styled with Crispy forms.

Javascrpt has been used on the home page for the scrolling image at the top of the page (https://www.javascript.com/), as well as the Stripe payment functionality.

#### Python

The site has been built using the Python based Django framework (https://www.djangoproject.com/) and is run from the 'manage.py' file which is stored in the outer folder. Within the main folder you can see the list of apps that have been created to deal with the different functionality of the site. These are:

* Home App - This deals with the home page, about page and the contact form.
* Blog App - This deals with the create, edit, delete and the viewing of the blogs.
* Jobs App - Deals with the uploading of a job for a job owner, and the uploading of files and comments for all users.
* Users App - This deals with the sign up, login and reset password functionality.
* Shop App - This deals with the viewing of the products/ shop.
* Cart App - Where the products that the user has added from the shop are stored.
* Checkout App - Where the shop products total price is stored and the user has the ability to pay.
* cadwork is the main app file which contains the settings for the site. 

The 'jinja template engine' (http://jinja.pocoo.org/) has been used within the html template pages.

#### Payment Methods

The products from the shop, if added to the users cart can be paid for through the 'Stripe API'. This is connected to the site with the 'stripe.js' file stored in the 'js' folder within 'static'.

#### Data Storage

Database tables were created in the 'models.py' files of the apps. During the development phase of the project a 'db.sqlite3' database was used. This contained the data while the project was used in my local environment. When the site was deployed a 'Postgres' database was attached to the project in Heroku, and this is what is being used on the live site currently.

The static files and media files are stored within an S3 bucket in AWS environment. 

#### Version Control

Git was used throughout the project for version control.

## Testing

#### Manual Testing

I have tested the site on different internet browsers (including Chrome, Firefox and Edge). Using the developer tools in Chrome I tested for different screen sizes, to ensure the site is fully responsive and responds to the different screen breakpoints I set in the CSS file.

The CSS was run through a CSS validator and showed no errors. The javascript/jquery code was validated using jshint and showed no errors.

The site has been tested manually by clicking all anchor links to the pages (both internal and external links) and checking all of the jQuery options, including the drop down item for the navbar, the scrolling images on the home page.

Prior to submitting the project but after it was live I created test users, each to create blogs, jobs, comment and upload comments to them. All features and functionality of the site were tested.

Test payments were made using the default test credit card number with Stripe. I was having issues with the order and payment forms, as they were not validating at first. It turned out that the files for Stripe were being loaded in the wrong place. There was also a small typing error in one of the pages which oce corrected work. Payments were made using Stripes test card. 

![payment](https://user-images.githubusercontent.com/23212520/64378624-018e9680-d025-11e9-94a6-f89de5c400b4.JPG)

The image above shows the errors I was getting before the issues were corrected. The files recently have resulted in successful payments as expected.

After the project was deployed I created three users. One of these users was a superuser, and the others were regular users who had just signed up for an account. Each of these have created blogs and jobs, commented on each others projects/blogs, and uploaded files. The superuser uploaded the products that are now in the shop.

#### Unit Testing

I have connected the project files in Github to Travis via the '.travis.yml' file in the main folder. At the top of this README file the current results of the tests can be seen. 19 tests have been created across the apps, testing a number of the different aspects, from creating a job or blog to testing the home views of each of the apps. The tests have been created in the tests.py file of each of the apps.

There were some tests that were failing when they were first written, which were updated until they passed. The result of this, as can be seen above, is that the build of this project is now passing.

## Deployment

This project has been deployed to Github in my local environment using the 'git push' command in the terminal.

To deploy this project into a live environment an AWS S3 bucket was created. This isused to store the media and static files that need to be served within the site. This allows for space, as considering users are uploading images, within the profiles, blogs, and jobs sections, there is the potential for there to be a very large number of files that need to be stored. The bucket has been linked to the project with AWS variables set in the 'settings.py' file.

The project has been created in Heroku, which is also where the Postgres database is stored, and within the settings in Heroku the configuration variables have been set. In the 'deploy tab' the deployment method has been set to link to Github, thus using the files pushed to Github to display the live site.

As the site was deployed I needed to make sure all the necessary requirements were placed in the requirements.txt file. 

When the project was deployed I had some issues from the development version which I needed to fix. I updated the way the images are saved within the models files in the users, jobs and blog app. Before the project was submitted, debug was changed from 'True' to 'False' in the settings file.

If you would like to contribute to the project it can be cloned or downloaded from the Github link provided below. 

The individual files on Github can be found via https://github.com/JShad30/CADWork_full_stack, and the website can be viewed via https://cadwork-full-stack-milestone.herokuapp.com/

## Credits

#### Media

The house extension picture was taken from https://www.bbc.co.uk/news/uk-england-48405569.

All other front page images, and those used as a default for the blogs and jobs were taken from Pixabay 

Images for the products in the shop have been taken from Amazon, Toolstation, Walmart, Athletics Direct, RS Components, dhgate.com and programsfull.org.

The default user face image has been taken from nepad.org.

#### Acknowledgements

Throughout the project I received support from the mentor and the tutors. The site functionality, ideas and database structure were discussed with the mentor.

The following project assisted me with the comments sections particularly: https://github.com/hschafer2017/PCSwimming

I used a Youtube series from Corey Schafer to help with the registration and login functionality for the 'users' app, and creating the blog app: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1

To help with the uploading files within the blog section I used the following videos from Vitor Freitas: https://www.youtube.com/watch?v=Zx09vcYq1oc

The following website helped with several areas of the site: https://simpleisbetterthancomplex.com/
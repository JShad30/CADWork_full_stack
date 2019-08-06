# CADWork - Full Stack Django Milestone Project

This project has been created for a start up that allows people to advertise jobs and bid on jobs for CAD work on small scale construction projects, whether new build extensions or interior design projects. You are able to create an account and create your job, allowing people to bid on the project. The job owner is then able to select the winning bidder and the work can begin.

The site is also useful for people who want to begin in this field, with blogs available for view. Blogs are uploaded to the site by users who have an account so there are advantages to becoming a site member. The products/shop page is also for people looking to start in the industry and there are products available for them to buy, and they would be able to buy direct from the site.

The site has been given a consistent look and feel throughout to make the user experience as good as possible. Professional fonts and colours have been used in keeping with the professional nature of the site.

## User Experience/ User Stories

### Example uses of site

The basic user stories were drawn up prior to development of this site and can be viewed in the wireframes folder.

#### User wants to create an account

On the home and about page there is reasons given as to why a user would want to become a member of the site and sold the benefits of doing so. Should they decide they would want to do so they would click the 'sign up' button from the home page. Once signed up they are able to log in. This takes them to their personal page. This is where jobs are managed from including the uploading, bidding on, upload blogs or be able to purchase products from the shop. The user is advised to set up their personal account and fill in some details. These are displayed in a column on the profile page. The useris able to update this at any time through by clicking the 'edit profile' button.

#### Uploading a job

A user wants to upload a job and find a CAD professional to undertake their work for a new house extension. This user would need to sign up for an account on the 'sign up' page. Once they have done this, or they already have an account they should go to the 'log in' page. They are then be directed to their personal home page. From here they can view their current jobs or click the 'create a job' button. This takes them to the 'create a job' page. This page contains a form from which they upload details and images. When a job is created it is placed on the job board from where CAD professionals are able to view and bid on it. 

If the job owner would like to know more about the users who are bidding on their job they are able to click on their 'username', which takes them to a details page about that user. Once happy with a bid, they can press the 'accept bid' button. This job is then only available for view by the job owner and winning bidders boards under 'jobs under way'. They should then wait to receive the documents from the winning bidder when they have completed the work and then make the payment.

#### Bidding on a job

As previous, to be able to bid on a job you must first create an account. When logged in you would then go to the 'view jobs' page where you see all jobs uploaded by fellow users. Selecting one of these jobs takes you to that particular jobs page, from where you can view more details and images. If you would like to bid on a job you would press the 'make a bid' button. This brings up a modal that contains a text box that expects a currency value and a 'confirm bid' button. Once pressed this then appears in your personal page under 'jobs you have currently bid on'. If successful (the job owner selects the 'accept bid' button) the job appears in the 'jobs under way' board of the users personal page.

#### User want to read or upload blogs

The blog section is created to allow users to understand more about the industry or to share their insights with others. To view blogs, you do not need to be logged in. On the home page you can directly and read the three most recently uploaded blogs, or click the 'view more' button, which redirects the user to the 'blogs page'. Once here they are able to select any of them and read the whole article. If a user would like to upload a blog they would either need to sign up or log in. Once on their personal page, they would be able to click on the 'create a blog' button. When here they are taken to a form from where they would be able to write, upload images and 'submit'. This blog would then appear on the main blog section of the website. If the user is logged in and select a blog they have uploaded they would get to either update/edit or delete the post.

#### Shop/Products

A user can go to the shop/products page of the website if they are starting out in the industry and find a selection of related products. If a user wishes to buy a product they can click on the 'add to basket button'. This adds the products to the cart. The user does not need to be logged in or have an account to be able to purchase the products. 

## Features

Features are functionality that has been added to different areas of the site.

### Jobs

The jobs section (uploading and bidding) contains functionality that enables the users to be able to view the position of a job at any time. The pressing of the buttons moves the job between, being able to bid, active job and completed job. The job owner and the chosen bidder are able to share files between each other on the 'job page'. 

### Blog

The blog contains the functionality to be able to upload, update and delete the post. This, as previously mentioned is only available to those users who are logged in.

### Shop/Products

As with most products/shops online, the products section gives the users the ability to view products, add to their shopping cart and pay for products.

### Payment systems

The functionality of accepting creadit and debit card information is taken care of.

## Technology Used

This project was built using different languages, libraries and frameworks. 

### Frontend

The template pages have been written with HTML5 (http://www.html5.com/) and styled with CSS3 (www.css3.com) in the style.css file which is held within the staic folder. CSS3 was used to create the mobile responsiveness seen across the whole site. It has also been used to create the hover effects for the buttons and icons. On each of the pages, you will find the jinja template engine used. A 'base.html' page has been created to contain the HTML code that is to be used on each of the pages i.e. the head, header and the footer.

The Bootstrap library has been used to style portions of the site, including the forms, buttons and modals.

jQuery (https://jquery.com/) has been used in the navbar to control the dropdown menus. Javascrpt has been used on the home page for the scrolling image at the top of the page (https://www.javascript.com/). DC and D£ charting libraries are used within a users personal page to show how many jobs they have completed and how many jobs they have currently bidded on and won.

### Python

The site has been built using the Python based Django framework (https://www.djangoproject.com/) and is run from the 'manage.py' file which is stored in the outer folder. Within the main folder you can see the list of apps that have been created to deal with the different functionality of the site. These are:

* Home App - This deals with the home page, about page and the contact form.
* Jobs App - Deals with the uploading of a job for a job owner, the bidding on a job, accepting bids and the messages and payment between the parties.
* Users App - This deals with the sign up, login and reset password functionality.
* Blog App - This deals with the create, edit, delete and the viewing of the blogs
* Products App - This deals with the viewing, cart and checkout functionality of the products/ shop.
* cadwork is the main app file. 

The 'jinja template engine' (http://jinja.pocoo.org/) has been used within the html template pages already described.

### Payment Methods

The products from the shop, if added to the users cart can be paid for through the 'Stripe API'. This is connected to the site.............

### Data Storage

### Version Control

Git was used throughout the project for version control.

## Testing

The CSS was run through a CSS validator and errors were corrected. It now shows no errors. The javascript/jquery code was validated using jshint and showed no errors.

The site has been tested manually by clicking the links to the pages and checking all of the jQuery options. It has also been tested in different browsers.

Accounts have been created and I have created jobs, bid on jobs to ensure that all functionality works well for new members. 

## Further Considerations

### Blog

I would add a comments section to the blog, allowing members to add their thoughts. The users would need to be logged in to access this functionality. Using the same methods as with the navbar and using is_authenticated. If the user is authenticated then a button would be placed at the bottom of the blog. To press this would bring up a textbox, which would be contained within a form. When this was submitted the message would appear at the bottom of the blog.

## Deployment

This project has been deployed to both Github and Heroku by using the push command in the terminal.

If you would like to contribute to the project can be cloned or downloaded from the Github link provided below. 

The individual files on Github can be found via ................https://github.com/JShad30/the_recipe_store.............., and the website can be viewed via ...............https://solar-system-quiz.herokuapp.com/...............

## Credits

### Media

The images used on the front page for the scrolling header and the meal type pictures are taken from Pixabay, except for the house extension picture, which was taken from https://www.bbc.co.uk/news/uk-england-48405569.

Images for the products have been taken from Amazon, Toolstation, Walmart, Athletics Direct, RS Components, dhgate.com and programsfull.org.

The default user face image has been taken from nepad.org. The users personal page default header image was taken from https://photodune.net/item/architect-drawing-architectural-project/21372430.

### Acknowledgements

Throughout the project I received support from the mentor and the tutors.
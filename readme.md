# My Blogs

## Description
This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. Also displays random quotes on the site

## My Blogs
The user would like to.... :
*  View the blog posts on the site
*  Comment on blog posts
*  View the most recent posts
*  An email alert when a new post is made by joining a        subscription.
* See random quotes on the site

The writer would like to... :

* see random quotes on the site
* sign in to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading.
* update or delete blogs I have created.




## Behaviour Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| all blogs | Signup if no account | Taken to the clicked blog | Click on `Comment`
| Click on `Click Add a blog` | If logged in, display form to add a blog| Redirected to the all blogs page and all blogs displayed 
|Delete blog | Delete a blog | Redirected to the all blogs page
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
| Click on Sign Out | Redirects to the home page | Signs user out |


## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip
* flask


## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Flask
* Boostrap
* HTML
* CSS

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
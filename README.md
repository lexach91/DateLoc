# Code Institute's February Hacakthon: Valentine's - Share the love

## Project: Escapade - Let the location make the match

## Team: (Insert team name)

![Multiple Device Demo](add image from techsini.com)

## Live Site

[Escapade](https://escapade-match.herokuapp.com/)

## Repository

[Escapade](https://github.com/lexach91/DateLoc)

## Contents
- [Purpose](#purpose)
- [Objective](#objective)
- [User Experience](#user-experience)
    - [User stories](#user-stories)
        -   [First Time Visitor Goals](#first-time-visitor-goals)
        -   [Returning Visitor Goals](#returning-visitor-goals)
        -   [Frequent User Goals](#frequent-user-goals)
    -   [UXD User Experience Design](#uxd-user-experience-design)
        -   [Colour Scheme](#colour-scheme)
        -   [Typography](#typography)
    -   [Wireframes](#wireframes)
-   [Features](#features)
    - [Current Features](#current-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Other Technologies](#other-technologies)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)





## Purpose
The purpose of this project is to work collaboratively in a small team to
build a project relating to the Code Institute's February Hackathon:
Valentine's - Share the love.

## Objective
Escapade is a location based dating app, designed to take away some of the pressure
users feel when trying to find a match. Rather than simply matching based on looks, Escapade
puts the focus on the location of the date. Users swipe left or right to choose their desired location,
and Escapade will match them with someone who also likes the chosen location.
Users can then chat to get to know one another before agreeing to meet.

By going through this process, users will have a common interest in the location to break the ice, and 
potentially find love, with an amazing first date story.

## User Experience

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site
        1. As a First Time Visitor, I want to be able to create a profile and enter my details
        1. As a First Time Visitor, I want to to choose my the gender I identify with rather than male or female.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to login to my account and continue where I left off
        1. As a Returning Visitor, I want to find a match and chat to them
        1. As a Returning Visitor, I want to know which locations are being used in the app

    -   #### Frequent User Goals
        1. As a Frequent User, I want organise a date with my match, and continue talking to them afterwards
        1. As a Frequent User, I want update my profile details
        1. As a Frequent User, I want to match and chat to several people seperately to see who I connect with

-   ### UXD User Experience Design

    -   #### Colour Scheme
        -   To make the app fun and inviting, a purple gradient background is featured on all pages. with content 
            set into a translucent 
    -   #### Typography
        -   Open Sans is used for the majorty of the site for its ease of readability, to complement that and give a slight difference,
            Roboto is used for the buttons throughout the site.

### Wireframes

[Wireframes - Seperate document](static/readme-content/wireframes.md)

Click above to view all of the wireframes for mobile, tablet and desktop.

## Features

### Current Features

1. Create Account
- Users can click here to create a username and password for the app. Users must confirm their password to prevent mistakes. Parameters are
listed next to the relavent input for what can and cannot be used.

1. Sign in
- Users who have already made an account can sign in with their credentials and all of their chats and profile
details are saved.

1. Profile
- Users can view their current profile details, including profile pic, age, bio, relationship status etc.

1. Update Profile
- Users Can edit all of the details previously mentioned here, and save them or cancel the changes.

1. Location Match
- Users can choose from a list of locations, then see other users who have also liked that location.

1. Chat
- Once users choose who they want to chat with, a chat window will open for them to converse and organise a meetup.

### Features Left to Implement

1. The concept of this app could work in anywhere in the world, and could be limited to a single city, with the location options
    being a restaurant or park. For this reason, it would be helpful to have images displaying as well as the location name, so users
    can get a feel for the places they like.

1. With this in mind, users could also rate the locations for other users to see and make a decision based on this.

1. When matching with a person, it could be useful to have the other user's profile picture appear. Currently the app works as a blind date
    type thing, but matching a picture to a name would make users feel more secure.

1. A report button for users to give feedback on other negative users. This can then be investigated through chat logs and users can be removed
    if necessary.

## Technologies Used

### Languages

1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
1. [CSS3](https://en.wikipedia.org/wiki/CSS)
1. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
1. [Python](https://en.wikipedia.org/wiki/Python_(programming_language)

### Other Technologies

1. [Django](https://www.djangoproject.com/)
    - Framework used to build the site/app. Admin console stores user details and locations, allowing us to
    quickly edit 
1. [JQuery](https://jquery.com/)
    - Library used to send Ajax requests more easily.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the Open Sans and Roboto fonts.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [TinyPNG:](https://tinypng.com/)
    - TinyPNG was used to compress image file sizes.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [Wireframes](static/readme-content/wireframes.md) during the design process.
1. [Heroku](https://dashboard.heroku.com/login) 
    - Site used to host the deplyed version of the app.
1. [Amazon Web Services](https://aws.amazon.com/?nc2=h_lg)
    - Used to store static data.
1. [Cloudinary](https://cloudinary.com/)
    - Would have been used to add images to the locations. See features left to implement.

1. [Github](https://github.com/)
    - Used to remotely host the repository and allow us to branch and merge requests individually

## Testing

### Manual Testing

Thorough manual testing was done throughout the development of the app to ensure that any new features were not
negatively impacting the rest of the site.

### Further Testing

-   The Website was tested on Google Chrome, and Safari on iOS and iPadOS.
-   The website was tested on Chrome, Safari and Firefox on laptop and desktop.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPad, iPad Pro, iPhone7, iPhone X, iPhone SE & iPhone 12.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
-   I tested the page using GoogleDev Tools Lighthouse feature on both mobile and desktop settings

## Deployment

### Heroku

- Navigate to your [heroku dashboard](https://dashboard.heroku.com/apps)
- Click "New" and select "Create new app".  
- Input a meaningful name for your app and choose the region best suited to
  your location.
- Select "Settings" from the tabs.
  - Click "Reveal Config Vars".
    ![Config vars button](
  - Input `PORT` and `8000` as one config var and click add. 
- Select "Resources" from the tabs.
    1. Select "Heroku Postgres
    1. Choose your desired plan name from the dropdown
    1. Click "Submit Order Form"
    1. Your add on should appear in the list
    1. Now search for "Heroku Redis" and follow steps 2-4.
- Select "Deploy" from the tabs.  
  - Select "GitHub - Connect to GitHub" from deployment methods.  
  - Click "Connect to GitHub" in the created section.  
  - Search for the GitHub repository by name.  
  - Click to connect to the relevant repo.  
  - Either click `Enable Automatic Deploys` for automatic deploys or `Deploy
    Branch` to deploy manually. Manually deployed branches will need
    re-deploying each time the repo is updated. Automatic will build the app
    each time you use you add, commit and push new code.
  - Click `View` to view the deployed site.

The site is now live and operational

---

## Credits

### Code

-   [Django](https://www.djangoproject.com/)
    - To quickly build and edit dynamic apps rather than editing individual pages.
    This gave the whole site a more connected feel by making each page look similar to the others.
-   [Django Channels](https://channels.readthedocs.io/en/stable/)
    - Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.
-   [Codemy.com Youtube Tutorial](https://www.youtube.com/watch?v=EqjRhO5CK6A)
    - Used to help build the 'register users', 'login' and 'logout' functionality

### Content

-   All content was designed and created by the 5 contributors
    - [Aleksei Konovalov](https://github.com/lexach91)
    - [Aws Sabah Gheni](https://github.com/AwsSG)
    - [Shiba Deb Github](https://github.com/shiba517)
        - [Shiba LinkedIn](https://www.linkedin.com/in/shiba-deb-2099b6105/)
    - [Steve Dawson](https://github.com/Steven-Dawson18)
        [Steve's LinkedIn](https://www.linkedin.com/in/steve-dawson-fullstack/)
    - [Tom Ainsworth](https://github.com/Tom-Ainsworth)
        - [Tom's LinkedIn](https://www.linkedin.com/in/tomainsworth94/)

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

[Wireframes - Seperate document]()

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

1. 

## Technologies Used

### Languages

1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
1. [CSS3](https://en.wikipedia.org/wiki/CSS)

### Other Technologies

1. [Pexels:](https://www.pexels.com/)
    - Pexels was used for royalty free images seen in the Hero Image and Shows sectons.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Domine' font into the style.css file which is used throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for the footer social media icons.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [TinyPNG:](https://tinypng.com/)
    - TinyPNG was used to compress image file sizes.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [Wireframes](assets/readme-content/wireframes.md) during the design process.
1. [W3Schools:](https://www.w3schools.com/)
    - W3Schools was used for quick access to tutorials, particularly for CSS.

## Testing

### Code Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_uri) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftom-ainsworth.github.io%2Fblackshaw-theatre%2F)

![HTML Result](assets/readme-content/images/w3school-html-validation.png)


-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftom-ainsworth.github.io%2Fblackshaw-theatre%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS Result](assets/readme-content/images/w3school-css-validation.png)
    - 6 Warnings were found, with 4 relating to the nav bar border colour being the same
        - 4 warnings about the nav bar border colour being the same as the background. This was due to the hover effect and so was not a concern.
        - 2 warnings were related to code applied to placeholder colour, necessary when using the website in various browsers. I was also happy with this code being included.
    

### Testing User Stories

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text and a brief description about the company.
        2. The main points are made immediately with the hero image
        3. Beneath the description are 2 calls to actions, users can find out more, or get in touch. With the fold displaying more content to encourage scrolling. 

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid, with a clear navigation bar with links to all sections of the page. 
        2. As mentioned, the call to action buttons are strategically placed between sections to give users something to interact with.
        3. On the Contact Us Page, after a form response is submitted, the submitted form loads on a seperate tab, so the user can go straight back to the site should they wish.

    3. As a First Time Visitor, I want to view the site on multiple devices at different times, and want the experience to be the same on all devices

        1. I created media queries to keep the user experience the same on the vast majority of screen sizes, with responsive text and images throughout.
        2. I added column-counts for tablet and desktop screen sizes to minimize scrolling, and display relevant content in the correct order. No sections overlap so the information heirarchy isn't disturbed.
        3. I added multiple hero image files depending on the screen width. I wanted the hero image to be appropriately sized as it is the first thing users see when the open the site.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find out who is behind Blackshaw Theatre and what they do.

        1. The Tell Me More call to action takes users straight to the About section for quick access.
        2. All of the About images display info about the respective staff member when hovered over, empowering users to see the information they want. This also draws focus to the individual to help users concentrate on what they're looking at.

    2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

        1. Below each show is a call to action to "get in touch" which takes the user to the contact section of the page.
        2. The whole site has a white background, apart from the contact form. This change of colour creates an emotive response for the user that the interaction on the page has changed, from viewing content, to submitting their own content.
        3. The footer contains social media links to Blackshaw Theatres pages. Some users are more familiar with communicating through these sites rather than via email, and so may choose to message through there. All links open in seperate tabs to keep focus on the main site.

    3. As a Returning Visitor, I want to find see what kind of presence they have on social media sites
        1. As mentioned above, should a user wish to simply browse the socials, they have the option to do so with the footer links.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any new shows out to see.
        1. I changed the navigation bar name from "what's on" to "shows" during the site creation. This saved space on smaller screen sizes, allowing the nav bar to remain on one line, and also made it crystal clear what the section was relating to.
        2. Every show on the site is listed with the same format, making users feel comfortable and in control as they browse the site. This also allows future shows to be easily added or edited by another contributor.
        3. All shows include a link to the contact form in case users want to find out more.

    2. As a Frequent User, I want to purchase tickets for the shows while still being able to come back to the site
        1. Next to the "get in touch" button is a link to the relavent page to purchase tickets for the show. All of these pages are trustworthy, and users can feel safe being directed by Blackshaw for their own shows, rather than searching through 3rd party sites.

    3. As a Frequent User, I want to work with the company to produce a show, and speak with the owner directly.
        1. Throughout the page are CTA's linking to the contact form, and a specific input for businesses/companies to tell Blackshaw who they are.
        2. In the about section, users are introduced the the owner of Blackshaw Ellie, who managed the emails and social medias herself. When she replies to users they will feel safe knowing they are talking tot the owner, rather than someone else in the company.

### Further Testing

-   The Website was tested on Google Chrome, and Safari on iOS and iPadOS.
-   The website was tested on Chrome, Safari and Firefox on laptop and desktop.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPad, iPad Pro, iPhone7, iPhone X, iPhone SE & iPhone 12.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
-   I tested the page using GoogleDev Tools Lighthouse feature on both mobile and desktop settings

### Lighthouse Results

#### Mobile

![Mobile](assets/readme-content/images/lighthouse-result-mobile.png)

#### Desktop

![Desktop](assets/readme-content/images/lighthouse-result-desktop.png)

## Bugs

### Known Bugs
-   When reducing the site from around 1775px to 1575px, the About section images overlap slightly. The screen sizes I tested the site on do not show this at all, I only noticed it when manually dragging the screen down through these dimensions, as seen here:
![Known Bug](assets/readme-content/images/bug-1.png)

### Fixed Bugs
- At first the hero image was set within HTML based on mobile device sizes. When it came to making the site responsive, I found it difficult to implement the picture element, and so opted to change this to a background image within CSS. This gave me far more flexibility to style the image, and meant that I could swap the image out with media queries, making the site look much better on all screen sizes.

- The text overlay on top of the hero image was only featured at the bottom of the screen on the W3Schools tutorial, so I had to figure out how to add it to the top as well. This went through several iterations of position changes, before I separated the text into cover-text-top and cover-text-bottom IDs. This made it much easier to style the text in relation to the hero image.

- The shows section wouldn't scale into multiple columns like the about section does. I would have liked it to display the show info, with the image below. However it would only split the text on the left, and the images on the right, which wasn't very appealing to look at. I tried the same method I used for the about section, seperating the shows by classes: "show-1, show-2" which gave this result:
![Show bug 1](assets/readme-content/images/bug-2.png)

I then tried adjusting the section as a whole, so that the content of each show div would stay together. However the h2 tag wouldn't stay central, and the buttons from the first show were being cut in half.
![Show Bug 2](assets/readme-content/images/bug-3.png)

I actually fixed this bug as I was writing it down as a known bug. I simply added a container to the shows section, and left the h2 tag outside of it, therefore allowing the h2 to stay central, and giving the buttons enough room beneath the image. This one was very satisfying to fix!
![Shows Bug Fix](assets/readme-content/images/shows-bug-fix.png)

- The overlay was causing me issues on the about section. I knew that I wanted to implement it quite early on, as I found it while researching image tags on [W3Schools](https://www.w3schools.com/howto/howto_css_image_overlay.asp). Tweaking the CSS properties from the code given took a lot of experimenting, as the positioning was very important to maintain the look of the site. As there are several class selectors, I needed to ensure I was calling the correct HTML, as my class names were different to that of the tutorial. I wanted to make this feature repeatable within a container "staff-bio" in case the client wanted to add any more staff members. At first I had indiviual height and width values for all selectors, however later decided to add inherited values to help with site maintainence.

- As I knew the site would be scaled up, I tried to make all text responsive from the get go, using the vw property to unify all elements of the same type. This worked quite well for mobile and tablet, but meant that desktop text was far too large. I researched more standardised sizings and noticed that major sites such as Apple, Facebook and Youtube had very similar pixel values for the relative elements. After adding these to media queries, and adjusting the primary sizing, the page looked far better when resizing the screen.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Tom-Ainsworth/blackshaw-theatre)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://pages.github.com/) for a page with instructions on how to use Github Pages
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Main".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://tom-ainsworth.github.io/blackshaw-theatre/) in the "GitHub Pages" section.

## Credits

### Code

-   The full-screen hero image code came from this [Pexels page](https://www.pexels.com/photo/silhouette-photography-of-people-on-theater-1714361/)

-   [W3Schools](https://www.w3schools.com/) : For various tutorials and explanations of properties. 
    - Code was used and adapted from [This Tutorial](https://www.w3schools.com/howto/howto_css_image_transparent.asp) for the text overlay on the hero image.
    - Code was used and adapted from [This Tutorial](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_overlay_fade) for the Overlay images in the About Section
    - Code was used and adapted from [This Tutorial](https://www.w3schools.com/howto/howto_css_placeholder.asp) to change the placeholder colour within form inputs on various browsers.
    - Code was used and adapted from [This Tutorial](https://www.w3schools.com/howto/howto_css_animate_buttons.asp) to create the animated submit button on the contact form.
- Code was used from [Google Fonts](https://fonts.google.com/) to import the font family within my CSS file.
- Code was used from [Font Awesome](https://fontawesome.com/) to add social media links in the footer.

### Content

-   All code was written by myself apart from the segments above, which were adapted to suit the sites needs.
-   README.md Template courtesy of Code Instite, with layout inspiration from [Dave Horrocks](https://github.com/DaveyJH)

### Acknowledgements

-   Ellie Pitkin, the owner of Blackshaw Theatre for allowing me to use the company site for this project.

-   My Mentor Antonio Rodriguez for helpful feedback and ideas.

-   The September 2021 Slack group for constant support for one another and bumps when feeling overwhelmed.

-   Fellow CI student Dave Horrocks for quick and incredibly helpful tips on several occasions, and for providing an inspiring project to work towards.


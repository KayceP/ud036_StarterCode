# Fresh Tomato.es - v0.1

Welcome to Fresh Tomato.es! With this program you can easily generate a list of your favorite movie trailers, and add or edit your own. The code is meant to be easy to understand, and very customizeable.

## Getting started

To view the full rendered layout, with our built in sample trailers, extract all the files to a folder on your computer. Once extracted, run 'entertainment_center.py' to execute the code. A web page will open in your default browser, and you'll see our default picks!

### Customization

To customize your own list of trailers, the only file you need to edit is 'entertainment_center.py'.

You can add your movies inside 'entertainment_center.py' with the following format:

    movie_title = media.Movie("Movie Title",
                            "Summary",
                            "Direct link to poster",
                            "Direct link to trailer")

After adding any new movies, the last step is to add the variable for each entry, in this case 'movie_title' to the 'movies' entry at the end of the file.

    movies = [movie_title, movie_title]

You're all done! Save and run 'entertainment_center.py' to enjoy your new additions.

### Credit

- Base code was forked from [adarsh0806](https://github.com/adarsh0806).
- Movie summary on hover was developed from code by [banzomaikaka on Stack Exchange](https://stackoverflow.com/users/1171873/banzomaikaka).
- Full page image header code from [w3schools.com](https://www.w3schools.com/howto/howto_css_full_page.asp)
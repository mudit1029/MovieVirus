# MovieVirus

Ability :- 

This project contains two apps :-

1. Movies :- This app allows the user to add movies into the database and fetch information of the movie using IMDB Movie ID and TMDB Api Key.
             This app also have the feature to provide download links of movies and screenshots of the uploaded movie quality type.
             
2. Users :- This app allows the user to create account , login and logout the user , shows details of the user , forgot password function whith OTP generation and sending email to the provided user email id.

Steps to use the project :-

1. Clone this repository and heads up to the project folder.
2. Open terminal and type  ----  winpty python manage.py createsuperuser
3. The above command will ask for the user credentials to register , after completion user will set to be as a superuser or admin.
4. After that in the terminal type  ----  python manage.py runserver
5. The above command will start the server at the base route ,i.e, http://127.0.0.1:8000
6. Open Browser and type the above base route in the url bar.
7. Browser will open the Index Page or the Home Page of the website.
8. Head up to the Login / Register Button and login with the superuser credentials.
9. After login user will redirected to the Home Page and it shows add movies button.
10. Click on it and type IMDB movie id , for example - tt156324 , and type TMDB Api key which you have to get from https://tmdb.com by creating the account.
11. Click on fetch button which will fetch the details of the movie , after successfully fetching of details click on add to database button.
12. Now your movie is added in the database.
13. Now go to the admin route ,i.e, http://127.0.0.1:8000/admin , and click on movies section to see the added movie.
14. Click on the added movie and and set publish field to TRUE or click on publish checkbox and click on save.
15. After saving head up to the base route , and you will see your uploaded movie their.

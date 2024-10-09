# INFOB318

Acronyme: Digi-Sm

Title: Digital Scrum master

Client: Nicolas Matton

Student: Richter Benjamin

## Description of Project

Digi-Sm or Digital Scrum Master is a website designed to help you and your team develop projects and to learn
and apply the agile methodology. Its easy to use and can help your entire team get on board about what
user stories are left and the priority of these. You can create and input all your user stories at once
and then create your sprints as you go along. This is designed to help you stick to a schedule and visualise your project.
!A more detailed description and visual of the website can be found on the readme.md within the code file!
This one contains both mermaid diagrams but also a short explanation of the routes of the website

## How to launch the website

A basic graphic interface was created in order to facilitate the launching of the website.

Simply go in the /bin folder and, if python is added to your enviroment variables, if not see bellow, simply click
on the launchServer.bat file. This will launch the interface and give you the choice of
creating, loading or loading dummy data into the database in order to use the server.

This will open a first cmd window to check if you meet the requirements and download them if not.
And then a second window opens launching the server.
All you have to do to access it is then entering 127.0.0.1:5000 in any browser and you're ready to go!

Just be careful that creating or loading dummy data will overwritte the existing database.

python not in your env variable: then you have two options, either add it or go in the .bat file and edit the first py.exe by the path to your python module

notes to linux user:
The .bat file won't work so you'll have to manually go into the ./code/Digi-sm folder and execute the following two commands

- pip install -r requirements.txt
- python run.py

and you're ready to go on 127.0.0.1:5000

## To access admin features

Username : admin123

Password : admin123##!wqeq

## More details

A more detailed description accompanied by visuals can be found in the readme.md of the /code/Digi-sm folder

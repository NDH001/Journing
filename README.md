# Journing - Django and JQuery based web application
![index](project_imgs/index.png)

## Table of Contents
- [Overview](#Overview)
- [Installation](#Installation)
- [Documentations](#Documentations)
- [Disclaimer](#Disclaimer)
 
## Overview
An innovative web application developed using the Django framework in conjunction with JQuery, designed to facilitate seamless user interaction with comprehensive travel information - which was pre-scrapped from ctrip.com and are stored in the local postgres database. This platform empowers users to efficiently navigate and explore travel-related data, engage in commentary, establish interconnected communities, and notably, plan and curate individualized travel itineraries.

The web page provides several key functions which includes but not limited to :

**1. User authentication and registration**
![regi](project_imgs/regi.png)
![login](project_imgs/login.png)

**2. Browse travel information ( Data scrapped from the chinese version of trip.com --> ctrip.com )**
![cities](project_imgs/cities.png)

**3. Establish connection between users**
![connection](project_imgs/connection.png)

**4. View and make comments on attractions or topics**
![comments](project_imgs/comments.png)

**5. Mark attractions/restaurants/shops** 
![mark](project_imgs/mark.png)

**6. Customize personal travel plan with the pre-marked collections**
![journal](project_imgs/journal.png)

#### Responsive mobile design 
Although the project was built with desktop users as the main audience, however, most of the features can also be access through mobile phones with proper responsive design. 
Tested with IPhone Xr and Oppo R17 , this does **not** guarantee proper styling on all mobile devices.
<img src='project_imgs/m_cities.jpeg' style='width:22%;display:inline;'>
<img src='project_imgs/m_collection.jpeg' style='width:22%;display:inline;'>
<img src='project_imgs/m_detail.jpeg' style='width:22%;display:inline;'>
<img src='project_imgs/m_journal.jpeg' style='width:22%;display:inline;'>

## Installation
Follow the installation step and set up the project.
  
1.  **Clone the Repository:** Begin by cloning this project to your local repository using : 
`git clone https://github.com/NDH001/Journing.git`
2.  **Install Dependencies:** Navigate to the project directory and install the required dependencies by running: `pip install -r requirements.txt`
3. **Database Migration:** Apply the necessary database migrations with the following command:
`python manage.py migrate`
4. **Import Data:** Import the pre-scrapped travel data to the postgres database by running : `psql your_database_name < migrates.sql`
5. **Run the Development Server:** Launch the development server using: `python manage.py runserver`

## Documentations
The objective of this segment is to furnish comprehensive elucidation pertaining to the project in question. The documentation encompassing elements such as the product backlog, database schemas, prototyping documents, and the Gantt chart, is enumerated herewith.

**1. Product backlog & Gantt Chart :** The project is founded upon an Agile methodology coupled with the Scrum framework. Each week is designated as a discrete sprint, wherein the activities encompass the stages of application development, thorough review, and rigorous testing. The project encompasses a timeline extending over a duration of three months, commencing with data scraping and subsequently progressing to the substantive phases of application development.
![Backlog](project_imgs/product.png)
![gantt](project_imgs/gantt.png)

**2. Data Scrapping :** The data available on the website is pre-scrapped from ctrip.com, the [project](https://github.com/NDH001/travelWeb_scrapper) has detailed source code and steps on how to scrap for data used in this project.

**3. Database schemas :** The database consist of  4 schemas , each segement responsible for storing related data and contents. Click [here](project_imgs/database.pdf) for the original pdf.

**4. Prototye:** This subsection contains some of the initial design and ideas for the website. 

<img src='project_imgs/1.png' style='width:100%;display:inline;'>
<img src='project_imgs/2.png' style='width:100%;display:inline;'>
<img src='project_imgs/3.png' style='width:100%;display:inline;'>
<img src='project_imgs/4.png' style='width:100%;display:inline;'>
<img src='project_imgs/5.png' style='width:100%;display:inline;'>
<img src='project_imgs/6.png' style='width:100%;display:inline;'>
<img src='project_imgs/7.png' style='width:100%;display:inline;'>
<img src='project_imgs/8.png' style='width:100%;display:inline;'>
<img src='project_imgs/9.png' style='width:100%;display:inline;'>



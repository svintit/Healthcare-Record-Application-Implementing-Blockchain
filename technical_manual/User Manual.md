User Manual 
==
_Medical Database Implementing Blockchain_ 

_3rd Year Project_ 

_Traian Svinti 14432128_ 

_David Talan 14387991_ 

_Supervisor: Geoff Hamilton_ 

  

Section 1 – Index page/First page 
--
In the beginning we are presented with the index page which is our first page. This page is accessed through the url http://127.0.0.1:8000/personalInfo/. This page shows the general layout of the system, logo and two buttons. These two buttons are crucial to the usability of the website specifically for the doctor. 

The button on the left has the label "Existing Patient". This button brings either the doctor or patient to the login page described later in this manual. As long as the user has been created before, this is the only page the patient should need. 

The button on the right presents a label called "New Patient". When clicked the user is redirected to the admin login page which is specific to doctors only. 

A patient cannot use his/her credentials to access the admin page as only a doctor's login credentials will work. A doctor can use his/her credentials to login as a patient as doctors can also be patients and have information in the database. 

An image of this page is shown below. 

![](https://i.imgur.com/tYiTYk4.png) 

  

Section 2 – New Patient Admin Login (Doctor) 
--

When the doctor presses the "New Patient" button, he/she will be redirected to the admin log in page. This page can only be accessed by users with 'superuser' accounts which patients cannot have. 

![](https://i.imgur.com/GMN7Akm.png) 

Section 3 – Admin Adding Users 
--

Once a doctor is logged in through the admin login page as above, they are shown 2 options; 'Users' and 'User profiles'. 

To create a new user, the doctor should press 'add' beside 'Users'. ![](https://i.imgur.com/2yVDCmp.png) 

We are then presented with this page: 

![](https://i.imgur.com/GHfhkSb.png)Input all information necessary and press save. Once this is completed press the home button and click on 'User profiles' under 'Users'. 

This will display all user profiles whether new and empty or previously created profiles that can be edited. Input all necessary information for the patient and save it. This will now be saved in the database. 

![](https://i.imgur.com/4iZdoTZ.png) 

Section 4 – Existing Patient Login (Patient)
--

Once the patient/doctor presses the button "Existing Patient" from the first page, they are presented with a login page. This login page can only be accessed by previously created patients which were created by a doctor. 

The patient can input their 'username' and 'password' to access their information. If incorrect credentials are used the page will refresh and the patient will have to re-input their credentials. If the correct details are entered the patient will be redirected to his/her information. 

An image of this page is shown below. 

![](https://i.imgur.com/azUoKN2.png) 

Section 5 – Viewing profile information (Patient) 

When the patient completed logging in as shown above, they are then presented with their information in a clean and simple UI. We are presented with multiple tabs. These tabs each show different information that the patient has. 

![](https://i.imgur.com/95RNg2k.png)![](https://i.imgur.com/SZ2DDXi.png) 

![](https://i.imgur.com/YYNVWXP.png)![](https://i.imgur.com/1S9chAN.png) 


**Tables of Contents**
---
*1. Introduction
1.1 Purpose	
1.2 Overview	
1.3 Business Context.	
1.4 Glossary*	

*2. General Description
2.1 Product / System Functions	
2.2 User Characteristics and Objectives	
2.3 Operational Scenarios	
2.4 Constraints*	

*3. Functional requirements
3.1 Creating Profile	
3.2 Logging in	
3.3 Using the system/Navigating profile	
3.4 Web-app and blockchain database communication*	

*4. System Architecture
              4.1 Figure A – System Architecture Diagram*	

*5. High-Level Design
              5.1 Figure B – Context Diagram	
              5.2 Figure C – Data Flow Diagram	
              5.3 High-Level Design Description*	

*6. Preliminary Schedule
              6.1 Overview	
              6.2 Figure D – Gantt chart*	


---
Section 1 
-
**Introduction**
 
 
**1.1 Purpose**
This document will provide the functional specification designed to give a synopsis of the Healthcare Record Application Implementing Blockchain (Come up with a name please).  This will provide a reference for the system design and the intended audience is the project coordinator, project supervisor and the CA326 demonstration panel.

**1.2 Overview**

Our project is based on accessing medical records through a Blockchain database that is encrypted with public and private keys. Each block in the database will have a specific patient's medical records which can be accessed wherever the patient is. This is extremely beneficial when it comes to travelling or changing doctors. 
The project will entail a web app and a Blockchain database which will be accessed by the web app. The information in the Blockchain will be encrypted and the only way to access their records is through a public key which the doctors will have and a private key which will access the patient's specific records.

**1.3 Business Context**

This product will be used in Healthcare and Medical organizations as an elementary way of accessing medical records. The product will not have any third-party owners meaning only hospitals will have access to it and the specific patient. 


**1.4 Glossary**

•	*Blockchain*:
A continuously growing list of records, called blocks, which are linked and secured using cryptography.
•	*BigChainDB*:
Scalable blockchain database that will contain the records.
•	*Public/Private Keys*: 
These are numbers or passwords used to access and decrypt the Blockchain data.
•	*Nodes*:
Nodes can be referred to as the computers on which the Blockchain network uses.


---
Section 2
-
**General Description**

**2.1 Product / System Functions**

*Patient user functionality*

The web app will be accessed through a web browser by the patient. There will then be a page to login using the patient's key to view his own personal records. The patient will not be able to add data himself.

*Doctor user functionality*

If data needs to be added to the block a doctor must also use his key to login and add new data to the patient's medical data. This is done so the patient cannot add false information about his illness to acquire certain medicine. 

*Database interaction and Blockchain*

The web app will be connected to the database. We are using a database called BigChainDb which will host our Blockchain. Once data is entered into a patient's specific block a hash value will be created based on the data inside the block. This makes the blocks immutable as any value changed in a block will affect the hash value of all the previous connecting blocks.


**2.2 User Characteristics and Objectives**
This application is suitable for all people of all ages. The user requirements for the patient would be that they are computer literate and be able to remember or store their private key somewhere safe. If those requirements aren’t met due to illnesses or disabilities, ideally they would have a close relative that they could trust with the private key and come to doctor appointments with.

The requirements for the doctor are also the same as the patient but it would be optimal if the doctor is familiar with the app for ease of access.

We aim to provide an application that will provide a seamless experience so that in the case of accessing the records with different doctors or in different countries, the experience will be effortless and consistent no matter the situation.




**2.3 Operational Scenarios**
*Use Case 1 - Accessing record blocks*


The patient will produce their unique private key and combine it with the doctor’s public key in order to view the latest block in the blockchain that contains their healthcare record. They can use the different drop-down menus to access different information such as allergies, vaccines, all previous doctors, previous operations/surgeries etc.

*Use Case 2 - Doctor editing/adding information*
Once the block has been accessed, the web app will produce a healthcare record template that contains the current information of the patient and the doctor will be able to add on information and update any relevant information.

*Use Case 3 – Adding the record on to the blockchain*
After any changes have been completed on the healthcare record template, the doctor is then able to add that into a new block containing the new information.


**2.4 Constraints**

Below is a list of constraints that are put upon us for designing and creating this product and features.

*Time*
The time allotted for the project may not be very short but as there are also other modules and project/assignments to worry about working on the project constantly is a very hard task. As the project is due in April, the main bulk of the project will be done in the 2nd semester.

*Storing medical records*
We will not be using real medical records. For this project we will attempt to find out all the types of information that is stored in a medical record and create our own personas with random/made up medical records to show how the system runs and how the UI will look with the information.

*Speed*
This will mainly depend on the internet speed of the Internet Service Provider of whoever is trying to access the blockchain database. The blockchain is stored in different nodes in a blockchain network, so as long as there is sufficient internet speed, access to the blockchain shouldn’t be a big issue.

*Security*
Security is a very important precaution that we need to make sure works correctly. We need to test our encryption of the data vigorously as to not have any flaws in it. We also have to encourage the patients to be very careful of their private key and prevent sharing it unless they really need to.

*Ease of use*
Another constraint we may come across is the ease of use of the website. As there will be a lot of information needed to be displayed, we will create a user friendly interface that the doctors can use easily. We also need to make sure that navigating through the web application is made easy and the choice of font, text size and other design elements help provide a pleasant experience.



---
Section 3
-

**Functional Requirements**

**3.1 Creating Profile**

*Description*
Creating a patient's profile is the first thing that needs to be done to be able to use the system. Unlike other websites where a profile is needed to be created by the user the doctor creates the patient's profile with existing information about the patient already and information is added on consultations or any other procedures where the patient comes to the doctor.

Creating the profile also means that the patient will be given a private key that will give access to their own set of blocks in the Blockchain network. 

*Criticality*
Creating a profile is a critical process as without this there is no information to be viewed about the patient and the system becomes obsolete. The profile will show everything from basic information such as name, contact details, allergies to surgeries and previews doctors/medicine.

*Technical issues*
The main issue would be creating a simpler and quicker way of transferring existing data about the patient onto the system. Once this is solved a profile can be created very easily and all information will be easily accessed by patient or doctor.

*Dependencies with other requirements*
As creating a profile is essential to be able to use the system every other requirement will be based off this one. 



**3.2 Logging in**

*Description*
The doctor and the patient can view his/her profile together as described above by logging in by combining their private and public keys. This process is very secure as the combination of the keys is encrypted.

*Criticality*
The logging in process is essential to accessing specific profiles and medical data about patients and also making the data as secure as possible. Using the keys given will access the block with the patient's data.

*Technical issues*
The database must be able to find the specific block that is connected with the key/password that is inputted. Also, each login must be unique, randomly generated and very secure.

*Dependencies with other requirements*
This is the only way to access the profile that has been created. This is dependent on the previous functional requirement 3.1. This can only be used after a profile is created.


**3.3 Editing the patient's records**

*Description*
Once the doctor/patient has gained access to the profile by logging in, the doctor and patient now has the ability to view all of his/her details. These details will be easy to find and view. To edit the patient’s profile the doctor can press on the “+” button to add new data or the “edit” button to edit previously inputted data.

*Technical issues*
There will be difficulty in editing a patient’s record as a new block would need to be created to be able to accomplish this as the database is immutable. 

*Dependencies with other requirements*
Editing a record can only be done after the creating and logging in to the patient’s profile so this requirement is dependent on both 3.1 and 3.2 requirements to be able to be utilized.

**3.4 User and Blockchain database communication**

*Description*
When data is entered into the web app by a doctor, this data is encrypted and sent to a node which accesses the patient's blockchain database. The block containing the data is then added to the blockchain. Using this method of storing data is beneficial in many ways such as:
•	The data will be encrypted for the highest security so no one except the doctor and patient can access these records.
•	The Blockchain can be used as an immutable database meaning that it cannot be changed and we do not want medical files to be changed or removed.
•    There are no hosts for the Blockchain so no one owns      the data apart from the hospital and patient. Not having a third-party is beneficial as the medical data cannot be altered, meaning it can’t be used for fraud.

*Criticality*
This communication between the web app and database is critical as we do not want to store the data on the web page for everyone to be able to view. It would be a lot less secure without a Blockchain database. Also having separate user profiles would be a lot harder to accomplish without a database.

*Technical Issues*
One of our major issues would be storing the data efficiently and effectively to the patient's unique block. We also need to make sure that the encrypting and decrypting is working properly and we do not lose any data.

*Dependencies with other requirements*
This communication is dependent on 3.3 as there is no communication to the database involved without data being added to the web-app.
 

 
 ---
Section 4
-
**System Architecture**
**4.1 Figure A – System Architecture Diagram**

![](https://i.imgur.com/N5z5L3z.png)
---
Section 5
-
**High-Level Design**

**5.1 Figure A – Context Diagram** 
![](https://i.imgur.com/9cF2uA3.png)


**5.2 Figure B – Data Flow Diagram** 
![](https://i.imgur.com/P8MtdIg.png)


**5.3 High-Level Design Description**

•	*Log in*
Once the profile is created by the doctor, the combined public key and private key from both the doctor and patient will retrieve the data and be displayed in the web-app.

•	*Creating Profile*
Once logged in, the profile can be edited only by the doctor and not the patient. Once the required changes are made a new block is created with the updated data.

•	*Searching database*
After access has been given to the web-app, the database will be searched for the patient’s specific block that matches the combined keys.

•	*Returning data from block*
When clicking on a certain drop-down menu the data from the block for that specific menu will be returned from the node to the web-app.

•	*Log Out*
Once the session has finished there will be a log out button to close the patient’s profile.

---
Section 6
-
**Preliminary Schedule**

**6.1 Overview**
The time schedule in figure D below was created using Microsoft Excel. It shows each of our activities (task and events) that we have accomplished and future undertakings. On the left of the Gantt chart we are shown a list of activities and along the top are a suitable time scale. Each activity is represented by a bar. The position and length of this bar reflects the start date, duration and the end date of each activity.

**6.2 Figure D – Gantt chart**

![](https://i.imgur.com/3w3p5FX.png)

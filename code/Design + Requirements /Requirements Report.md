Requirements Report
===

Healthcare Record Application Implementing Blockchain 

3rd Year Project 

Traian Svinti 14432128 

David Talan 14387991 

Supervisor: Geoff Hamilton 

User Demographic 
=====================

Since the project deals with people’s medical records, the target demographic consists mainly of doctors, patients, and possibly nurses and other hospital staff. The users would need to register with the website and create a user profile within it. It would also hold their public and private keys to be able to validate blockchain transactions. The most important users in the demographic would be the doctors as they would have the power to change the patient’s information in the medical record. 

Expertise with Technology 
==============================

When it comes to the technology required, the users would simply need a computer to use for the web app. Computers can be found in all hospitals, and doctors and nurses alike are usually trained to use any software in them. If they were introduced to a new website or application, they most likely wouldn’t struggle as they would be computer literate enough through their college education or training. However, there are also older doctors and nurses that aren’t as good with computers compared to their younger colleagues. 

When it comes to patients, their technological expertise will vary. The younger patients may be more accustomed to computers and navigating websites, so they would have an easier time using the web app. The older patient demographic would most likely struggle with a complicated website design with too much information in one page. 

With the demographic’s expertise with technology in mind, the decision was to design a simple UI that is easy to use. This would also help since the app would be used multiple times a day because the hospital staff would be accessing it more often than a patient would. If a doctor or nurse would be in a hurry, they wouldn’t be stuck trying to figure out how the app works. The website should also be usable by anyone, disregarding whether they’re good or bad in using a computer. This is to accommodate the patients that might want to view their medical record outside of an appointment or the hospital. 

Problem factors present in, or specific to, these user groups 
==================================================================

Intellectual Ability 
-------------------------

This factor concerns the users that are much older. A lot of elderly may not be as quick learning and intellectual as they once were. This may lead to a difficulty in trying to learn how to use the web app. 

Impairments 
----------------

A patient may have different types of impairments, either physical or cognitive that may prevent them from being able to use a computer. Having someone, a relative or a healthcare assistant, to help them use the website can greatly help. 

**Context of use **
===================

In what context will the user group use the product or service? 
--------------------------------------------------------------------

· A patient might need to use the application if they’re buying prescription medicine. 

· When a patient visits a doctor. 

· When a doctor decides to make changes, or add anything to the patient’s information. 

· If a patient is abroad and visits a hospital or a GP and need access to their records. 

· A patient might want to view it to create a ‘Care Plan’. 

When and where will this service be used? 
----------------------------------------------

· Hospitals/Private practices 

· Patient’s home 

· When abroad or on holiday 

Limiting factors/barriers 
------------------------------

· If a computer isn’t present 

· Internet isn’t working 

· A user has an impairment and is unable to use the application by themselves 

User Requirement analysis 
==============================

The group decided to use these methods to understand the user requirements for the application: 

1. Questionnaire 

2. Interviews 

Questionnaire 
------------------

Most software found online dealing with someone’s medical record, whether it be their full medical history or just a few medical details, costs money to use. This made it difficult to compare the application to an existing one because of the cost. An online questionnaire was created to gather information about what users might expect when using a healthcare record application. A few UI mock-ups were created for the proposal and this was used as part of the questionnaire to gather ideas. Questions like; is the text was too small, are the colours enticing and other questions were asked to help improve the interface and user experience. 

The questionnaire was shared online as everyone would have their own medical records once they do visit a hospital or a doctor. It was also passed on to hospital staff as David’s mother worked as a nurse. This proved very helpful because a lot of constructive criticism was received in the feedback section of the questionnaire. 

### Questionnaire Results 

The questionnaire had 60+ participants of varying age, mostly being aged 18-24 years old. However, the older demographic was also represented, with 5 users being 60+ years old. As the group expected, a large number of people (83%), has never seen their own medical records. 35% of them answered “Yes” when asked if they ever needed access to their medical record outside of the hospital. In regards to the mock-up questions, only 40% liked the overall look of the initial design. 74% thought that the elements, like the buttons and tabs, were too small. Finally, 56% didn’t agree with the colour combination on mock-ups. 

### Conclusion 

The group had predicted that the number of users that have never seen their own records would be high as they haven’t seen it themselves. Also, the fact that the majority of the participants were younger people may have played a big part to skew that figure. In 2009, the figure for hospital stays in America, whose patients aged 1-17, was 229 stays per 10,000. ((MD), 2009). In comparison, the number for those aged 65-84 was 3,084 per 10,000 and those who are older being 5,463 per 10,000 respectively. This explains why the survey yielded the result with the majority not having seen their medical record before. 

Regarding the UI that group created in the mock-up, it was also expected that the results to be quite negative towards it. However, it was unexpected that the elements did not satisfy the users. The group then agreed to move the tabs for accessing different pages to the top side of the page and remove the details of the patient being constantly displayed completely. It was also a surprise that the buttons shown were too small for the users, so that was also changed to satisfy the needs. 

Interviews 
---------------

The group allocated a few hours in the initial stages of the project to interview multiple people to gather more detailed information. Each interview lasted about 10 mins, with the interviews with hospital staff i.e. nurses, lasting a couple minutes longer. The questions that were asked were more detailed than the questionnaire. Questions included were; “What does/do you think a medical record looks like?” and asking them circumstances on when they think they would need access to one. 

With the interviews with the hospital staff, while showing them the mock-ups, their initial thoughts were noted down. The group asked questions like; “How could we improve this app for professional use?” and “How easy does it look to use?”. 

### Interview Results 

Overall, the interviews were a great a success. The comprehensive answers that the group collected greatly helped shape the design of the application and its functionality. The initial idea and aim of the design was shared with the users in the interview and it was met with their own suggestions for improvement. 

With the description of what the users think a healthcare record looks like, this gave the group an idea of what the template of the record would look like. Also, with the help of the hospital staff that deal with healthcare records on a daily basis, they were able to point out the most important information a doctor or patient might need access to immediately. 

### Conclusion 

The interview provided the group with a clear idea of how a user might interact with the application and also their expectations. Using the feedback from the people interviewed, it was decided to redesign the whole application from our mock-up to implement easier navigation throughout. The suggestions provided were used as a guide to create a painless user experience for the application. 

In terms of the healthcare record itself, with the help of the hospital staff, the group was able to formulate a template catered to the user needs. 

Requirements and Functionality 
===============================

A user should be able to: 

· Log in to the application and view their healthcare record, even outside of a hospital or without visiting a doctor. 

o View their healthcare record abroad in case they need to provide information when they visit a hospital. 

· Doctors should be able to log in to view and modify the patient’s record. 

· Doctor’s should be able to create a new “patient profile” for patients that have no previous record. 

Usability Considerations 
=========================

Impairments 
------------

Many users, especially the elderly patients would have many physical or mental impairments that might get in the way of using the application. The range of illnesses and disabilities a person might have can be very large and the group must take this into consideration to accommodate them. An older person will probably have a harder time reading due to their eyesight worsening as they age so the application would need to use larger fonts that is easily readable. Colour blindness is also relatively common and should be acknowledged before designing the UI. If a person has a hearing impairment, descriptions of what an image or an object looks like, if we add any, should be available for screen readers throughout the application. 

If a user is unable to use a computer due to physical disabilities, the group must ensure that the application can be used easily by another person. The patient might have a carer that looks after them so the application should be accessible even if the patient is directing a third party to use it.

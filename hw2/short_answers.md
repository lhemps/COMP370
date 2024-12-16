Q1: Give four reasons why a cloud machine is better than a laptop for data science and work at scale.
    1. Storage capacity- cloud machine has way more storage space than a regular laptop
    2. Processing power- cloud machine has way more processing power than a regular laptop
    3. Collaboration with others- many people can access the database from different machines and work simultaneously 
    4. Security- if someone steals your laptop they have access to your work and there's nothing you can do about it without
       physically getting the laptop back, if you use a cloud machine you can access the server from another machine and change
       the permissions

Q2: List out the stages in the data science process and define each.
    1. Question Definition: clearly lay out the question you are working to investigate, and what a useful answer to said question
       would look like
    2. Data collection: collect the data necessary to thouroughly investigate your question
    3. Data annotation: label and compute necessary attributes of your collected data
    4. Data analysis: use existing methods, make statistical models and visualizations of your data
    5. Interpretation: look at the analysis of your data and see how it answers your question and what conclusions can be drawn
    6. Communication: convey the answer to your question to shareholders, probably in a narrative form, in a way that is understandable
       to lay people, without misrepresenting the data.

Q3: What is the difference between data analytics and data science?
    Data analytics is mainly concerned with using existing methods of statistical analysis on existing types of data, while data science has to have an element of innovation or exploration in the type of data used, the type of methods used to analyze that data, or in the actual question being asked. eg. Using youtube views to A/B test thumbnails would be data analytics, as this is using existing data types with existing methods. Collecting the comments of a video and analysing the emojis used to estimate the age of the average channel viewer would be data science, because as far as I know no one has ever used comment section emojis in this way before, so the researchers would have to figure out a lot of new methods in the process.

Q4: Give an example of how a loop can occur in the data science process.
    Suppose you are investigating the question "Why is there a housing crisis in this area?". You collect data on the number of residences in an area and the number of people wanting to live in that area. In your data analysis it seems like there are actually more houses than people which doesn't make sense as it contradicts the premise of the question. You then go back to the data collection step and collect more data on who owns the properties and how many are currently occupied. After analyzing the new data, in the interpretation stage you see that many of the registered owners names sound like company names not people names, so you go back to the annotation step and add an attribute specifying which residences are owned by a corporate landlord. This raises new avenues to look into, like comparing the cost, rate of overturn, demographic, etc. of corporate vs non-corporate owned residences, or how any of these factors have changed over time. This broadens the scope of investigation significantly, and will require movement back and forth between stages in order to answer the question in a meaningful way.
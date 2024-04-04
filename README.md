Abstract
Food analysis is a prerequisite for ascertaining product quality,
implementing regulatory enforcements, checking compliance with national
and international food standards, contracting specifications and nutrient
labeling requirements. One third of all food produced is lost or wasted –
around 1.3 billion tonnes of food –costing the global economy close to $940
billion each year. If one quarter of the food currently lost or wasted could be
saved, it would be enough to feed 870 million hungry people. In this project,
we will be using Machine Learning Algorithms to predict the number of
orders a restaurant should produce given certain variables to minimise the
food wastage.
7
1) Introduction:
1.1 Overview:
Food is central to human well-being: it provides the body with
nourishment, offers livelihoods that lift people out of poverty, and
brings communities together. Although food is a basic human need,
too many people are trapped in a cycle of hunger by forces beyond
their immediate control, like poverty, disaster, conflict and
inequality.
Despite decades of progress in reducing world hunger, 2017 saw
increases in the number of people who are hungry. More than 820
million people still go to bed hungry every night — that’s one in
every nine people who don’t have the food they need to live a
healthy, productive life.
The World Health Organization considers this to be the single
greatest threat to global health. Hunger is cyclical and generational:
it inhibits people’s ability to work and learn to their fullest
potential, which can curb their future and trap them and their
families in more poverty — and more hunger.
People in poverty generally spend between 60 and 80 percent of
their income on food, which can force them to prioritize feeding
their families over meeting other basic needs or reaching long-term
goals, like sending their children to school. If an emergency strikes,
they may need to skip meals in order to cope financially — and the
cycle of hunger continues.
According to the Food Security Information Network, conflict and
insecurity were primary drivers of food insecurity in 2017, alone
accountable for putting 74 million people in need of urgent
assistance. Climate change is also eroding existing efforts to
improve food security.
8
1.2 Purpose:.
Recent years, the ML methods have become popular as they allow
researchers to improve prediction accuracy and used in many
applications.
In this study, regression algorithms are used to predict various food
material requirement. Based on this predictions farmers and
producers can produce them to meet the requirement. Here ML
regression methods are used for prediction. The study aimed to
determine the most successful regression methods by comparing
the logistic regression, decision tree (DT), random forest (RF),
linear regression, multiple regression, support vector regression,
Naïve Bayes.
9
2) Literature Survey:
2.1 Existing Problem:
Our world population is expected to grow from 7.3 billion today to
9.7 billion by 2050. Finding solutions for feeding the growing
world population has become a hot topic for food and agriculture
organizations, entrepreneurs and philanthropists. These solutions
range from changing the way we grow our food to changing the
way we eat. To make things harder, the world's climate is
agriculture. Hence, it is necessary that we analyze the food
production and act faster rather than repenting later.
2.2 Proposed Solution :
Using a machine learning model, we can predict the number of
orders on a food item per day for any kind of cuisine located in
various regions and cities which is directly proportional to the food
required. We can take various inputs as a base price, region code,
city code, food item id, type of cuisine etc to the algorithm. We then
use regression algorithms to predict which food item gets how
many orders. A food item is considered to be most interesting
when the number of orders has more than 500 per day. The model
will be trained based on the algorithm features which will give the
higher accuracy. Finally, it will be integrated into a web based
application. The final system allows the user to give the details
required as input and the system will display the output number of
orders.
10
3) Theoretical Analysis
3.1 Hardware / Software designing:
The software used to implement this project is mainly Jupyter Notebook
and Spyder. The other programming skills required are Python, Flask,
HTML and CSS. The project works in 2 parts. The first part is building
the model and the other part is building the frontend. The model building
is done by using Machine Learning libraries by the help of Python. The
frontend development is done by using HTML and the designs are added
by using CSS. Both the frontend and backend are connected by using
Flask. The Flask generates localhost for the application to run.
11
3.2 Block Diagram
Food requirement analysis
Data Collection
Data Preprocessing
Import libraries
Import data set
Data Visualization
Handling null
values Label
Encoding
OneHot Encoding
Feature Scaling
Splitting data
Model Building
Application Building
Create html file
Build python code
12
3.3 Flowchart:
13
4.METHODOLOGY:
4.1 DataPreprocessing
Data Merging
● Data merging is the process of combining two or more data sets into a
single data set. Most often, this process is necessary when you have raw
data stored in multiple files, worksheets, or data tables, that you want to
analyze all in one go.
● We have three datasets. We merge them to form a single dataset.
14
Data Cleaning
● Data cleaning is one of the important parts of machine learning. It plays
a significant part in building a model. Data Cleaning is one of those
things that everyone does but no one really talks about. It surely isn’t the
fanciest part of machine learning and at the same time, there aren’t any
hidden tricks or secrets to uncover. However, proper data cleaning can
make or break your project. Professional data scientists usually spend a
very large portion of their time on this step.
● Before we go for modeling the data, we have to check whether the data is
cleaned or not. And after cleaning, we have to structure the Data. For the
cleaning part, First I have to check whether there exists any missing
values. For that I am using the code snippet isnull()
There are no missing values in our dataset. So we continued with other
operations.
15
4.2 LABEL ENCODING:
Label Encoding refers to converting the labels into numeric form so as to
convert it into the machine-readable form. Machine learning algorithms can
then decide in a better way on how those labels must be operated. It is an
important preprocessing step for the structured dataset in supervised learning.
16
4.3 ONE HOT ENCODING:
A one hot encoding allows the representation of categorical data to be more
expressive. Many machine learning algorithms cannot work with categorical
data directly. The categories must be converted into numbers.
17
4.4 MODELLING
IMPORTANT PYTHON LIBRARIES
● Numpy
● Pandas
● Scikit Learn
In modelling the data is fed into machine learning algorithms.
So we split the data into two parts training and testing.
The training data is used to train the algorithm and testing data is used to test
the model .
Generally the model having the highest accuracy is chosen as the good model.
The problem here we are dealing comes under the classification as we have to
predict whether the applicant can get loan sanctioned or not?
There are many algorithms for Regression in the scikit learn library. The
algorithms here we are going to use are

# Comp3_Final_Project
All Files for Comp Methods 3 Final Project

Welcome to our Final Project for Computational Methods 3. We sought to find the optimal spending percentages of the salary cap a team will need to pay each position to maximize their probability of entering the playoffs, winning a conference championship game, or winning the Super Bowl. We choose to look at each as an independent event, i.e. if you made it to the Super Bowl, what is the probability of winning. Future research can look at making them dependent events. 

For the files provided, the SQL and football_data.ipynb have tutorials included as markdowns. Our py files have comments indicating what our code is doing as comments, this includes our RidgeRegression.ipynb file. Finally, we have included an HTML file rendered from RStudio that walks you through the how build out an ensemble model for determining which predictors are relevant to the events above. 

Last but not least, we have included a py file that runs our streamlit app that allows you to be an acting general manager. You will get to assign how much you pay a team and will then be given a probability of success for the three events. 

Before we get to the instructions on running the streamlit py file, the order provided below will allow you recreate what we did for the project:

1) run the football_data.ipynb to obtain the data
2) run the RidgeRegression.ipynb and the code within the HTML file to determine the predictor coefficients
3) run finalcalc.py file which has the prebuilt coefficients within the file. You will need to provide the following arguments: event(superbowl, ccwins, playoffs) & number of simulations(your choose) in the terminal. Do not include the & when running the code from the command. You will receive an error should you include & or fail to add in one of the arguments. 
4) Then use the SQL.ipynb file to use SQL tables get the averages needed in our steamlit file. 

Should you choose not replicate what was done in this project, you are able to download the streamlit py file and run it directly. 

### Dashboard Functionality ###

In order to run the NFL GM Dashboard on your system:
   1. Download the "NFL_GM_Dashboard.py" file in the Git Repository
   2. Put the .py file into desired directory.
   3. Ensure the following are installed on your computer:
	a. Python (version 3.7 or higher)
	b. Pip (python's package manager)
	
	To check if these are installed on your computer, run the following commands in your Interactive Design Environment:
	"python --version"
	"pip --version"

   4. Install the required libraries by running the following in your terminal:
	"pip install streamlit numpy matplotlib openai"

   5. Run the Dashboard! At this point, you can run the Dashboard. Open up a new terminal and navigate to the directory where the "NFL_GM_Dashboard.py" is stored.

   6. In the terminal run the command: "python -m streamlit run .\NFL_GM_Dashboard.py"

   This should open the dashboard!

### Using the Dashboard ###

This dashboard allows you to set a salary for the given positions. Some position groups (such as Offensive Line or Defensive Line) are a collection of several positions. For ease of use, this Dashboard combines those positions into an overall position group. Input should be in millions of dollars. For example, an input of 4.5 would mean $4,500,000. The league low, high and average for each position group (for the 2024) season are listed below as reference.

Once all salaries are determined, click "Get Probability of Success!" to see the probability of your roster Winning the Super Bowl, Winning the Conference Championship or making the playoffs.

### CHAT GPT FUNCTIONALITY ###

   To integrate the "Generate Season Narrative" function enabled by ChatGPT:

   1. Navigate to https://platform.openai.com/settings/organization/api-keys
   
   2. Create a new API_key. OF NOTE: you must sign up and deposit money into you API Account (https://platform.openai.com/settings/organization/billing/overview)  to get access to multiple API calls, which is necessary for this part of the Dashboard's functionality. If you choose not to do this step, you will quickly run out of free API calls.

   3. Copy and paste your API Key into line 333 of the Dashboard.

   OPTIONAL: Adjust the ChatGPT Query.

   The current query that gets sent to chatGPT that generates the season narrative integrates the probability of winning the Superbowl from the previous code and asks ChatGPT to create a season narrative based on it. It also asks ChatGPT for a critical play that defines their season, and requests that it mention the downfall of the Dallas Cowboys.

   The current query reads:

"In 150 words or less, write a narrative about an NFL team of your choosing that has a {superbowl_probability*100:.1f} chance of winning the Super Bowl. Make sure you include one dramatic play that defines their season, whether it is good or bad. Also, talk about the Dallas Cowboys and make sure they have a bad season with a funny reason why; include a bit of violence. Change the team that the narrative talks about each time, and make them different for each response."

   The query starts at line 353. You may adjust to query to suit your personal needs.

# Import Statements
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import openai

# Cutsom CSS Styles 
st.markdown("""
    <style>
        .body {
            background-color: #4682B4; /* Blue background color */
            }
        .title {
            text-align: center;
            font-size: 37px;
            font-weight: bold;}
        .sub_title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            text-decoration: underline;}
        .info {
            text-align: left;
            font-size: 16px;
            font-weight: normal;
            line-height: normal;
            margin-bottom: 40px;}
        .salary_cap {
            text-align: center;
            font-size: 20px;
            font-weight: bold;}
        .small {
            font-size: 12px;
            }
        .centered_button {
            display: flex;
            justify-content: center;
            align-items: center;}
    </style>
""", unsafe_allow_html=True)


# Dashboard Title (using CSS STYLE: Dashboard Title)
st.markdown("<div class='title'>Virtual NFL General Manager</div>", unsafe_allow_html=True)
st.markdown("") # For spacing
st.markdown("") # For spacing

# Welcome Text
welcome_txt = "Welcome to the Virtual NFL General Manager Dashboard! In this dashboard you can decide how much you are willing to spend on each position, and then generate success probabilities for the roster you have created."

# Display Welcome Text (CSS STYLE: Information)
st.markdown(f"<div class='info'>{welcome_txt}</div>", unsafe_allow_html=True)

# Display Salary Cap
salary_cap = 255.40 # Manual input for the current year's salary cap, used later as well
st.markdown(f"<div class='salary_cap'>2024 NFL Salary Cap: ${salary_cap} Million</div>", unsafe_allow_html=True)
st.markdown("") # For spacing

############################# WIDGETS #############################
############################# Widgets to Input Offensive Salary #############################

st.markdown("<div class='sub_title'>Offense</div>", unsafe_allow_html=True)  # Section Title
column1, column2, column3 = st.columns(3)                                    # Break up into columns

with column1:
    QB_value = column1.text_input("**ENTER QUARTERBACK SALARY**", 0)
    # Display the minimum, average and maximum values for X
    st.markdown("""
    <div class="small">
    <b><u>QB Salary Range</u></b><br>
    - <b>League Low:</b> $3.37M <br>
    - <b>League Average:</b> $20.99M <br>
    - <b>League High:</b> $53.77M <br><br>
    </div>
    """, unsafe_allow_html=True)

    TE_value = column1.text_input("**ENTER TIGHT END SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>TE Salary Range</u></b><br>
    - <b>League Low:</b> $2.89M <br>
    - <b>League Average:</b> $9.63M <br>
    - <b>League High:</b> $22.24M <br><br>
    </div>
    """, unsafe_allow_html=True)

with column2:
    RB_value = column2.text_input("**ENTER RUNNING BACK SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>RB Salary Range</u></b><br>
    - <b>League Low:</b> $2.96M <br>
    - <b>League Average:</b> $7.42M <br>
    - <b>League High:</b> $21.24M <br><br>
    </div>
    """, unsafe_allow_html=True)

    OL_value = column2.text_input("**ENTER OFFENSIVE LINE SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>OL Salary Range</u></b><br>
    - <b>League Low:</b> $17.59M <br>
    - <b>League Average:</b> $33.93M <br>
    - <b>League High:</b> $63.16M <br><br>
    </div>
    """, unsafe_allow_html=True)
    
with column3:
    WR_value = column3.text_input("**ENTER WIDE RECEIVER SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>WR Salary Range</u></b><br>
    - <b>League Low:</b> $5.26M <br>
    - <b>League Average:</b> $17.09M <br>
    - <b>League High:</b> $41.06M <br><br>
    </div>
    """, unsafe_allow_html=True)

############################# Widgets to Input Defensive Salary #############################

st.markdown("<div class='sub_title'>Defense</div>", unsafe_allow_html=True)

# Break up into columns
column1, column2, column3 = st.columns(3)

with column1:
    DL_value = column1.text_input("**ENTER DEFENSIVE LINE SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>DL Salary Range</u></b><br>
    - <b>League Low:</b> $7.76M <br>
    - <b>League Average:</b> $28.46M <br>
    - <b>League High:</b> $66.30M <br><br>
    </div>
    """, unsafe_allow_html=True)
    
with column2:
    LB_value = column2.text_input("**ENTER LINEBACKER SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>LB Salary Range</u></b><br>
    - <b>League Low:</b> $6.47M <br>
    - <b>League Average:</b> $21.68M <br>
    - <b>League High:</b> $62.96M <br><br>
    </div>
    """, unsafe_allow_html=True)

with column3:
    SEC_value = column3.text_input("**ENTER SECONDARY SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>Secondary Salary Range</u></b><br>
    - <b>League Low:</b> $15.98m <br>
    - <b>League Average:</b> $29.70M <br>
    - <b>League High:</b> $58.37M <br><br>
    </div>
    """, unsafe_allow_html=True)

############################# Widgets to Input Special Teams Salary #############################
st.markdown("<div class='sub_title'>Special Teams</div>", unsafe_allow_html=True)
column1, column2, column3 = st.columns(3)

with column1:
    K_value = column1.text_input("**ENTER KICKER SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>K Salary Range</u></b><br>
    - <b>League Low:</b> $0.61M <br>
    - <b>League Average:</b> $2.89M <br>
    - <b>League High:</b> $5.92M <br><br>
    </div>
    """, unsafe_allow_html=True)
    
with column2:
    P_value = column2.text_input("**ENTER PUNTER SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>P Salary Range</u></b><br>
    - <b>League Low:</b> $0.60M <br>
    - <b>League Average:</b> $2.03M <br>
    - <b>League High:</b> $3.98M <br><br>
    </div>
    """, unsafe_allow_html=True)

with column3:
    LS_value = column3.text_input("**ENTER LONG SNAPPER SALARY**", 0)
    st.markdown("""
    <div class="small">
    <b><u>LS Salary Range</u></b><br>
    - <b>League Low:</b> $0.57M <br>
    - <b>League Average:</b> $1.16M <br>
    - <b>League High:</b> $1.55M <br><br>
    </div>
    """, unsafe_allow_html=True)
    
############################# End of the Widgets Sections #############################
############################# Salary Cap Checking Section #############################
try:
    QB_salary = float(QB_value)
    TE_salary = float(TE_value)
    RB_salary = float(RB_value)
    OL_salary = float(OL_value)
    WR_salary = float(WR_value)
    DL_salary = float(DL_value)
    LB_salary = float(LB_value)
    SEC_salary = float(SEC_value)
    K_salary = float(K_value)
    P_salary = float(P_value)
    LS_salary = float(LS_value)
except ValueError:
    st.error("Please enter valid numeric values for all salary inputs.")
    QB_salary = TE_salary = RB_salary = OL_salary = WR_salary = DL_salary = LB_salary = SEC_salary = K_salary = P_salary = LS_salary = 0

# Calculate total salary input and remaining cap space
total_salary = QB_salary + TE_salary + RB_salary + OL_salary + WR_salary + DL_salary + LB_salary + SEC_salary + K_salary + P_salary + LS_salary
remaining_cap_space = salary_cap - total_salary

# Display the total salary and remaining cap space

# Break up into columns
column1, column2 = st.columns(2)

with column1:
    st.markdown(f"#### Total Salary:\n #### ${total_salary:.2f} Million")

with column2:
    st.markdown(f"#### Remaining Cap Space:\n #### ${remaining_cap_space:.2f} Million")

# Display an error message if the total salary exceeds the cap
if total_salary > salary_cap:
    st.error("Error: Total salary exceeds the salary cap!")


############################# Data Analysis Formula #############################

# Define Mean and Standard Deviation for Each Scenario

means_sb = {"QB": 0.13024158127252583, "TE": 0.12702407030355536, "DL": 0.11958639693815622,
    "P": 0.10361200034616726, "OL": 0.10107342640188728, "LB": 0.08405611633741628,
    "WR": 0.08343930893186806, "SEC": 0.07529585944410092, "K": 0.06026363173530399,
    "LS": 0.05864312898953742, "RB": 0.05676447929948134}
sds_sb = { "QB": 0.04336172191052706, "TE": 0.04452312121059261, "DL": 0.04676690322955546,
    "P": 0.049356419723869185, "OL": 0.049461568681967376, "LB": 0.04795705265039734,
    "WR": 0.047829768989051155, "SEC": 0.045671211949084474, "K": 0.03899087431154402,
    "LS": 0.038020551347684804, "RB": 0.036947985166913846}

means_cc = {"DL": 0.14667127958217377, "TE": 0.11206614263335382, "K": 0.1103356061834117,
    "QB": 0.10662231165499735, "SEC": 0.09524262447087296, "OL": 0.09449882315160152,
    "P": 0.0820284165938657, "WR": 0.0696083150716234, "LS": 0.06210262724378655,
    "RB": 0.060378659364026616, "LB": 0.06044519405028646}
sds_cc = {"DL": 0.03536766596916879, "TE": 0.04834366086082, "K": 0.048604396977552,
    "QB": 0.04911553930418163, "SEC": 0.049455523517796626, "OL": 0.04945488876420557,
    "P": 0.04773678876063367, "WR": 0.04380502706256277, "LS": 0.040248464721236325,
    "RB": 0.03933908336684582, "LB": 0.039354020308348246}

means_po = {"LB": 0.1262722284477314, "QB": 0.1253398835529392, "DL": 0.11963177842725703,
    "SEC": 0.10982916167507122, "WR": 0.10178706625488919, "OL": 0.0914112811429917,
    "K": 0.08137721823608954, "RB": 0.06728177836427726, "LS": 0.0600240110792441,
    "TE": 0.05854090591994142, "P": 0.058504686899567955}
sds_po = {"LB": 0.044889389626874304, "QB": 0.04524769458798916, "DL": 0.04692054351047184,
    "SEC": 0.048887885047520584, "WR": 0.049485948027946015, "OL": 0.049134228233623255,
    "K": 0.0473833822479805, "RB": 0.042425462977998485, "LS": 0.038795637898694973,
    "TE": 0.03793812681856334, "P": 0.03796750901385969}

def calculate_probabilities(qb, te, rb, ol, wr, dl, lb, sec, k, p, ls, 
                            means_sb, sds_sb, means_cc, sds_cc, means_po, sds_po, salary_cap):

    # Weights Determined by Previous Data Analysis
    weights_superbowl = {
        "QB": 0.459, "TE": 0.439, "DL": 0.394, "P": 0.298, 
        "OL": 0.282, "LB": 0.178, "WR": 0.174, "SEC": 0.123, 
        "K": 0.025, "LS": 0.013, "RB": max(-0.018, 0)
    }
    weights_ccwins = {
        "DL": 0.618, "TE": 0.386, "K": 0.375, "QB": 0.351, 
        "SEC": 0.278, "OL": 0.273, "P": 0.191, "WR": 0.107, 
        "LS": 0.055, "RB": 0.043, "LB": 0.043
    }
    weights_playoffs = {
        "LB": 0.862, "QB": 0.849, "DL": 0.779, "SEC": 0.659, 
        "WR": 0.559, "OL": 0.430, "K": 0.304, "RB": 0.121, 
        "LS": 0.021, "TE": max(-0.031, 0), "P": max(-0.166, 0)
    }

    #user input
    input_values = {"QB": qb, "TE": te, "RB": rb, "OL": ol,
        "WR": wr, "DL": dl, "LB": lb, "SEC": sec,
        "K": k, "P": p, "LS": ls}

    #normalize the input per the given salary cap
    normalized_values = {position: value / salary_cap for position, value in input_values.items()}

    #penalize any deviations from the mean and calculate the probability of success
    def calculate_success_probability(values, weights, means, sds):
        success_score = 0
        for position, value in values.items():
            weight = weights.get(position, 0)
            mean = means.get(position, 0)
            sd = sds.get(position, 1) 
            deviation_penalty = np.exp(-np.abs(value - mean) / (sd if sd != 0 else 1))
            success_score += value * max(weight, 0) * deviation_penalty  # Apply penalty
        
        #apply log tranformation to get probability and make them more realistic
        probability = 1 / (1 + np.exp(-success_score))
        return probability
        
    superbowl_probability = calculate_success_probability(normalized_values, weights_superbowl, means_sb, sds_sb)
    ccwin_probability = calculate_success_probability(normalized_values, weights_ccwins, means_cc, sds_cc)
    playoff_probability = calculate_success_probability(normalized_values, weights_playoffs, means_po, sds_po)

    return superbowl_probability, ccwin_probability, playoff_probability

############################# Call Probability Formula #############################

superbowl_probability, ccwin_probability, playoff_probability = calculate_probabilities(QB_salary, TE_salary, RB_salary, OL_salary, WR_salary, 
    DL_salary, LB_salary, SEC_salary,
    K_salary, P_salary, LS_salary, 
    means_sb, sds_sb, means_cc, sds_cc, means_po, sds_po,
    salary_cap)

# Implement Button
st.markdown("") # For spacing
st.markdown("") # For spacing

if st.button("Get Probabilities of Success"):
    st.markdown(f'**Winning Superbowl:** {superbowl_probability*100:.1f}%')
    st.markdown(f'**Winning Conference Championship:** {ccwin_probability*100:.1f}%')
    st.markdown(f'**Making Playoffs:** {playoff_probability*100:.1f}%')

############################# ChatGPT Integration #############################

# OpenAI API key
openai.api_key = "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"

# Function to call ChatGPT API
def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" if needed
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250,  # Adjust the response length
            temperature=0.7  # Adjust the creativity level
        )
        # Extract and return the response
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Season Narrative")

# Pre-defined query
query = (
    f"In 150 words or less, write a narrative about an NFL team of your choosing "
    f"that has a {superbowl_probability*100:.1f} chance of winning the Super Bowl. Make sure you include one dramatic play "
    f"that defines their season, whether it is good or bad. Also, talk about the Dallas Cowboys "
    f"and make sure they have a bad season with a funny reason why; include a bit of violence."
    f"Change the team that the narrative talks about each time, and make them different for each response."
)

# Button to trigger API call
if st.button("Generate Season Narrative"):
    with st.spinner("Contacting ChatGPT..."):
        # Call the API with the pre-defined query
        response = get_chatgpt_response(query)
    # Display the response
    st.subheader("ChatGPT Response:")
    st.write(response)

#To Do Items:\n
#-Add chatgpt tie in (if possible)\n
#-Add background picture\n

#-Instructions: "pip Install openai"
#-Instruction: Plug into Terminal at appropriate address: python -m streamlit run .\NFL_GM_Dashboard.py
#-LOW PRIORITY:
#-CSS Styling (Borders, hover effects)

#Always import the necessary libraries needed to run the code.
#Certain print statements are commented out to avoid cluttering the output.
import random
import numpy as np
import math
import sys
import json
from datetime import datetime
import matplotlib.pyplot as plt
import time

#Our first function generates random spending percentages for each position based on the number of positions and a minimum spending value.
#the minimum spending value is set to 0.01 by default otherwise it can be set to 0 which is not a realistic value. 
#We then scale the values to ensure that the sum of the spending percentages is equal to 1.
def generate_random_spending(num_positions, min_spending=0.01):
    remaining_spending = 1 - num_positions * min_spending
    random_values = np.random.rand(num_positions)
    scaled_values = random_values / sum(random_values) * remaining_spending
    spending_percentages = [min_spending + value for value in scaled_values]
    return spending_percentages

#to determine our success probability, we calculate the success score by multiplying the spending percentage for each position by the weight for that position.
#We then apply a logistic function to transform the success score to a probability between 0 and 1.
#the logistic function works since we have a binary outcome (success or failure) and the success score can take any real value.
def calculate_success_probability(spending_percentages, weights):
    success_score = 0
    for position, weight in weights.items():
        success_score += spending_percentages[position] * max(weight, 0)
    
    success_probability = 1 / (1 + np.exp(-success_score))
    return success_probability

#Our main function runs the football simulation for a given set of weights, number of simulations, and minimum spending value.
#This function uses the generate_random_spending and calculate_success_probability functions to run the simulations.
#We then store the spending percentages and predicted probabilities for each simulation in a list of dictionaries.
def run_football_simulation(weights, num_simulations, min_spending=0.01):
    results = []
    for _ in range(num_simulations):
        spending_percentages_values = generate_random_spending(len(weights), min_spending)
        spending_percentages = dict(zip(weights.keys(), spending_percentages_values))

        predicted_probability = calculate_success_probability(spending_percentages, weights)

        results.append({'spending_percentages': spending_percentages,
            'predicted_probability': predicted_probability})
    return results

#We use the main function to allow for different probability types (superbowl, ccwins, playoffs) and number of simulations to be passed as command-line arguments.
if __name__ == "__main__":
    start_time = time.time()
    #We check if the correct number of command-line arguments are provided.
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <probability_type> <num_simulations>")
        sys.exit(1)
    #We then assign the probability type and number of simulations to variables.
    probability_type = sys.argv[1].lower()
    num_simulations = int(sys.argv[2])
    #here we define the weights for each position based on the probability type.
    weights_superbowl = { "QB": 0.459, "TE": 0.439, "DL": 0.394, "P": 0.298, 
        "OL": 0.282, "LB": 0.178, "WR": 0.174, "SEC": 0.123, 
        "K": 0.025, "LS": 0.013, "RB": max(-0.018, 0)}
    weights_ccwins = {"DL": 0.618, "TE": 0.386, "K": 0.375, "QB": 0.351, 
        "SEC": 0.278, "OL": 0.273, "P": 0.191, "WR": 0.107, 
        "LS": 0.055, "RB": 0.043, "LB": 0.043}
    weights_playoffs = {"LB": 0.862, "QB": 0.849, "DL": 0.779, "SEC": 0.659, 
        "WR": 0.559, "OL": 0.430, "K": 0.304, "RB": 0.121, 
        "LS": 0.021, "TE": max(-0.031, 0), "P": max(-0.166, 0)}
    #We then assign the appropriate weights based on the probability type.
    if probability_type == 'superbowl':
        weights = weights_superbowl
    elif probability_type == 'ccwins':
        weights = weights_ccwins
    elif probability_type == 'playoffs':
        weights = weights_playoffs
    else:
        #provide an error message if the probability type is not valid.
        print("Invalid probability type. Choose 'superbowl', 'ccwins', or 'playoffs'.")
        sys.exit(1)

    #We then run the simulations
    results = run_football_simulation(weights, num_simulations)

    #Sunce we chose to look for the top 10% of results, we calculate the threshold for the top 10% of predicted probabilities.
    #We then filter the results to only include those with predicted probabilities above the threshold.
    probabilities = [result['predicted_probability'] for result in results]
    threshold = np.percentile(probabilities, 90)  # Top 10%
    top_results = [result for result in results if result['predicted_probability'] >= threshold]
    min_probability = min([result['predicted_probability'] for result in top_results])
    max_probability = max([result['predicted_probability'] for result in top_results])
    #count_top_results = len(top_results)

    #Print statements for debugging
    #print(f"Threshold (90th percentile): {threshold:.5f}")
    #print(f"Minimum Predicted Probability in Top Results: {min_probability:.5f}")
    #print(f"Maximum Predicted Probability in Top Results: {max_probability:.5f}")
    #print(f"Number of Top Results: {count_top_results}")


    #We then calculate the mean and standard deviation of spending percentages for top results
    all_spending = {pos: [] for pos in weights.keys()}
    for result in top_results:
        for pos, value in result['spending_percentages'].items():
            all_spending[pos].append(value)

    #Finally, we calculate the mean and standard deviation of spending percentages for each position.
    mean_spending = {pos: np.mean(values) for pos, values in all_spending.items()}
    std_spending = {pos: np.std(values) for pos, values in all_spending.items()}

    #Print statements for debugging
    #print(f"Running simulations for {probability_type} probability...")
    #print(f"Number of simulations: {num_simulations}")
    #print("Mean Spending Percentages for Top Results:")
    #print(mean_spending)
    #print("\nStandard Deviation of Spending Percentages for Top Results:")
    #print(std_spending)
    
    #We then calculate the elapsed time for the simulation
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    #We create list to store our ratio values from the top results and the filtered probabilities.
    qb_rb_ratios = []
    qb_ol_ratios = []
    ol_dl_ratios = []
    qb_te_ratios = []  
    filtered_probabilities = []

    #We then iterate over the top results to calculate the ratios and store the filtered probabilities.
    for result in top_results:
        spending = result['spending_percentages']
        #We then need to avoid division by zero by checking if all required values are greater than 0
        if spending['RB'] > 0 and spending['OL'] > 0 and spending['DL'] > 0 and spending['TE'] > 0:
            qb_rb_ratios.append(spending['QB'] / spending['RB'])
            qb_ol_ratios.append(spending['QB'] / spending['OL'])
            ol_dl_ratios.append(spending['OL'] / spending['DL'])
            qb_te_ratios.append(spending['QB'] / spending['TE']) 
            filtered_probabilities.append(result['predicted_probability'])


    #Finaly, we plot the histograms for the ratios and the filtered probabilities.
    plt.figure(figsize=(30, 5))

    #Histogram for QB/RB Ratio
    plt.subplot(1, 5, 1)
    plt.hist(qb_rb_ratios, bins=30, color='blue', alpha=0.7, edgecolor='black')
    plt.title('Histogram of QB/RB Ratio')
    plt.xlabel('QB/RB Ratio')
    plt.ylabel('Frequency')
    plt.grid(True)

    #Histogram for QB/OL Ratio
    plt.subplot(1, 5, 2)
    plt.hist(qb_ol_ratios, bins=30, color='green', alpha=0.7, edgecolor='black')
    plt.title('Histogram of QB/OL Ratio')
    plt.xlabel('QB/OL Ratio')
    plt.ylabel('Frequency')
    plt.grid(True)

    #Histogram for OL/DL Ratio
    plt.subplot(1, 5, 3)
    plt.hist(ol_dl_ratios, bins=30, color='red', alpha=0.7, edgecolor='black')
    plt.title('Histogram of OL/DL Ratio')
    plt.xlabel('OL/DL Ratio')
    plt.ylabel('Frequency')
    plt.grid(True)

    #Histogram for QB/TE Ratio
    plt.subplot(1, 5, 4)
    plt.hist(qb_te_ratios, bins=30, color='purple', alpha=0.7, edgecolor='black')
    plt.title('Histogram of QB/TE Ratio')
    plt.xlabel('QB/TE Ratio')
    plt.ylabel('Frequency')
    plt.grid(True)

    #Histogram for All Predicted Probabilities
    plt.subplot(1, 5, 5)
    plt.hist(probabilities, bins=30, color='teal', alpha=0.7, edgecolor='black')
    plt.title('Histogram of Predicted Probabilities')
    plt.xlabel('Predicted Probability')
    plt.ylabel('Frequency')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('combined_ratio_and_probability_histograms.png')
    print("Histogram saved to 'combined_ratio_and_probability_histograms.png'")
    plt.show()

    #We then save the results to a JSON file. Include the full path to the file to avoid any issues with the file path.
    #Included here was the file path for HPC for use there. 
    #output_file = f"~/SL/final_project/{probability_type}.json"
    output_file = f"/Users/andrewtamez/Desktop/NPS/OA3802_Comp3/Final_Project/{probability_type}.json"

    #Finally, we write results to the specified file and print a message indicating where the results were saved
    #or an error message if there was an issue saving the results.
    try:
        with open(output_file, 'w') as f:
            json.dump(top_results, f, indent=4)

        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving results to {output_file}: {e}")

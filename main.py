import os
import game_data
import art_higher_lower
import random

def calculate(total_f1,total_f2):
  if total_f1 > total_f2:
    return figure_1
  else:
    return figure_2

def get_figure():
  random_figure = random.choice(game_data.data)
  return random_figure

figure_1 = get_figure()
figure_2 = get_figure()
score = 0
in_game = True

print(art_higher_lower.logo)

while in_game == True:
  
  # print(figure_1['follower_count'])
  # print(figure_2['follower_count'])
  
  print(f"Compare A: {figure_1['name']}, a {figure_1['description']}, from {figure_1['country']}.")
  print(art_higher_lower.vs)
  print(f"Against B: {figure_2['name']}, a {figure_2['description']}, from {figure_2['country']}.")
  decission = input("Who has more followers? Type 'A' or 'B': ").lower()
  os.system('cls')
  
  if  decission == "a" and calculate(figure_1['follower_count'],figure_2['follower_count']) == figure_1:
    score += 1
    figure_1 = figure_2
    figure_2 = get_figure()
    print(art_higher_lower.logo)
    print(f"You're right! Current score: {score}.")
  elif decission  == "b" and calculate(figure_1['follower_count'],figure_2['follower_count']) == figure_2:
    score +=1
    figure_1 = figure_2
    figure_2 = get_figure()
    print(art_higher_lower.logo)
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    in_game = False
  
  
  
  




  # print(f"Compare A: {random_figure1['name']}, a {random_figure1['description']}, from {random_figure1['country']}.")
  # print(f"Compare B: {random_figure2['name']}, a {random_figure2['description']}, from {random_figure2['country']}.")
  # if calculate(random_figure1['follower_count'],random_figure2['follower_count']) == 0:
    
    
    # print(f"Compare A: {random_figure1['name']}, a {random_figure1['description']}, from {random_figure1['country']}.")
    
  
  # print(random_figure1['follower_count'] , random_figure1['follower_count'])
    
    
    

  # print(random_figure1)
# user_input = input("Who has more followers? Type 'A' or 'B':").lower()
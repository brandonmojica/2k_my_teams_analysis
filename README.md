# 2k_my_teams_analysis

<h2>NBA 2k20 My Teams</h2>
This project is aimed at determining if cards from a certain universtity are faster than the rest of the cards (Players). This test I expored weather on average do players that come from Duke University are faster than than the rest of the players/cards. I chose this project because of interest in basketball and NBA 2k20. I spend a obscene amount of time playing this game, and I wanted to see if there was some basic stats I could try and leverage.I found the data of all the cards on the website: https://2kmtcentral.com/.

<h2>During my EDA</h2>
There are 1166 players/cards in my data set that each have 47 attributes. 


I found that my data was not clean. There were a few columns that had data that was meant to be in sperate columns but was combined into a single string. 

![df_1](https://github.com/brandonmojica/2k_my_teams_analysis/blob/master/images/df_not_clean.png)

## Statistical Test:
1. Null Hypothesis: The sample means of Duke players Speed are the same as the rest of the players/cards.
2. Alternative Hypothesis: The sample means of Duke players and the rest of the cards are not the same.
3. The statistical test I will use is a T-test to compare the samples. 
4. Signiificance Level = 0.05


## Results
I ran a T-test on two samples of data; 

      filter1 = myteam_player_data["School"]=="Duke"
      df_school = myteam_player_data.where(filter1)
      duke_player_cards = df_school.dropna()
      #Create an arr for t-test
      duke_players_arr = duke_player_cards['Speed'].tolist()
      #get all of the non duke players
      players_not_duke = myteam_player_data[myteam_player_data.School != 'Duke']
      #Create an arr for t-test
      players_not_duke_arr = players_not_duke['Speed'].tolist()
      stats.ttest_ind(duke_players_arr, players_not_duke_arr, equal_var = True)
 My p-value resulted in pvalue=0.45928484103163847. There was not significant difference in the players from duke's speed that the rest of the population (aka all the other cards not including Duke)

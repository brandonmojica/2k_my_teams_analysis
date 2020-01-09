import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', None)

file_path = '/Users/brandonmojica/Desktop/Galvanize/Capstones/Capstone_1/2k_my_teams_analysis/player_data_2.json'
raw_data = pd.read_json(file_path,lines=True)

player_data = raw_data.copy()

def split_athleticism_2(row_str):
    '''
    Description: 
    
    This fuction takes in a string and parses that string into 8 attributes into a list. This is meant to be used with the pandas apply method.
    
    INPUT:
        - row_str: a single string of data 
        
    OUTPUT: Tuple of the 8 attributes or a tuple of the 8 0's if there is an error some where
    
    '''
    
    
    try:
        Athleticism = re.split('Athleticism',  row_str)
                

        Speed = re.split('Speed',Athleticism[1])
                

        Acceleration = re.split('Acceleration',Speed[1])
                

        Vertical = re.split('Vertical',Acceleration[1])
                

        Strength = re.split('Strength',Vertical[1])
                

        Stamina = re.split('Stamina',Strength[1])
                

        Hustle = re.split('Hustle',Stamina[1])
                

        Overall_durability = re.split('Overall durability',Hustle[1])

        return int(Athleticism[0]),int(Speed[0]),int(Acceleration[0]),int(Vertical[0]),int(Strength[0]),int(Stamina[0]),int(Hustle[0]),int(Overall_durability[0])
    
    except:
           return 0,0,0,0,0,0,0,0       

athleticism_df = player_data['athleticism'].apply(split_athleticism_2)    
#convert the current series dataframe into a list dataframe
final_athleticism= pd.DataFrame(athleticism_df.to_list())

#change the name of the cols
final_athleticism.rename({0:"Athleticism", 1: "Speed", 2: "Acceleration", 3: "Vertical", 4: "Strength",5: "Stamina",6: "Hustle",7: "Overall_durability"},inplace=True,axis=1)

#combine the original data frame and the new cleaned Athleticism dataframe
player_data_and_Athleticism_df= pd.concat((player_data,final_athleticism),axis=1)

def split_playmaking(row_str):
    
    '''
    Description: 
    
    This fuction takes in a string and parses that string into 6 attributes into a list. This is meant to be used with the pandas apply method.
    
    INPUT:
        - row_str: a single string of data 
        
    OUTPUT: Tuple of the 6 attributes or a tuple of the 8 0's if there is an error some where
    
    '''
    
    try:
        Playmaking = re.split('Playmaking',  row_str)
                

        Speed_with_ball = re.split('Speed with ball',Playmaking[1])
               

        Ball_handle = re.split('Ball handle',Speed_with_ball[1])
                

        Passing_accuracy = re.split('Passing accuracy',Ball_handle[1])
                

        Passing_vision = re.split('Passing vision',Passing_accuracy[1])
               

        Passing_IQ = re.split('Passing IQ',Passing_vision[1])
               

        return int(Playmaking[0]),int(Speed_with_ball[0]),int(Ball_handle[0]),int(Passing_accuracy[0]),int(Passing_vision[0]),int(Passing_IQ[0])
    except:
           return 0,0,0,0,0,0      

playmaking_df = player_data['playmaking'].apply(split_playmaking)

final_playmaking_df = pd.DataFrame(playmaking_df.to_list())

final_playmaking_df.rename({0:"playmaking", 1: "Speed_with_ball", 2: "Ball_handle", 3: "Passing_accuracy", 4: "Passing_vision",5: "Passing_IQ"},inplace=True,axis=1)
                      
final_athleticism_and_final_playmaking_df = pd.concat((player_data_and_Athleticism_df,final_playmaking_df),axis=1)

def split_rebounding(row_str):


    '''
    Description: 
    
    This fuction takes in a string and parses that string into 3 attributes into a list. This is meant to be used with the pandas apply method.
    
    INPUT:
        - row_str: a single string of data 
        
    OUTPUT: Tuple of the 3 attributes or a tuple of the 3 0's if there is an error some where
    
    '''


    try:
        Rebounding = re.split('Rebounding',  row_str)
                #athletic_array.append(Athleticism)

        Offensive_rebound = re.split('Offensive rebound',Rebounding[1])
                #athletic_array.append(Speed)

        Defensive_rebound = re.split('Defensive rebound',Offensive_rebound[1])
                #athletic_array.append(Acceleration)

        return int(Rebounding[0]),int(Offensive_rebound[0]),int(Defensive_rebound[0])
    except:
           return 0,0,0

rebounding_df = player_data['rebounding'].apply(split_rebounding)

final_rebounding_df = pd.DataFrame(rebounding_df.to_list())

final_rebounding_df.rename({0:"Rebounding", 1: "Offensive_rebound", 2: "Defensive_rebound"},inplace=True,axis=1)

final_rebounding_and_final_playmaking_df = pd.concat((final_athleticism_and_final_playmaking_df,final_rebounding_df),axis=1)



def split_inside_scoring(row_str):
    try:
        Inside_scoring = re.split('Inside scoring',  row_str)
               

        Driving_layup = re.split('Driving layup',Inside_scoring[1])
               

        Standing_dunk = re.split('Standing dunk',Driving_layup[1])
               
        
        Driving_dunk = re.split('Driving dunk',  Standing_dunk[1])
               

        Draw_foul = re.split('Draw foul',Driving_dunk[1])
                

        Post_moves = re.split('Post moves',Draw_foul[1])
                
            
        Post_hook = re.split('Post hook',Post_moves[1])
                

        Post_fade = re.split('Post fade',Post_hook[1])
                
            
        Hands = re.split('Hands',Post_fade[1])
            
        return int(Inside_scoring[0]),int(Driving_layup[0]),int(Standing_dunk[0]),int(Driving_dunk[0]),int(Draw_foul[0]),int(Post_moves[0]),int(Post_hook[0]),int(Post_fade[0]),int(Hands[0])
    except:
           return 0,0,0,0,0,0,0,0,0

inside_scoring_df = player_data['inside_scoring'].apply(split_inside_scoring)

inside_scoring_df = pd.DataFrame(rebounding_df.to_list())

inside_scoring_df.rename({0:"Inside_scoring", 1: "Driving_layup", 2: "Standing_dunk", 3: "Driving_dunk", 4: "Draw_foul",5: "Post_moves",6: "Post_hook",7: "Post_fade",8: "Hands"},inplace=True,axis=1)

final_inside_scorning_and_prev = pd.concat((final_rebounding_and_final_playmaking_df,inside_scoring_df),axis=1)



def split_outside_scoring(row_str):

    '''
    Description: 
    
    This fuction takes in a string and parses that string into 7 attributes into a list. This is meant to be used with the pandas apply method.
    
    INPUT:
        - row_str: a single string of data 
        
    OUTPUT: Tuple of the 7 attributes or a tuple of the 7 0's if there is an error some where
    
    '''


    try:
        Outside_scoring = re.split('Outside scoring',  row_str)
               

        Shot_close = re.split('Shot close',Outside_scoring[1])
                

        Shot_mid = re.split('Shot mid',Shot_close[1])
                
        
        Shot_3pt = re.split('Shot 3pt',  Shot_mid[1])
                

        Shot_IQ = re.split('Shot IQ',Shot_3pt[1])
                

        Free_throw = re.split('Free throw',Shot_IQ[1])
                
            
        Offensive_consistency = re.split('Offensive consistency',Free_throw[1])
                
            
        return int(Outside_scoring[0]),int(Shot_close[0]),int(Shot_mid[0]),int(Shot_3pt[0]),int(Shot_IQ[0]),int(Free_throw[0]),int(Offensive_consistency[0])
    
    except:
           return 0,0,0,0,0,0,0

outside_scoring_df = player_data['Outside_Scoring'].apply(split_outside_scoring)

outside_scoring_df = pd.DataFrame(outside_scoring_df.to_list())

outside_scoring_df.rename({0:"Outside_scoring", 1: "Shot_close", 2: "Shot_mid", 3: "Shot_3pt", 4: "Shot_IQ",5: "Free_throw",6: "Offensive_consistency"},inplace=True,axis=1)


final_outside_scorning_and_prev = pd.concat((final_inside_scorning_and_prev,outside_scoring_df),axis=1)


def split_defending(row_str):
    
    '''
    Description: 
    
    This fuction takes in a string and parses that string into 12 attributes into a list. This is meant to be used with the pandas apply method.
    
    INPUT:
        - row_str: a single string of data 
        
    OUTPUT: Tuple of the 12 attributes or a tuple of the 12 0's if there is an error some where
    
    '''
    
    try:
        Defending = re.split('Defending',  row_str)
                

        Interior_defense = re.split('Interior defense',Defending[1])
               

        Perimeter_defense = re.split('Perimeter defense',Interior_defense[1])
                
        
        Help_defense_IQ = re.split('Help defense IQ',  Perimeter_defense[1])
                

        Pick_and_roll_defense_IQ = re.split('Pick & roll defense IQ',Help_defense_IQ[1])
                

        Lateral_quickness = re.split('Lateral quickness',Pick_and_roll_defense_IQ[1])
                
            
        Pass_perception = re.split('Pass perception',Lateral_quickness[1])
                

        Reaction_time = re.split('Reaction time',Pass_perception[1])
                
            
        Steal = re.split('Steal',Reaction_time[1])
        
        Block = re.split('Block',Steal[1])
        
        Shot_contest = re.split('Shot contest',Block[1])
        
        Defensive_consistency = re.split('Defensive consistency',Shot_contest[1])
        
        
            
        return int(Defending[0]),int(Interior_defense[0]),int(Perimeter_defense[0]),int(Help_defense_IQ[0]),int(Pick_and_roll_defense_IQ[0]),int(Lateral_quickness[0]),int(Pass_perception[0]),int(Reaction_time[0]),int(Steal[0]),int(Block[0]),int(Shot_contest[0]),int(Defensive_consistency[0])
    
    except:
           return 0,0,0,0,0,0,0,0,0,0,0,0
        
defending_df = player_data['defending'].apply(split_defending)

defending_df = pd.DataFrame(defending_df.to_list())

defending_df.rename({0:"Defending", 1: "Interior_defense", 2: "Shot_mid", 3: "Perimeter_defense", 4: "Help_defense_IQ",5: "Pick_and_roll_defense_IQ",6: "Lateral_quickness",7:"Pass_perception", 8: "Reaction_time", 9: "Steal", 10: "Block", 11: "Shot_contest",12: "Defensive_consistency"},inplace=True,axis=1)

final_player_data = pd.concat((final_inside_scorning_and_prev,defending_df),axis=1)



myteam_player_data = final_player_data

myteam_player_data = myteam_player_data[myteam_player_data.Speed != 0]

def out_of_range_fix(num):
    if num > 100:
        s = str(num)
        return float(str(s[1:]))
    else:
        return num

def out_of_range_fix_1000(num):
    if num > 1000:
        s = str(num)
        return float(str(s[2:]))
    else:
        return num


myteam_player_data['Speed'] = myteam_player_data['Speed'].apply(out_of_range_fix)
myteam_player_data['Acceleration'] = myteam_player_data['Acceleration'].apply(out_of_range_fix)
myteam_player_data['Vertical'] = myteam_player_data['Vertical'].apply(out_of_range_fix)
myteam_player_data['Stamina'] = myteam_player_data['Stamina'].apply(out_of_range_fix)
myteam_player_data['Overall_durability'] = myteam_player_data['Overall_durability'].apply(out_of_range_fix)
myteam_player_data['Speed_with_ball'] = myteam_player_data['Speed_with_ball'].apply(out_of_range_fix)
myteam_player_data['Ball_handle'] = myteam_player_data['Ball_handle'].apply(out_of_range_fix)
myteam_player_data['Passing_accuracy'] = myteam_player_data['Passing_accuracy'].apply(out_of_range_fix)
myteam_player_data['Driving_layup'] = myteam_player_data['Driving_layup'].apply(out_of_range_fix)
myteam_player_data['Standing_dunk'] = myteam_player_data['Standing_dunk'].apply(out_of_range_fix)
myteam_player_data['Post_fade'] = myteam_player_data['Post_fade'].apply(out_of_range_fix)
myteam_player_data['Hands'] = myteam_player_data['Hands'].apply(out_of_range_fix)                               
myteam_player_data['Interior_defense'] = myteam_player_data['Interior_defense'].apply(out_of_range_fix)
myteam_player_data['Help_defense_IQ'] = myteam_player_data['Help_defense_IQ'].apply(out_of_range_fix)
myteam_player_data['Block'] = myteam_player_data['Ball_handle'].apply(out_of_range_fix)

myteam_player_data['Passing_vision'] = myteam_player_data['Passing_vision'].apply(out_of_range_fix_1000)
myteam_player_data['Passing_IQ'] = myteam_player_data['Passing_IQ'].apply(out_of_range_fix_1000)
myteam_player_data['Offensive_rebound'] = myteam_player_data['Offensive_rebound'].apply(out_of_range_fix_1000)
myteam_player_data['Defensive_rebound'] = myteam_player_data['Defensive_rebound'].apply(out_of_range_fix_1000)

myteam_player_data['Draw_foul'] = myteam_player_data['Draw_foul'].apply(out_of_range_fix_1000)
myteam_player_data['Post_moves'] = myteam_player_data['Post_moves'].apply(out_of_range_fix_1000)
myteam_player_data['Shot_mid'] = myteam_player_data['Shot_mid'].apply(out_of_range_fix_1000)
myteam_player_data['Perimeter_defense'] = myteam_player_data['Perimeter_defense'].apply(out_of_range_fix_1000)

myteam_player_data['Pass_perception'] = myteam_player_data['Pass_perception'].apply(out_of_range_fix_1000)
myteam_player_data['Steal'] = myteam_player_data['Steal'].apply(out_of_range_fix_1000)

myteam_player_data['Passing_vision'] = myteam_player_data['Passing_vision'].apply(out_of_range_fix)
myteam_player_data['Offensive_rebound'] = myteam_player_data['Offensive_rebound'].apply(out_of_range_fix)
myteam_player_data['Passing_IQ'] = myteam_player_data['Passing_IQ'].apply(out_of_range_fix)
myteam_player_data['Defensive_rebound'] = myteam_player_data['Defensive_rebound'].apply(out_of_range_fix)
myteam_player_data['Post_moves'] = myteam_player_data['Post_moves'].apply(out_of_range_fix)
myteam_player_data['Post_hook'] = myteam_player_data['Post_hook'].apply(out_of_range_fix)
myteam_player_data['Shot_mid'] = myteam_player_data['Shot_mid'].apply(out_of_range_fix)
myteam_player_data['Perimeter_defense'] = myteam_player_data['Perimeter_defense'].apply(out_of_range_fix)
myteam_player_data['Pass_perception'] = myteam_player_data['Pass_perception'].apply(out_of_range_fix)
myteam_player_data['Steal'] = myteam_player_data['Steal'].apply(out_of_range_fix_1000)
myteam_player_data['Draw_foul'] = myteam_player_data['Draw_foul'].apply(out_of_range_fix)


myteam_player_data.to_csv('/Users/brandonmojica/Desktop/Galvanize/Capstones/Capstone_1/2k_my_teams_analysis/myteams_data_2.csv')







## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy  

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye
  
## haha path
* haha
 - utter_haha
 
## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## default fallback
* out_of_scope
 - action_default_fallback
  
## corona precautions path
* corona_precautions
 - utter_corona_precautions  
  
## corona tracker path
* corona_state
 - action_corona_tracker
  
## corona symptoms path
* corona_symptoms
 - utter_corona_symptoms 

## corona zone path
* corona_zone
 - action_corona_zone
 
## corona helpline path
* corona_helpline
 - utter_corona_helpline

## corona country path
* corona_country
 - action_corona_country 
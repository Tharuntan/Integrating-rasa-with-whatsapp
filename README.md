# Rasa

* RASA is an opensource framework for building AI-powered chatbots. You can use RASA to create awesome bots for various channels such as Facebook, Telegram, Slack, etc.Here i have created a Automated chatBot for covid-19 cases using whatsappApi ,Rasa and Twilio.

## Installation 

- **How to install Rasa**
  [Installation](https://rasa.com/docs/rasa/user-guide/installation/)
  
## Start App

* Clone/Download the repo.[https://github.com/Tharun-Mamillapalli/Rasa-Bot.git](https://github.com/Tharun-Mamillapalli/Rasa-Bot.git)    
* cd into folder.  
* Run ```rasa init```.  
* Change the values in ```data/nlu.md``` your NLU training data, 
* ```data/stories.md```your stories,
* ```domain.yml```your assistant’s domain,
* ```actions.py```code for your custom actions,
* ```credentials.yml```details for connecting to other services,
* ``` endpoints.yml```details for connecting to channels like fb messenger,to suit your use-case.  

## API used

* ["https://api.covid19india.org/data.json"]("https://api.covid19india.org/data.json")

## Run App

* Run ```conda activate rasa``` to activate rasa environment .
* Run ```rasa train``` to train the updated data.
* Run ```rasa run actions``` in the another terminal simultaneously .
* Run ```rasa shell``` to start a chat session with your assistant .

## Rasa X

- **How to install Rasax**
 [Installation](https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide/).

* Install Rasax and run ```rasax```to  deploy your assistant on local host.

## Twilio
* Twilio provides a telephony infrastructure web service in the cloud, allowing web developers to integrate phone calls, text messages and IP voice communications
* Signup for a Twilio account [Here](https://www.twilio.com/try-twilio)
* [Create a Project](https://www.twilio.com/login?g=%2Fconsole%2Fprojects%2Fcreate%3F&t=afcdb21a4add30114e5283d3e144b3368e6ced57af2b08365699f245ed1540f2)

## Integrating Twilio with rasa
* Enable Whatsapp sandbox under Programmable SMS.[Here](https://www.twilio.com/console/sms/whatsapp/sandbox).
* Add Twilio channel to your RASA ```credentials.yml```.More info [here](https://rasa.com/docs/rasa/user-guide/connectors/twilio/).
* ```twilio:```
  ```account_sid: "<TWILIO ACCOUNT ID>"```
  ```auth_token: "<TWILIO AUTH TOKEN>"```
  ```twilio_number: "whatsapp:<TWILIO NUMBER>"```.
*  Launch your rasa instance. You can use ngrok to get a public https URL for your bot instance. More info [Here](https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels/#testing-channels-on-your-local-machine-with-ngrok).
   ```ngrok http 5005; rasa run```.
* Add your Rasa Twilio Webhook to [Sandbox configuration](https://www.twilio.com/console/sms/whatsapp/sandbox) .
* ```https://<your id>.ngrok.io/webhooks/facebook/webhook```
* Finally follow the instruction to join the WhatsApp sandbox from your mobile number [Here](https://www.twilio.com/console/sms/whatsapp/learn).
* Now you have your RASA bot integrated with Whatsapp.

  

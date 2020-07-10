# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from pip._vendor import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCoronaState(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker:  Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now",entities)
        state = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']



        for data in response["statewise"]:
             if data["state"] == state.title():
                print(data)
                message = "Confirmed:" +data["confirmed"]+" \n" +"Active:"+data["active"]+" \n"+"deaths:" +data["deaths"]+" \n"+"Recovered:"+data["recovered"]+" \n"+"LastUpdatedOn:"+data["lastupdatedtime"]

        print(message)
        dispatcher.utter_message(message)

        return []

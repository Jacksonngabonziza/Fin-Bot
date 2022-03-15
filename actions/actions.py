# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
#from country_list import countries_for_language
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
def getAgent(district):
    url="https://financial-chatbot-basic.herokuapp.com/api/v1/agent/location/"
    district=district.lower()
    urlr=url+district
    x=requests.get(url)
    #print(x.text)
    result=x.json()
    return result


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_agents"

     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        district=tracker.get_slot("district")             
        result=getAgent(district)
        dispatcher.utter_message(
                       f" imibare ya covid ya : are {result}."
                   )
        #els   
            #dispatcher.utter_message(
                   #    f" imibare ya covid ya {count} ni {temp}."
                 #     
        return

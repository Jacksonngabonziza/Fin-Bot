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
dist=["bugesera"
    ,"gatsibo","kayonza","kirehe","ngoma","nyagatare","rwamagana","gasabo","kicukiro","nyarugenge","burera","gakenke","gicumbi"
,"musanze","rulindo","gisagara","huye","kamonyi","muhanga","nyamagabe","nyanza","nyaruguru","ruhango","karongi"
,"ngororero","nyabihu","nyamasheke","rubavu","rusizi","rutsiro"]

from typing import Any, Text, Dict, List
#from country_list import countries_for_language
from rasa_sdk import Action, Tracker
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
)
from rasa_sdk.executor import CollectingDispatcher
import requests
def getAgent(district):
    url="http://financial-chatbot-basic.herokuapp.com/api/v1/agent/location/"
    district=district.lower()
    urlr=url+district
    x=requests.get(urlr)
    #print(x.text)
    result=x.json()
    return result
def getbranch(district):
    url="http://financial-chatbot-basic.herokuapp.com/api/v1/branches/district/"
    url=url+district
    x=requests.get(url)
    #print(x.text)
    result=x.json()
    return result

class ActionAgents(Action):

     def name(self) -> Text:
         return "action_agents"

     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        district=tracker.get_slot("district") 
        district=district.lower()
        
        result=getAgent(district)
        if len(result)>1:
            for agent in result:
                mystr=""
                mystr+=' '.join(agent)
                dispatcher.utter_message(f" {mystr}")
              
   
   
        else:  
            dispatcher.utter_message( f"  We don't have any agent yet in {district} but very soon we are adding more data.")
        district=""   
        return


class ActionBranch(Action):
     def name(self) ->Text:
        return "action_branch"
     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        district=tracker.get_slot("district")             
        result=getbranch(district)
        if len(result)>1:
            for branch in result:
                mystr=""
                mystr+=' '.join(branch)
                dispatcher.utter_message(f" {mystr}")
        else:  
            dispatcher.utter_message(f" We don't have a branch yet in {district} but very soon we are adding more data.")
        district=""        
        return

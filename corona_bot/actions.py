# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Any, Text, Dict, List,Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted


class symptom(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "symptom_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return [
                "age",
                "city",
                "medical_history",
                "exhausted",
                "caugh",
                "sore_throat",
                "loss_smell",
                "fever_level",
                "breathing_trouble",
                ]
        
    
    def slot_mappings(self) -> Dict[Text,Union[Dict,List[Dict]]]:
        return{
                'age':self.from_text(),
                'city':self.from_text(),
                'medical_history':[self.from_intent(intent="affirm", value=True),
                                  self.from_intent(intent="deny", value=False),],
                'exhausted':[self.from_intent(intent="affirm", value=True),
                                  self.from_intent(intent="deny", value=False),],
                'caugh':[self.from_intent(intent="affirm", value=True),
                                  self.from_intent(intent="deny", value=False),],
                'sore_throat':[self.from_intent(intent="affirm", value=True),
                                  self.from_intent(intent="deny", value=False),],                 
                'loss_smell':[self.from_intent(intent="affirm", value=True),
                                  self.from_intent(intent="deny", value=False),],
                'fever_level':[self.from_entity(entity="fever")],
                'breathing_trouble':[self.from_intent(intent="affirm", value=True),
                                  self.from_intent(intent="deny", value=False),],                  
                                  }
        
    def submit(self,dispatcher: CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],) -> List[Dict]:
        dispatcher.utter_message(template="utter_slots_values")
        return []
    
class Actionvalidation(Action):

    def name(self)->Text: 
        return"action_validation"

    def run (self,dispatcher:CollectingDispatcher,tracker:Tracker,
             domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
        city=tracker.get_slot("city")
        age = tracker.get_slot("age")
        medical_history = tracker.get_slot("medical_history")
        exhausted = tracker.get_slot("exhausted")
        caugh = tracker.get_slot("caugh")
        sore_throat=tracker.get_slot("sore_throat")
        loss_smell=tracker.get_slot("loss_smell")
        fever_level=tracker.get_slot("fever_level")
        breathing_trouble=tracker.get_slot("breathing_trouble")
        
        hospitals= {"chennai":"Rajiv Gandhi Government General Hospital",
            "vellore":"Government Vellore Medical College Hospital","salem":"Government Mohan Kumaramangalam Medical College Hospital","coimbatore":"ESI Hospital",
            "villupuram":"medical college hospital","tiruvannamalai":"tiruvannamalai Medical College Hospital","dharmapuri":"Government Dharmapuri Medical College Hospital",
            "karur":"Government Karur Medical College Hospital","chidambaram":"Raja Muthiah Medical College","tiruchi":"Mahatma Gandhi Memorial Government Hospital",
            "thanjavur":"Government Thanjavur Medical College Hospital","tiruvarur":"Government Tiruvarur Medical College Hospital","sivangaga":"Government Sivaganga Medical College Hospital",
            "madurai":"Government Madurai Medical College Hospital","theni":"Government Theni Medical College Hospital","tirunelveli":"Government Tirunelveli Medical College Hospital",
            "kanyakumari":"Government Kanyakumari Medical College Hospital"}

        city = city.lower()
        for i in hospitals.keys():
            if city in i.lower():
                hospital=hospitals[i]
                break
            else:
                hospital='Government Hospital'
        if loss_smell or sore_throat or caugh == True:
            if fever_level != 'no fever':
                dispatcher.utter_message(f"you are in trouble so please visit {hospital} in {city} for furthur checkup")
            else:
                dispatcher.utter_message("you have a mild symptoms ,Isolate yourself and have a quality rest and healty food")
        else:
             dispatcher.utter_message("you are perfectly healty, Please make sure that you are following the safy measures to live a healty life")
        
        return []
    
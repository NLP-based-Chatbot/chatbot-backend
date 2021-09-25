# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


class Act_palaceAppointment(Action):

    def name(self) -> Text:
        return "act_place_appointment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        userhash = tracker.get_slot("userhash")
        if  userhash == "" or userhash == None:
            dispatcher.utter_message("If you have user hash, please rovide it. If you don't\
                have one or can't remeber your previous one, don't worry .you can get\
                a new one. If you have please provide it.\
                Otherwise just say 'No'")
            return[]

        return []

class Form_placeAppointment_exactdate(FormAction):

    def  name(self) -> Text:
        return "form_place_appointment_exact_date"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["userhash","service_person","date","time"]
    
    def slot_mappings(self)-> Dict[Text,any]:
        return {}

    def submit(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain:Dict[Text,any]) -> List[Dict]:
        return [{}]


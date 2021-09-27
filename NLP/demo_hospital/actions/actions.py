# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

from dbconnection.demo_hospital_db import *


class SpecList(Action):

    def name(self) -> Text:
        return "act_list_specilizations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        specializations = session.query(Specialization)
        # userhash = tracker.get_slot("userhash")
        

        return []

class DoctorList(Action):

    def name(self) -> Text:
        return "act_list_doctors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # userhash = tracker.get_slot("userhash")
        

        return []

class DateList(Action):

    def name(self) -> Text:
        return "act_list_dates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # userhash = tracker.get_slot("userhash")
        

        return []

class TimeSlotList(Action):

    def name(self) -> Text:
        return "act_list_timeslots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # userhash = tracker.get_slot("userhash")
        

        return []
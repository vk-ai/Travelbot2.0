# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from datetime import datetime
import dateutil.parser

import logging
import requests
import json
import re

API_KEY = "AIzaSyDcbyhKMHdjZSJeb0sojf8xuQlNbQ-s3M4"

def get_geocoding(location):
    geocoding_url = "https://maps.googleapis.com/maps/api/geocode/json"
    PARAMS = {'address': location, 'key': API_KEY}
    get_req = requests.get(url = geocoding_url, params = PARAMS)
    data = get_req.json()
    latlog = ''
    if data['status'] == 'OK':
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        # latlog = str(latitude)+ ',' + str(longitude)
    return latitude, longitude

def get_requested_details(lattitude, longitude, type, radius):
    location = str(lattitude) +','+ str(longitude)
    request_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    PARAMS = {'key': API_KEY, 'location': location, 'type': type, 'radius': radius}
    get_request = requests.get(url=request_url, params=PARAMS)
    data = get_request.json()
    json_data = []
    if data['status'] == 'OK':
        json_data = data['results']
    return json_data


class ActionAskRestaurant(Action):
    def name(self):
        return "action_ask_restaurants"

    def run(self, dispatcher, tracker, domain):
        try:
            location = next(tracker.get_latest_entity_values('GPE'))
            print("location", location)
            if location:
                lattitude, longitude = get_geocoding(location)
                if lattitude and longitude:
                    get_restaurants = get_requested_details(lattitude, longitude, 'restaurant', 1000)
                    if get_restaurants:
                        restaurant_details = get_restaurants[:5]
                        print(restaurant_details)
                        print(location)
                        # dispatcher.utter_message("List of top restaurants in "+location+".")
                        print("TOp")
                        for each_restaurant in restaurant_details:
                            name = each_restaurant['name']
                            try:
                                opening_hours = "Open Now" if each_restaurant['opening_hours']['open_now'] else "Closed"
                            except:
                                opening_hours = "Not available"
                            # Images
                            try:
                                overall_rating = str(each_restaurant['rating'])
                                user_rating = str(each_restaurant['user_ratings_total'])
                                address = each_restaurant['vicinity']
                                dispatcher.utter_message("Name: "+name+"\n Opening Hours: "+opening_hours+"\n Overall Rating: "+overall_rating+"\n User Rating: "+user_rating+"\n Address: "+address)
                            except:
                                address = each_restaurant['vicinity']
                                dispatcher.utter_message(
                                    "Name: " + name + "\n Opening Hours: " + opening_hours + "\n Address: " + address)
                    else:
                        dispatcher.utter_message(
                            "Sorry! There are no restaurants available in "+location+". Thank you.")
                else:
                    dispatcher.utter_message(
                        "Sorry! The location what you are requesting is not in my memory. I'll try update my location memory. Please try again later. Thank you.")
            else:
                dispatcher.utter_message(
                    "Sorry! I'm not able to identify the location in my memory. Please try again later. Thank you.")
        except:
            dispatcher.utter_message("Sorry! I'm not able to get the requested details. Please try again later. Thank you.")
        return []


class ActionAskTouristAttraction(Action):
    def name(self):
        return "action_ask_tourist_attraction"

    def run(self, dispatcher, tracker, domain):
        try:
            # location = tracker.get_slot('location')
            location = next(tracker.get_latest_entity_values('GPE'))
            print("location", location)
            if location:
                lattitude, longitude = get_geocoding(location)
                if lattitude and longitude:
                    get_tourist_attraction = get_requested_details(lattitude, longitude, 'tourist_attraction', 30000)
                    if get_tourist_attraction:
                        tourist_attraction_details = get_tourist_attraction[:5]
                        dispatcher.utter_message("List of top Sightseeing places in "+location+".")
                        for each_tourist_attraction in tourist_attraction_details:
                            name = each_tourist_attraction['name']
                            # Images
                            try:
                                overall_rating = str(each_tourist_attraction['rating'])
                                user_rating = str(each_tourist_attraction['user_ratings_total'])
                                address = each_tourist_attraction['vicinity']
                                dispatcher.utter_message("Name: "+name+"\n Overall Rating: "+overall_rating+"\n User Rating: "+user_rating+"\n Address: "+address+"\n\n\n\n")
                            except:
                                address = each_tourist_attraction['vicinity']
                                dispatcher.utter_message("Name: " + name + "\n Address: " + address+"\n\n\n\n")
                    else:
                        dispatcher.utter_message(
                            "Sorry! There are no sightseeing places available in "+location+". Thank you.")
                else:
                    dispatcher.utter_message(
                        "Sorry! The location what you are requesting is not in my memory. I'll try update my location memory. Please try again later. Thank you.")
            else:
                dispatcher.utter_message(
                    "Sorry! I'm not able to identify the location in my memory. Please try again later. Thank you.")
        except:
            dispatcher.utter_message("Sorry! I'm not able to get the requested details. Please try again later. Thank you.")
        return []


class ActionAskCarRentals(Action):
    def name(self):
        return "action_ask_car_rentals"

    def run(self, dispatcher, tracker, domain):
        try:
            # location = tracker.get_slot('location')
            location = next(tracker.get_latest_entity_values('GPE'))
            if location:
                lattitude, longitude = get_geocoding(location)
                if lattitude and longitude:
                    get_car_rentals = get_requested_details(lattitude, longitude, 'car_rental', 2000)
                    print(get_car_rentals)
                    if len(get_car_rentals) != 0:
                        print("top")
                        car_rental_details = get_car_rentals[:5]
                        print(car_rental_details)
                        dispatcher.utter_message("List of top CarRental in "+location+".")
                        for each_car_rental in car_rental_details:
                            name = each_car_rental['name']
                            try:
                                opening_hours = "Open Now" if each_car_rental['opening_hours']['open_now'] else "Closed"
                            except:
                                opening_hours = "Not Available"
                            # Images
                            try:
                                overall_rating = str(each_car_rental['rating'])
                                user_rating = str(each_car_rental['user_ratings_total'])
                                address = each_car_rental['vicinity']
                                dispatcher.utter_message(
                                    "Name: " + name + "\n Opening Hours: " + opening_hours + "\n Overall Rating: " + overall_rating + "\n User Rating: " + user_rating + "\n Address: " + address)
                            except:
                                address = each_car_rental['vicinity']
                                dispatcher.utter_message(
                                    "Name: " + name + "\n Opening Hours: " + opening_hours + "\n Address: " + address)
                    else:
                        dispatcher.utter_message(
                            "Sorry! There are no car rental places available in "+location+". Thank you.")
                else:
                    dispatcher.utter_message(
                        "Sorry! The location what you are requesting is not in my memory. I'll try update my location memory. Please try again later. Thank you.")
            else:
                dispatcher.utter_message(
                    "Sorry! I'm not able to identify the location in my memory. Please try again later. Thank you.")
        except:
            dispatcher.utter_message("Sorry! I'm not able to get the requested details. Please try again later. Thank you.")
        return []


class HotelForm(FormAction):

    def name(self):
        return "hotel_form"

    @staticmethod
    def required_slots(tracker):
        """A list of required slots that the form has to fill"""

        return ["checkin_date", "checkout_date", "location", "num_of_guests", "num_of_children", "room_type", "email"]

    def slot_mappings(self):
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "checkin_date": [self.from_entity(entity="checkin_date"),
                             self.from_entity(entity="time")],
            "checkout_date": [self.from_entity(entity="checkout_date"),
                              self.from_entity(entity="time")],
            "location": [self.from_entity(entity="location"),
                         self.from_entity(entity="GPE"),
                         self.from_entity(entity="LOC")],
            "num_of_guests": [self.from_entity(entity="num_of_guests", intent=["request_hotel"]),
                              self.from_entity(entity="number")],
            "num_of_children": [self.from_entity(entity="num_of_children", intent=["request_hotel"]),
                                self.from_entity(entity="number")],
            "room_type": self.from_entity(entity="room_type", intent=["request_hotel"]),
            "email": self.from_entity(entity="email")
        }

    def validate_checkin_date(self, value, dispatcher, tracker, domain):
        if isinstance(value, dict):
            checkin_date = dateutil.parser.parse(value['from']).date()
            checkout_date = dateutil.parser.parse(value['to']).date()
            return {
                'checkin_date': checkin_date.strftime('%d %b %Y'),
                'checkout_date': checkout_date.strftime('%d %b %Y')
            }
        else:
            checkin_date_obj = dateutil.parser.parse(value).date()
            today_date = datetime.today().date()
            if checkin_date_obj < today_date:
                dispatcher.utter_message("Check-in date should be greater than today's date.")
            else:
                return checkin_date_obj.strftime('%d %b %Y')

    def validate_checkout_date(self, value, dispatcher, tracker, domain):
        print("start date", dateutil.parser.parse(tracker.get_slot('checkin_date')).date())
        checkout_date = dateutil.parser.parse(value).date()
        print("end date", checkout_date)
        return checkout_date.strftime('%d %b %Y')

    def validate_email(self, value, dispatcher, tracker, domain):
        return value

    def validate_num_of_guests(self, value, dispatcher, tracker, domain):
        get_guests = str(value)
        print("before", get_guests)
        print("type", type(get_guests))
        get_num = re.findall("[1-9]", get_guests)
        if get_num:
            return value
        else:
            dispatcher.utter_message("Please enter number between 1 and 9.")

    def validate_num_of_children(self, value, dispatcher, tracker, domain):
        get_children = str(value)
        get_num = re.findall("[0-9]", get_children)
        if get_num:
            return value
        else:
            dispatcher.utter_message("Please enter number between 0 and 9.")

    def submit(self, dispatcher, tracker, domain):
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_slots_values")
        dispatcher.utter_message("Thank you for providing the details. We will get back to you on your Email ID "
                                 "with Booking Confirmation. Have a nice day!")
        # slot_dict = {"checkin_date": None, "checkout_date": None, "email": None, "location": None,
        #              "num_of_children": None, "num_of_guests": None, "room_type": None}

        return [AllSlotsReset()]


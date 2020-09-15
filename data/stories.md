## happy path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## ask is bot
* ask_isbot
    - utter_ask_isbot
* ask_isbot
    - utter_ask_isbot
* ask_isbot
    - utter_ask_isbot
* ask_isbot
    - utter_ask_isbot

## Generated Story -3029874067227023368
* handle_insult
    - utter_handleinsult
* handle_insult
    - utter_handleinsult
* handle_insult
    - utter_handleinsult

## Generated Story -1605554205657970292
* handle_insult
    - utter_handleinsult
* handle_insult
    - utter_handleinsult
* handle_insult
    - utter_handleinsult
* handle_insult
    - utter_handleinsult

## Generated Story -9062694308845098253
* ask_restaurants{"location": "Kuantan"}
    - slot{"location": "Kuantan"}
    - action_ask_restaurants

## Generated Story -4517939558982572109
* ask_restaurants{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_ask_restaurants

## Generated Story 5182780972619115697
* ask_touristattraction{"location": "Malaysia"}
    - slot{"location": "Malaysia"}
    - action_ask_tourist_attraction

## Generated Story 6450551178905024046
* ask_touristattraction{"location": "France"}
    - slot{"location": "France"}
    - action_ask_tourist_attraction
* ask_touristattraction{"location": "Johor Bahru"}
    - slot{"location": "Johor Bahru"}
    - action_ask_tourist_attraction
* ask_touristattraction{"location": "Rajasthan"}
    - slot{"location": "Rajasthan"}
    - action_ask_tourist_attraction
* ask_carrentals{"location": "Malaysia"}
    - slot{"location": "Malaysia"}
    - action_ask_car_rentals
* ask_carrentals{"location": "Singapore"}
    - slot{"location": "Singapore"}
    - action_ask_car_rentals

## Generated Story 8058128380591249014
* ask_carrentals{"location": "London"}
    - slot{"location": "London"}
    - action_ask_car_rentals
* ask_carrentals{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_ask_car_rentals
* ask_carrentals{"location": "London"}
    - slot{"location": "London"}
    - action_ask_car_rentals
* ask_touristattraction{"location": "Amsterdam"}
    - slot{"location": "Amsterdam"}
    - action_ask_tourist_attraction

## interactive_story_1
* greet
    - utter_greet
* request_hotel{"location": "Johor Bahru"}
    - hotel_form

## interactive_story_1
* greet
    - utter_greet
* request_hotel{"location": "Kuala Lumpur", "GPE": "Kuala Lumpur"}
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"location": "Kuala Lumpur"}
    - slot{"requested_slot": "checkin_date"}
* form: goodbye{"time": "2020-01-26T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "2020-01-26T00:00:00.000-08:00"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-29T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "2020-01-29T00:00:00.000-08:00"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": "4"}
    - form: hotel_form
    - slot{"num_of_guests": "4"}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": "2"}
    - form: hotel_form
    - slot{"num_of_children": "2"}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Standard Room"}
    - form: hotel_form
    - slot{"room_type": "Standard Room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "vk@gmail.com"}
    - form: hotel_form
    - slot{"email": "vk@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* request_hotel{"location": "Bengaluru", "GPE": "Bengaluru"}
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"location": "Bengaluru"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-15T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "15 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-16T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "16 Jan 2020"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 3}
    - form: hotel_form
    - slot{"num_of_guests": 3}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_children": 1}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Deluxe Room"}
    - form: hotel_form
    - slot{"room_type": "Deluxe Room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "vk@vk.com"}
    - form: hotel_form
    - slot{"email": "vk@vk.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* handle_insult
    - utter_handleinsult
* handle_insult
    - utter_handleinsult
* ask_isbot
    - utter_ask_isbot
* out_of_scope{"number": 2}
    - utter_out_of_scope
* out_of_scope
    - utter_out_of_scope
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_restaurants{"location": "New York", "GPE": "New York"}
    - action_ask_restaurants
* ask_restaurants{"location": "Kuantan", "GPE": "Kuantan"}
    - action_ask_restaurants

## interactive_story_1
* greet
    - utter_greet
* handle_insult
    - utter_handleinsult
* out_of_scope{"number": 1}
    - utter_out_of_scope
    - utter_default
* handle_insult

## interactive_story_1
* ask_restaurants{"location": "Kuantan", "GPE": "Kuantan"}
    - action_ask_restaurants

## interactive_story_1
* ask_restaurants{"location": "Kuantan", "GPE": "Kuantan"}
    - action_ask_restaurants

## interactive_story_1
* ask_restaurants{"location": "New York", "GPE": "New York"}
    - action_ask_restaurants

## interactive_story_1
* ask_restaurants{"location": "Singapore", "GPE": "Singapore"}
    - action_ask_restaurants

## interactive_story_1
* ask_restaurants{"location": "Bangalore", "GPE": "Bangalore"}
    - action_ask_restaurants

## interactive_story_1
* request_hotel{"location": "Singapore", "GPE": "Singapore"}
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"location": "Singapore"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-26T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "26 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-27T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "27 Jan 2020"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 3}
    - form: hotel_form
    - slot{"num_of_guests": 3}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_children": 1}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Standard Room"}
    - form: hotel_form
    - slot{"room_type": "Standard Room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "zxcv@gmail.com"}
    - form: hotel_form
    - slot{"email": "zxcv@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* out_of_scope
    - utter_out_of_scope
* goodbye
    - utter_goodbye
* ask_restaurants{"location": "Singapore", "GPE": "Singapore"}
    - action_ask_restaurants

## interactive_story_1
* ask_restaurants{"location": "New York", "GPE": "New York"}
    - action_ask_restaurants
* ask_restaurants{"location": "Singapore", "GPE": "Singapore"}
    - action_ask_restaurants

## interactive_story_1
* ask_restaurants{"location": "Singapore", "GPE": "Singapore"}
    - action_ask_restaurants

## interactive_story_1
* ask_restaurants{"location": "Singapore", "GPE": "Singapore"}
    - action_ask_restaurants

## interactive_story_1
* ask_touristattraction{"location": "Rajasthan", "GPE": "Rajasthan"}
    - action_ask_tourist_attraction
* ask_touristattraction{"location": "Bengaluru", "GPE": "Bengaluru"}
    - action_ask_tourist_attraction
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default

## interactive_story_1
* ask_carrentals{"location": "Paris", "GPE": "Paris"}
    - action_ask_car_rentals
* ask_carrentals{"location": "New York", "GPE": "New York"}
    - action_ask_car_rentals

## interactive_story_1
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-01T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": null}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-14T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "14 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-15T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "15 Jan 2020"}
    - slot{"requested_slot": "location"}
* form: request_hotel{"GPE": "London"}
    - form: hotel_form
    - slot{"location": "London"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 4}
    - form: hotel_form
    - slot{"num_of_guests": ["4", 4]}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_children": 1}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Suites"}
    - form: hotel_form
    - slot{"room_type": "Suites"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "jak@yahoo.co.in"}
    - form: hotel_form
    - slot{"email": "jak@yahoo.co.in"}
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_1
* ask_whatspossible
    - utter_ask_whatspossible
* handle_insult
    - utter_handleinsult
* out_of_scope
    - utter_out_of_scope
* ask_isbot
    - utter_ask_isbot

## interactive_story_11
* ask_whatspossible
    - utter_ask_whatspossible

## interactive_story_12
* ask_whatspossible
    - utter_ask_whatspossible

## interactive_story_13
* ask_whatspossible
    - utter_ask_whatspossible

## interactive_story_14
* ask_whatspossible
    - utter_ask_whatspossible

## interactive_story_15
* ask_whatspossible
    - utter_ask_whatspossible

## interactive_story_111
* handle_insult
    - utter_handleinsult

## interactive_story_112
* handle_insult
    - utter_handleinsult

## interactive_story_113
* handle_insult
    - utter_handleinsult

## interactive_story_114
* handle_insult
    - utter_handleinsult

## interactive_story_115
* handle_insult
    - utter_handleinsult


## interactive_story_1111
* out_of_scope
    - utter_out_of_scope

## interactive_story_1112
* out_of_scope
    - utter_out_of_scope

## interactive_story_1113
* out_of_scope
    - utter_out_of_scope

## interactive_story_1114
* out_of_scope
    - utter_out_of_scope

## interactive_story_1115
* out_of_scope
    - utter_out_of_scope

## interactive_story_11111
* ask_isbot
    - utter_ask_isbot

## interactive_story_11112
* ask_isbot
    - utter_ask_isbot

## interactive_story_11113
* ask_isbot
    - utter_ask_isbot

## interactive_story_11114
* ask_isbot
    - utter_ask_isbot

## interactive_story_11115
* ask_isbot
    - utter_ask_isbot


## interactive_story_1
* greet
    - utter_greet
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-26T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "26 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-02-27T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "27 Feb 2020"}
    - slot{"requested_slot": "location"}
* form: greet{"GPE": "Malaysia"}
    - form: hotel_form
    - slot{"location": "Malaysia"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 3}
    - form: hotel_form
    - slot{"num_of_guests": 3}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_children": 1}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Standard Room"}
    - form: hotel_form
    - slot{"room_type": "Standard Room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "jack@live.com"}
    - form: hotel_form
    - slot{"email": "jack@live.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
* out_of_scope

## interactive_story_1
* ask_whatspossible
    - utter_ask_whatspossible
* request_hotel{"location": "Paris", "number": 1, "GPE": "Paris"}
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"location": "Paris"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-01T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": null}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-20T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "20 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-21T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "21 Jan 2020"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 4}
    - form: hotel_form
    - slot{"num_of_guests": ["4", 4]}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 4}
    - form: hotel_form
    - slot{"num_of_children": ["4", 4]}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "suites"}
    - form: hotel_form
    - slot{"room_type": "suites"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "asd@asd.com"}
    - form: hotel_form
    - slot{"email": "asd@asd.com"}
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_1
* ask_whatspossible
    - utter_ask_whatspossible
* request_hotel{"number": 3, "GPE": "Amsterda"}
    - action_ask_tourist_attraction

## interactive_story_1
* handle_insult
    - utter_handleinsult
* out_of_scope
    - utter_out_of_scope

## interactive_story_1
* ask_whatspossible
    - utter_ask_whatspossible
* ask_restaurants{"location": "New York", "GPE": "New York"}
    - action_ask_restaurants
* handle_insult
    - utter_handleinsult

## interactive_story_1
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}

## interactive_story_1
* ask_restaurants{"location": "malaysia", "GPE": "malaysia"}
    - action_ask_restaurants
* ask_carrentals{"location": "Malaysia", "GPE": "Malaysia"}
    - action_ask_car_rentals
* ask_touristattraction{"location": "malaysia", "GPE": "malaysia"}
    - action_ask_tourist_attraction

## interactive_story_1
* ask_carrentals{"location": "malaysia", "GPE": "malaysia"}
    - action_ask_car_rentals

## interactive_story_1
* ask_touristattraction{"GPE": "sweden"}
    - action_ask_tourist_attraction

## interactive_story_1
* ask_touristattraction{"GPE": "germany"}
    - action_ask_tourist_attraction


## interactive_story_1
* ask_touristattraction{"GPE": "poland"}
    - action_ask_tourist_attraction

## interactive_story_1
* ask_touristattraction{"GPE": "greece"}
    - action_ask_tourist_attraction

## interactive_story_1
* ask_touristattraction{"GPE": "france"}
    - action_ask_tourist_attraction

## interactive_story_1
* ask_touristattraction{"GPE": "paris"}
    - action_ask_tourist_attraction

 ## interactive_story_1
* ask_touristattraction{"GPE": "belgium"}
    - action_ask_tourist_attraction

## interactive_story_1
* ask_carrentals{"location": "poland"}
    - action_ask_car_rentals

## interactive_story_1
* ask_carrentals{"location": "germany"}
    - action_ask_car_rentals

## interactive_story_1
* ask_carrentals{"location": "greece"}
    - action_ask_car_rentals

## interactive_story_1
* ask_carrentals{"location": "belgium"}
    - action_ask_car_rentals

## interactive_story_1
* ask_carrentals{"location": "finland"}
    - action_ask_car_rentals

## interactive_story_1
* ask_carrentals{"location": "poland"}
    - action_ask_car_rentals
## interactive_story_1
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: greet{"time": "2020-01-22T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "22 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-23T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "23 Jan 2020"}
    - slot{"requested_slot": "location"}
* form: greet{"GPE": "paris"}
    - form: hotel_form
    - slot{"location": "paris"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 0}
    - form: hotel_form
    - slot{"num_of_guests": null}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 2}
    - form: hotel_form
    - slot{"num_of_guests": ["2", 2]}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 0}
    - form: hotel_form
    - slot{"num_of_children": 0}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Deluxe Room"}
    - form: hotel_form
    - slot{"room_type": "Deluxe Room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "vk@vk.com"}
    - form: hotel_form
    - slot{"email": "vk@vk.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
* ask_restaurants{"location": "malaysia", "GPE": "malaysia"}
    - action_ask_restaurants
* goodbye
    - utter_goodbye
* ask_carrentals{"location": "Paris", "GPE": "Paris"}
    - action_ask_car_rentals
* ask_isbot
    - utter_ask_isbot
* ask_whatspossible
    - utter_ask_whatspossible
* ask_touristattraction{"location": "Japan", "GPE": "Japan"}
    - action_ask_tourist_attraction
* request_hotel{"location": "London", "GPE": "London"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_1
* greet
    - utter_greet
* ask_touristattraction{"location": "Amsterdam", "GPE": "Amsterdam"}
    - action_ask_tourist_attraction
* goodbye
    - utter_goodbye
* ask_restaurants{"location": "New York", "GPE": "New York"}
    - action_ask_restaurants
* request_hotel{"location": "London", "GPE": "London"}
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"location": "London"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-22T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "22 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-23T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "23 Jan 2020"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 3}
    - form: hotel_form
    - slot{"num_of_guests": 3}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 0}
    - form: hotel_form
    - slot{"num_of_children": 0}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "standard room"}
    - form: hotel_form
    - slot{"room_type": "standard room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "vk@gmail.com"}
    - form: hotel_form
    - slot{"email": "vk@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart

## interactive_story_2
* out_of_scope
    - utter_out_of_scope
* ask_restaurants{"location": "New York", "GPE": "New York"}
    - action_ask_restaurants
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-02-01T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "01 Feb 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-02-02T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "02 Feb 2020"}
    - slot{"requested_slot": "location"}
* form: request_hotel{"GPE": "London"}
    - form: hotel_form
    - slot{"location": "London"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_guests": 1}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_children": 1}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Deluxe Room"}
    - form: hotel_form
    - slot{"room_type": "Deluxe Room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "vk@gmail.com"}
    - form: hotel_form
    - slot{"email": "vk@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
* ask_whatspossible
    - utter_ask_whatspossible
* ask_touristattraction{"location": "Amsterdam", "GPE": "Amsterdam"}
    - action_ask_tourist_attraction
* goodbye
    - utter_goodbye

## interactive_story_1
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-02-01T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "01 Feb 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-02-02T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "02 Feb 2020"}
    - slot{"requested_slot": "location"}
* form: request_hotel{"GPE": "Poland"}
    - form: hotel_form
    - slot{"location": "Poland"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 2}
    - form: hotel_form
    - slot{"num_of_guests": ["2", 2]}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 0}
    - form: hotel_form
    - slot{"num_of_children": 0}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Suites"}
    - form: hotel_form
    - slot{"room_type": "Suites"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "v@k.com"}
    - form: hotel_form
    - slot{"email": "v@k.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye

## interactive_story_1
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-03-01T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "01 Mar 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-03-03T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "03 Mar 2020"}
    - slot{"requested_slot": "location"}
* form: greet{"GPE": "Malaysia"}
    - form: hotel_form
    - slot{"location": "Malaysia"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_guests": 1}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 0}
    - form: hotel_form
    - slot{"num_of_children": 0}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Suites"}
    - form: hotel_form
    - slot{"room_type": "Suites"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "vk@gk.com"}
    - form: hotel_form

## interactive_story_1
* ask_restaurants{"location": "Japan", "GPE": "Japan"}
    - action_ask_restaurants
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-08-01T00:00:00.000-07:00"}
    - form: hotel_form
    - slot{"checkin_date": "01 Aug 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-08-02T00:00:00.000-07:00"}
    - form: hotel_form
    - slot{"checkout_date": "02 Aug 2020"}
    - slot{"requested_slot": "location"}
* form: request_hotel{"GPE": "germany"}
    - form: hotel_form
    - slot{"location": "germany"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 4}
    - form: hotel_form
    - slot{"num_of_guests": ["4", 4]}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 0}
    - form: hotel_form
    - slot{"num_of_children": 0}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Suites"}
    - form: hotel_form
    - slot{"room_type": "Suites"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "vk@gmail.com"}
    - form: hotel_form
    - slot{"email": "vk@gmail.com"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_restaurants{"location": "Bengaluru", "GPE": "Bengaluru"}
    - action_ask_restaurants
* ask_carrentals{"location": "Chennai", "GPE": "Chennai"}
    - action_ask_car_rentals
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-04-21T00:00:00.000-07:00"}
    - form: hotel_form
    - slot{"checkin_date": "21 Apr 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-04-22T00:00:00.000-07:00"}
    - form: hotel_form
    - slot{"checkout_date": "22 Apr 2020"}
    - slot{"requested_slot": "location"}
* form: handle_insult{"GPE": "Greece"}
    - form: hotel_form
    - slot{"location": "Greece"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 7}
    - form: hotel_form
    - slot{"num_of_guests": 7}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 0}
    - form: hotel_form
    - slot{"num_of_children": 0}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Standard Room"}
    - form: hotel_form
    - slot{"room_type": "Standard Room"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "jg@gk.com"}
    - form: hotel_form
    - slot{"email": "jg@gk.com"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_carrentals{"location": "Greece", "GPE": "Greece"}
    - action_ask_car_rentals
* goodbye
    - utter_goodbye

## interactive_story_1
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-01-22T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkin_date": "22 Jan 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-01-23T00:00:00.000-08:00"}
    - form: hotel_form
    - slot{"checkout_date": "23 Jan 2020"}
    - slot{"requested_slot": "location"}
* form: request_hotel{"GPE": "Sweden"}
    - form: hotel_form
    - slot{"location": "Sweden"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 2}
    - form: hotel_form
    - slot{"num_of_guests": ["2", 2]}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 1}
    - form: hotel_form
    - slot{"num_of_children": 1}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Suites"}
    - form: hotel_form
    - slot{"room_type": "Suites"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "v@g.com"}
    - form: hotel_form
    - slot{"email": "v@g.com"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_carrentals{"location": "Bengaluru", "GPE": "Bengaluru"}
    - action_ask_car_rentals
* ask_whatspossible
    - utter_ask_whatspossible
* out_of_scope{"number": 1}
    - utter_out_of_scope
* ask_restaurants{"location": "Chennai", "GPE": "Chennai"}
    - action_ask_restaurants

## interactive_story_1
* request_hotel
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"requested_slot": "checkin_date"}
* form: request_hotel{"time": "2020-08-22T00:00:00.000-07:00"}
    - form: hotel_form
    - slot{"checkin_date": "22 Aug 2020"}
    - slot{"requested_slot": "checkout_date"}
* form: request_hotel{"time": "2020-08-23T00:00:00.000-07:00"}
    - form: hotel_form
    - slot{"checkout_date": "23 Aug 2020"}
    - slot{"requested_slot": "location"}
* form: request_hotel{"location": "Bangalore"}
    - form: hotel_form
    - slot{"location": "Bangalore"}
    - slot{"requested_slot": "num_of_guests"}
* form: request_hotel{"number": 9}
    - form: hotel_form
    - slot{"num_of_guests": 9}
    - slot{"requested_slot": "num_of_children"}
* form: request_hotel{"number": 9}
    - form: hotel_form
    - slot{"num_of_children": 9}
    - slot{"requested_slot": "room_type"}
* form: request_hotel{"room_type": "Suites"}
    - form: hotel_form
    - slot{"room_type": "Suites"}
    - slot{"requested_slot": "email"}
* form: request_hotel{"email": "v@k.com"}
    - form: hotel_form
    - slot{"email": "v@k.com"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}

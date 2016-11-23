from math import floor
import random

questions = [
    {
        "Reindeer have very thick coats, how many hairs per square inch do they have?": [
            "13,000",
            "1,200",
            "5,000",
            "700",
            "1,000",
            "120,000"
        ]
    },
    {
        "The 1964 classic Rudolph The Red Nosed Reindeer was filmed in:": [
            "Japan",
            "United States",
            "Finland",
            "Germany"
        ]
    },
    {
        "Santas reindeer are cared for by one of the Christmas elves, what is his name?": [
            "Wunorse Openslae",
            "Alabaster Snowball",
            "Bushy Evergreen",
            "Pepper Minstix"
        ]
    },
    {
        "If all of Santas reindeer had antlers while pulling his Christmas sleigh, they would all be:": [
            "Girls",
            "Boys",
            "Girls and boys",
            "No way to tell"
        ]
    },
    {
        "What do Reindeer eat?": [
            "Lichen",
            "Grasses",
            "Leaves",
            "Berries"
        ]
    },
    {
        "What of the following is not true?": [
            "Caribou live on all continents",
            "Both reindeer and Caribou are the same species",
            "Caribou are bigger than reindeer",
            "Reindeer live in Scandinavia and Russia"
        ]
    },
    {
        "In what year did Rudolph make his television debut?": [
            "1964",
            "1979",
            "2000",
            "1956"
        ]
    },
    {
        "Who was the voice of Rudolph in the 1964 classic?": [
            "Billie Mae Richards",
            "Burl Ives",
            "Paul Soles",
            "Lady Gaga"
        ]
    },
    {
        "In 1939 what retailer used the story of Rudolph the Red Nose Reindeer?": [
            "Montgomery Ward",
            "Sears",
            "Macys",
            "Kmart"
        ]
    },
    {
        "Santa's reindeer named Donner was originally named what?": [
            "Dunder",
            "Donny",
            "Dweedle",
            "Dreamy"
        ]
    },
    {
        "Who invented the story of Rudolph?": [
            "Robert May",
            "Johnny Marks",
            "Santa",
            "J.K. Rowling"
        ]
    },
    {
        "In what location will you not find reindeer?": [
            "North Pole",
            "Lapland",
            "Korvatunturi mountain",
            "Finland"
        ]
    },
    {
        "What Makes Santa's Reindeer Fly?": [
            "Magical Reindeer Dust",
            "Fusion",
            "Amanita muscaria",
            "Elves"
        ]
    },
    {
        "Including Rudolph, how many reindeer hooves are there?": [
            "36",
            "24",
            "16",
            "8"
        ]
    },
    {
        "Santa only has one female reindeer. Which one is it?": [
            "Vixen",
            "Clarice",
            "Cupid",
            "Cupid"
        ]
    },
    {
        "In the 1964 classic Rudolph The Red Nosed Reindeer, what was the snowman narrators name?": [
            "Sam",
            "Frosty",
            "Burl",
            "Snowy"
        ]
    },
    {
        "What was Rudolph's father's name?": [
            "Donner",
            "Dasher",
            "Blixen",
            "Comet"
        ]
    },
    {
        "In the 1964 movie, What was the name of the coach of the Reindeer Games?": [
            "Comet",
            "Blixen",
            "Donner",
            "Dasher"
        ]
    },
    {
        "In the 1964 movie, what is the name of the deer that Rudolph befriends at the reindeer games?": [
            "Fireball",
            "Clarice",
            "Jumper",
            "Vixen"
        ]
    },
    {
        "In the 1964 movie, How did Donner, Rudolph's father, try to hide Rudolph's nose?": [
            "Black mud",
            "Bag",
            "Pillow case",
            "Sock"
        ]
    },
    {
        "In the 1964 movie, what does the Misfit Elf want to be instead of a Santa Elf?": [
            "Dentist",
            "Reindeer",
            "Toy maker",
            "Candlestick maker"
        ]
    },
    {
        "In the 1964 movie,what was the Bumble's one weakness?": [
            "Could not swim",
            "Always hungry",
            "Candy canes",
            "Cross eyed"
        ]
    },
    {
        "In the 1964 movie, what is Yukon Cornelius really in search of?": [
            "Peppermint",
            "Gold",
            "India",
            "Polar Bears"
        ]
    },
    {
        "In the 1964 movie, why is the train on the Island of Misfit Toys?": [
            "Square wheels",
            "No Engine",
            "Paint does not match",
            "It does not toot"
        ]
    },
    {
        "In the 1964 movie, what is the name of the Jack in the Box?": [
            "Charlie",
            "Sam",
            "Billy",
            "Jack"
        ]
    },
    {
        "In the 1964 movie, why did Santa Claus almost cancel Christmas?": [
            "Storm",
            "No snow",
            "No toys",
            "The Reindeer were sick"
        ]
    },
    {
        "In the 1964 movie, what animal noise did the elf make to distract the Bumble?": [
            "Oink",
            "Growl",
            "Bark",
            "Meow"
        ]
    },
    {
        "In the 1964 movie, what is the name of the prospector?": [
            "Yukon Cornelius",
            "Slider Sam",
            "Bumble",
            "Jack"
        ]
    },
    {
        "How far do reindeer travel when they migrate?": [
            "3000 miles",
            "700 miles",
            "500 miles",
            "0 miles"
        ]
    },
    {
        "How fast can a reindeer run?": [
            "48 miles per hour",
            "17 miles per hour",
            "19 miles per hour",
            "14 miles per hour"
        ]
    }
]


def lambda_handler(event, context):

    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()


def on_intent(intent_request, session):

	print("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId']) 
	intent = intent_request['intent'] 
	intent_name = intent_request['intent']['name'] 
	
	if session.get('attributes', {}) and 'userPromptedToContinue' in session.get('attributes', {}): 
	    del session['attributes']['userPromptedToContinue'] 
	    if intent_name == "AMAZON.NoIntent": 
	        return handle_finish_session_request(intent, session) 
	    else: 
		    return handle_repeated_request(intent, session) 
	
	# Dispatch to your skill's intent handlers 
	if intent_name == "AnswerIntent": 
		return handle_answer_request(intent, session) 
	elif intent_name == "AnswerOnlyIntent": 
		return handle_answer_request(intent, session) 
	elif intent_name == "DontKnowIntent": 
		return handle_answer_request(intent, session) 
	elif intent_name == "AMAZON.YesIntent": 
		return handle_answer_request(intent, session) 
	elif intent_name == "AMAZON.NoIntent": 
		return handle_answer_request(intent, session)
	elif intentName == "AMAZON.StartOverIntent": 
		return get_welcome_response() 
	elif intentName == "AMAZON.RepeatIntent": 
		return handle_repeat_request(intent, session) 
	elif intentName == "AMAZON.HelpIntent": 
		return handle_get_help_request(intent, session) 
	elif intentName == "AMAZON.StopIntent" or "AMAZON.CancelIntent": 
		return handle_finish_session_request(intent, session) 
	else: 
		raise ValueError("Invalid intent")
    

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------

ANSWER_COUNT = 4
GAME_LENGTH = 5
CARD_TITLE = "Reindeer Games" 


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Reindeer Games. I will ask you " + GAME_LENGTH.__str__() + \
             		" questions, try to get as many right as you can. " \
             		"Just say the number of the answer. Let's begin. "
    reprompt_text = "You can have me read you the latest headlines by saying, " \
                    "what is the news"
    should_end_session = False

    game_questions = populate_game_questions()
    correct_answer_index = floor(random.random() * (ANSWER_COUNT))
    correct_answer_index = int(correct_answer_index)
    round_answers = populate_round_answers(game_questions, 0, correct_answer_index)
    
    current_question_index = 0
    
    keys = []
    for item in questions[game_questions[current_question_index]]: 
		keys.append(item) 
    
    spoken_question = keys[0]
    reprompt_text = "Question 1. " + spoken_question + " "
    
    
    for i in range(0, ANSWER_COUNT):
    	reprompt_text += (i+1).__str__() + ". " + round_answers[i] + ". "
    
    speech_output += reprompt_text
    
    session_attributes = {
    	"speechOutput": reprompt_text,
        "repromptText": reprompt_text,
        "currentQuestionIndex": current_question_index,
        "correctAnswerIndex": correct_answer_index + 1,
        "questions": game_questions,
        "score": 0,
        "correctAnswerText": questions[game_questions[current_question_index]][keys[0]][0]
    }
    
    return build_response(session_attributes, build_speechlet_response(
        CARD_TITLE, speech_output, reprompt_text, should_end_session))

def populate_game_questions(): 
	game_questions = [] 
	index_list = [] 
	index = len(questions)
	
	if GAME_LENGTH > index: 
		raise ValueError("Invalid Game Length.")

	for i in range(0, len(questions)):
		index_list.append(i) 
	
	# Pick GAME_LENGTH random questions from the list to ask the user, make sure there are no repeats.
	for j in range(0, GAME_LENGTH):
		rand = floor(random.random() * index) 
		index -= 1 
		
		rand = int(rand)
		
		temp = index_list[index] 
		index_list[index] = index_list[rand] 
		index_list[rand] = temp 
		game_questions.append(index_list[index]) 
	
	return game_questions;
    

def populate_round_answers(game_question_indexes, correct_answer_index, correct_answer_target_location):
	answers = []
	keys = []
	
	for item in questions[game_question_indexes[correct_answer_index]]: 
		keys.append(item) 
	
	answers_copy = questions[game_question_indexes[correct_answer_index]][keys[0]] 
	index = len(answers_copy)
	
	if index < ANSWER_COUNT:
		raise ValueError("Not enough answers for question.")
		
	for i in range(0, len(answers_copy)):
		rand = int(floor(random.random() * (index-1)) + 1)
		index -= 1
		
		temp = answers_copy[index]
		answers_copy[index] = answers_copy[rand]
		answers_copy[rand] = temp
    
    
	for i in range(0, ANSWER_COUNT): 
	    answers.append(answers_copy[i])
	
	temp = answers[0]
	answers[0] = answers[correct_answer_target_location]
	answers[correct_answer_target_location] = temp 
	return answers 
    

def handle_answer_request(intent, session):

	speech_output = "" 
	session_attributes = session['attributes'] 
	
	game_in_progress = False
	if session.get('attributes', {}) and "questions" in session.get('attributes', {}):
	    game_in_progress = True
	
	answer_slot_valid = is_answer_slot_valid(intent) 
	user_gave_up = intent['name'] == "DontKnowIntent" 
	
	if game_in_progress == False:
	    # If the user responded with an answer but there is no game in progress, ask the user 
	    # if they want to start a new game. Set a flag to track that we've prompted the user. 
	    session_attributes['userPromptedToContinue'] = True 
	    speech_output = "There is no game in progress. Do you want to start a new game? " 
	    return build_response(session_attributes, build_speechlet_response(CARD_TITLE, speech_output, speech_output, False)) 
	elif answer_slot_valid == False and user_gave_up == False: 
	    reprompt = session['attributes']['speechOutput']
	    speech_output = "Your answer must be a number between 1 and " + str(ANSWER_COUNT) + ". " + reprompt 
	    return build_response(session_attributes, build_speechlet_response(CARD_TITLE, speech_output, speech_output, False)) 
	else: 
	    game_questions = session['attributes']['questions'] 
	    correct_answer_index = session['attributes']['correctAnswerIndex']
	    current_score = session['attributes']['score']
	    current_question_index = session['attributes']['currentQuestionIndex']
	    correct_answer_text = session['attributes']['correctAnswerText']

        speech_output_analysis = "" 
        if answer_slot_valid == True and intent['slots']['Answer']['value'] == correct_answer_index: 
		    current_score += 1 
		    speech_output_analysis = "correct. "
        else:
            if user_gave_up == False:
                speech_output_analysis = "wrong. "
            speech_output_analysis += "The correct answer is " + str(correct_answer_index) + ": " + correct_answer_text + ". "
            
        # if current_question_index is 4, we've reached 5 questions (zero-indexed) and can exit the game session
        if current_question_index == (GAME_LENGTH - 1):
        	speech_output = ""
        	if user_gave_up == False:
        	    speech_output += "That answer is "
        	
        	speech_output += speech_output_analysis + "You got " + current_score.__str__() + " out of " + GAME_LENGTH.__str__() + " questions correct. Thank you for playing!" 
        	return build_response(session_attributes, build_speechlet_response(CARD_TITLE, speech_output, speech_output, True))        
        else:
            current_question_index += 1
            current_question = game_questions[current_question_index]
            spoken_question = questions[current_question].keys()[0]
            # Generate a random index for the correct answer, from 0 to 3  
            correct_answer_index = int(floor(random.random() * (ANSWER_COUNT)))
            round_answers = populate_round_answers(game_questions, current_question_index, correct_answer_index) 
            
            question_index_for_speech = current_question_index + 1 
            reprompt_text = "Question " + question_index_for_speech.__str__() + ". " + spoken_question + " " 
            for i in range(0, ANSWER_COUNT): 
                reprompt_text += (i+1).__str__() + ". " + round_answers[i] + ". " 
            
            speech_output = "" 
            if user_gave_up == False: 
                speech_output += "That answer is " 
            
            speech_output += speech_output_analysis + "Your score is " + current_score.__str__() + ". " + reprompt_text 
            session_attributes = {
                "speechOutput": reprompt_text,
                "repromptText": reprompt_text,
                "currentQuestionIndex": current_question_index,
                "correctAnswerIndex": correct_answer_index + 1,
                "questions": game_questions,
                "score": current_score,
                "correctAnswerText": questions[current_question][questions[current_question].keys()[0]][0]
            }
            return build_response(session_attributes, build_speechlet_response(CARD_TITLE, speech_output, reprompt_text, False))
        
    
    
def handle_repeated_request(intent, session):
	# Repeat the previous speechOutput and repromptText from the session attributes if available
    # else start a new game session
    need_repeat = False
    if session.get('attributes', {}) and "speechOutput" in session.get('attributes', {}):
	    need_repeat = True

    if need_repeat == False:
        return get_welcome_response()
    else: 
        return build_response(session['attributes'], build_speechlet_response(CARD_TITLE, session['attributes']['speechOutput'], session['attributes']['repromptText'], False))


def handle_get_help_request(intent, session):
	# Provide a help prompt for the user, explaining how the game is played. Then, continue the game
    # if there is one in progress, or provide the option to start another one.

    # Set a flag to track that we're in the Help state.
    session['attributes']['userPromptedToContinue'] = True

    # Do not edit the help dialogue. This has been created by the Alexa team to demonstrate best practices.

    speech_output = "I will ask you " + GAME_LENGTH + " multiple choice questions. Respond with the number of the answer. " \
        "For example, say one, two, three, or four. To start a new game at any time, say, start game. " \
        "To repeat the last question, say, repeat. Would you like to keep playing?" 
    reprompt_text = "To give an answer to a question, respond with the number of the answer . Would you like to keep playing?"
    should_end_session = False
    
    return build_response(session['attributes'], build_speechlet_response(CARD_TITLE, speech_output, reprompt_text, should_end_session))


def handle_finish_session_request(intent, session):
    # End the session with a "Good bye!" if the user wants to quit the game
    return build_response({}, build_speechlet_response(CARD_TITLE, "Good bye!", "", True))
    

def is_answer_slot_valid(intent):
    answer_slot = intent.get('slots', None) and intent['slots'].get('Answer', None) and intent['slots']['Answer'].get('value', None)
    if answer_slot is not None:
        return int(answer_slot) < (ANSWER_COUNT + 1) and int(answer_slot) > 0
    return False


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Have a nice day!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))



# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session):
	return {
		'outputSpeech': {
			'type': "PlainText",
			'text': speech_output
		},
		'reprompt': {
			'outputSpeech': {
				'type': "PlainText",
				'text': reprompt_text
			}
		},
		'shouldEndSession': should_end_session
	}


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_ssml_speechlet_response(title, ssml_output, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': ssml_output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechletTitle - ' + title,
            'content': 'SessionSpeechletContent - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

import speech_recognition as sr
import random
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def define(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        requery = "Did you mean %s instead? " % get_close_matches(word, data.keys())[0]
        return requery

key = "hello cat"
key_question_one = "what do you know about"
key_question_two = "what is"
greetings_list = ["Hello","Hi!","Yo","Hola!","Hey"]


def is_greetings(text):
    if key == text:
        return True
    else:
        return False

def is_query(text):
    if key_question_one in text:
        return True
    # elif key_question_two in text:
    #     return True
    else:
        return False

def get_random_number(length):
    random_num = random.randint(0,length-1)
    return random_num

def random_greetings():
    random_num = get_random_number(len(greetings_list))
    return greetings_list[random_num]

def process_text(text):
    if is_greetings(text):
        response = random_greetings()
        return response
    elif is_query(text):
        required_query = text.split("about ",1)[1]
        result = define(required_query)
        return result
    else:
        return "This functionality is not developed yet"

sample_rate = 48000
chunk_size = 2048
language_MY = "ms-MY"
language_default = "en_US"
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()

for i,microphone_name in enumerate(mic_list):
    if microphone_name == "pulse":
        device_id = i

with sr.Microphone(device_index = device_id, sample_rate= sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print "Say something..."
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language=language_default).lower()
        print "You said : " + text
        processed_text = process_text(text)
        if type(processed_text) == list:
            for eachtext in processed_text:
                print eachtext
        else:
            print processed_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

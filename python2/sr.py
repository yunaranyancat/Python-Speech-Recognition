import speech_recognition as sr

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
    print "Say something"
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language=language_default)
        print "You said : " + text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if "what is your name" in text:
        print "Hye, my name is Yunara"
    elif "how old are you" in text:
        print "I am xx years old"
    else:
        print "I don't fucking know what you're talking about"

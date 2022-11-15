import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def write_task():
    print('что записать')

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    with open('task.txt','a') as file:
        file.write(query)
    print('записал')

def hello():
    return 'привет'


with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

if query =='привет':
    print('hi')
elif query == 'задача':
    write_task():
    print('что записать?')

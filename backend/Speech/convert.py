import vosk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import wave
import json
import words
from app import samplerate, recognize, check
from testim2 import change

'''
this script reads a mono wav file (inFileName) and writes out a json file (outfileResults) with the speech to text conversion results.  It then writes out another json file (outfileText) that only has the "text" values.
'''
global dataframe
global index

inFileName = 'D:\\forest-inventory\\Speech\\input\\test_audio.wav'
outfileResults = 'C:\\Users\\KULAN\\Desktop\\Speech\\tmp\\M1S3-Results.json'
outfileText = 'C:\\Users\\KULAN\\Desktop\\Speech\\tmp\\tmpM1S3-Text.json'

"""audio_file = inFileName

song = AudioSegment.from_wav(audio_file)

new = song.low_pass_filter(1000)

new1 = new.high_pass_filter(1000)

# increae volume by 6 dB
song_6_db_quieter = new1 + 6

# save the output
song_6_db_quieter.export('C:\\Users\\KULAN\\Desktop\\Speech\\tmp\\test.wav', "wav")

inFileName = 'C:\\Users\\KULAN\\Desktop\\Speech\\tmp\\test.wav'"""


wf = wave.open(inFileName, "rb")

# initialize a str to hold results
results = ""
textResults = []



# build the model and recognizer objects.
model = vosk.Model('model_small')
recognizer = vosk.KaldiRecognizer(model, samplerate)
recognizer.SetWords(True)
temp = ''
answer = ''

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    if recognizer.AcceptWaveform(data):
        """recognizerResult = recognizer.Result()
        results = results + recognizerResult"""
        # convert the recognizerResult string into a dictionary
        data = json.loads(recognizer.Result())['text']

        recognize(data, vectorizer, clf)
    else:
        a = change(str(recognizer.PartialResult())[17:-3])
        check(temp, a, results)
        temp = a

        # save the 'text' value from the dictionary into a list
        """
        print(data.get("text", ""))
        dataframe.iloc[index, 3] = data.get("text", "")
        textResults.append(data.get("text", ""))
        """

##    else:
##        print(recognizer.PartialResult())

# process "final" result
"""
results = results + recognizer.FinalResult()
data = json.loads(recognizer.FinalResult())
textResults.append(data.get("text", ""))


# write results to a file
with open(outfileResults, 'w') as output:
    print(results, file=output)

# write text portion of results to a file
with open(outfileText, 'w') as output:
    print(json.dumps(textResults, indent=4), file=output)
"""
from gtts import gTTS

def text_to_speech(text, lang, output_file):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)

with open(r"D:\Dataset.txt", encoding="utf-8") as pointer:
    file = pointer.readlines()

file = [elem.strip() for elem in file]

for x in range(196):

    english_text = file[x]
    hindi_text = file[x+196]
    output_file_en = r"D:\Audio Dataset\eng\{}.mp3".format(x)
    output_file_hi = r"D:\Audio Dataset\Hindi\{}.mp3".format(x)
    text_to_speech(english_text, lang='en', output_file=output_file_en)
    text_to_speech(hindi_text, lang='hi', output_file=output_file_hi)

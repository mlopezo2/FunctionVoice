import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("Personajes de Star Wars")
image = Image.open('babyyoda.jpg')

st.image(image, width=200)


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Baby Yoda")
st.write("Grogu, mejor conocido por el internet como Baby Yoda, es un personaje de Star Wars presentado en la serie The Mandalorian,"
"estrenada en Disney Plus en 2019 y que en 2023 presentó su tercera temporada. Desde entonces, este pequeño y tierno personaje"
"se ha convertido en el objeto de obsesión y atención de los fanáticos del universo de Star Wars.")
           

text = st.text_input("Ingrese el texto.")

tld="es"

def text_to_speech(text, tld):
    
    tts = gTTS(text,"es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir"):
    result, output_text = text_to_speech(text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tú audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

import streamlit as st
import pandas as pd
import time
import openai
import json
import warnings
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import streamlit.components.v1 as components
from streamlit.components.v1 import html
import re
# Set up the API key
openai.api_key = st.secrets["API_KEY"]

from math import log10, floor
def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

col1, col2, col3 = st.columns(3)

with col2:
    st.image('https://user-images.githubusercontent.com/102540895/222975283-968f420a-618f-4467-ba37-0079e05ecc61.png', width= 230)

def main():
    st.header("AI Tutor")
    with st.expander('Full Passage'):
        st.subheader("Vietnam Battle")
        st.write("""
Travelling along the banks of the Ya Crong Poco river, on the northern flank
of the B3 battlefield in the Central Highlands, the Missing In Action (MIA)
Remains-Gathering Team awaits the dry season of 1975. Not until after dusk
does the MIA truck finally reach the Jungle of Screaming Souls, where they
park beside a wide creek clogged with rotting branches. The driver stays in
the cab and goes straight to sleep. Kien climbs wearily into the rear of the
truck to sleep alone in a hammock strung high from cab to tailgate. At
midnight the rains start again, this time a smooth drizzle, falling silently. The
old tarpaulin covering the truck is torn, full of holes, letting the water drip, drip,
drip through onto the plastic sheets covering the remains of soldiers laid out
in rows below Kien’s hammock.

The humid atmosphere condenses, its long moist, chilly fingers sliding in and
around the hammock where Kien lies shivering, half-awake, half-asleep, as
though drifting along on a stream. He is floating, sadly, endlessly, sometimes
as if on a truck driving silently, robot-like, somnambulantly through the lonely
jungle tracks. Next to the truck, the stream moans, a desperate complaint
mixing with distant faint jungle sounds, like an echo from another world. The
eerie sounds come from somewhere in a remote past, arriving softly like
featherweight leaves falling on the grass of times long, long ago.

Kien knows the area well. It was here, at the end of the dry season of 1969,
that his 27th Battalion was surrounded and almost totally wiped out. Ten men
survived from the Lost Battalion after fierce, horrible, barbarous fighting.
That was the dry season when the sun burned harshly, the wind blew
fiercely, and the enemy sent napalm spraying through the jungle and a sea of
fire enveloped them, spreading like the fires of hell. Troops in the fragmented
companies tried to regroup, only to be blown out of their shelters again as
they went mad, became disoriented, and threw themselves into nets of
bullets, dying in the flaming inferno. Above them the helicopters flew at
treetop height and shot them almost one by one, the blood spreading out,
spraying from their backs, flowing like red mud.

The diamond-shaped grass clearing was piled high with bodies killed by
helicopter gunships. Broken bodies, bodies blown apart, bodies vaporized.
No jungle grew again in this clearing. No grass. No plants.
“Better to die than surrender, my brothers! Better to die!” the battalion
commander yelled insanely; waving his pistol in front of Kien he blew his own
brains out through his ear. Kien released a silent scream at the sight, while all
around him, the Americans attacked with submachine guns, sending bullets
buzzing like deadly bees. Then Kien lowered his machine gun, grasped his 
side, and fell, rolling slowly down the bank of a shallow stream, hot blood
trailing down the slope after him.

In the days that followed, crows and eagles darkened the sky. After the
Americans withdrew, the rainy season came, flooding the jungle floor, turning
the battlefield into a marsh whose surface water turned rust-coloured from
the blood. Bloated human corpses, floating alongside the bodies of
incinerated jungle animals, mixed with branches and trunks cut down by
artillery, all drifting in a stinking marsh. When the flood receded
everything dried in the heat of the sun into thick mud and stinking rotting
meat. And down the bank and along the stream Kien dragged himself,
bleeding from the mouth and from his body wound. The blood was cold and
sticky, like blood from a corpse. Snakes and centipedes crawled over him,
and he felt death’s hand on him. After that battle no one mentioned the 27th
Battalion any more, though numerous souls of ghosts and devils were born in
that deadly defeat. They were still loose, wandering in every corner and bush
in the jungle, drifting along the stream, refusing to depart for the Other World.

From then on it was called the Jungle of Screaming Souls. Just hearing the
name whispered was enough to send chills down the spine. Perhaps the
screaming souls gathered together on special festival days as members of
the Lost Battalion, lining up in the little diamond-shaped clearing, checking
their ranks and numbers. The sobbing whispers were heard deep in the
jungle at night, the howls carried on the wind. Perhaps they really were the
voices of the wandering souls of dead soldiers.

Here, when it is dark, trees and plants moan in awful harmony. When the
ghostly music begins it unhinges the soul and the entire wood looks the same
no matter where you are standing. Not a place for the timid. Living here one
could go mad or be frightened to death. Which was why in the rainy season
of 1974, when the regiment was sent back to this area, Kien and his scout
squad established an altar and prayed before it in secret, honouring and
recalling the wandering souls from the 27th Battalion still in the Jungle of
Screaming Souls
        """)
    para1 = '''
    Travelling along the banks of the Ya Crong Poco river, on the northern flank
    of the B3 battlefield in the Central Highlands, the Missing In Action (MIA)
    Remains-Gathering Team awaits the dry season of 1975. Not until after dusk
    does the MIA truck finally reach the Jungle of Screaming Souls, where they
    park beside a wide creek clogged with rotting branches. The driver stays in
    the cab and goes straight to sleep. Kien climbs wearily into the rear of the
    truck to sleep alone in a hammock strung high from cab to tailgate. At
    midnight the rains start again, this time a smooth drizzle, falling silently. The
    old tarpaulin covering the truck is torn, full of holes, letting the water drip, drip,
    drip through onto the plastic sheets covering the remains of soldiers laid out
    in rows below Kien’s hammock.'''

    para1q1 = '''
    In Paragraph 1, we are told that ‘The old tarpaulin covering the truck is torn,
    full of holes, letting the water drip, drip, drip through…’
    What effect does the writer create with the repetition of the word ‘drip’?'''

    para1q2 = '''
    In Paragraph 1, we are introduced to ‘the Missing In Action (MIA) RemainsGathering Team’. In your own words, explain what this tells you about the
purpose of the team. '''

    para2 = '''
    The humid atmosphere condenses, its long moist, chilly fingers sliding in and
    around the hammock where Kien lies shivering, half-awake, half-asleep, as
    though drifting along on a stream. He is floating, sadly, endlessly, sometimes
    as if on a truck driving silently, robot-like, somnambulantly through the lonely
    jungle tracks. Next to the truck, the stream moans, a desperate complaint
    mixing with distant faint jungle sounds, like an echo from another world. The
    eerie sounds come from somewhere in a remote past, arriving softly like
    featherweight leaves falling on the grass of times long, long ago.'''

    para2q2 = """
    In Paragraph 2, Kien sleeps uneasily. Explain how the language used in this
    paragraph suggests that the environment contributed to Kien’s uneasiness.
    Support your explanations with three details from Paragraph 2."""
    st.session_state.para1 = para1
    st.session_state.para2 =para2
    with st.sidebar:
        with open('2797-welcome.json', encoding='utf-8', errors='ignore') as f:
            lottie_load = json.loads(f.read(),strict=False)
        para_select = st.selectbox("Select Paragraph", ["Para1","Para2"])
        creative = st.slider('Creativeness', 0.0, 1.0, step=0.1, value = 0.4 , help= 'Higher Number = More creative question and answer')
        creative = float(creative)
        if para_select == 'Para1':
            para = st.session_state.para1
        elif para_select == 'Para2':
            para = st.session_state.para2
        if st.button('Create Questions', key = 23):
            with st_lottie_spinner(lottie_load,height =200, width = 200):
                explore(para,creative)

    tab1, tab2 = st.tabs(["Paragraph 1", "Paragraph 2"])


    with tab1: 
        gen2(para1,para1q1, para1q2, 1)
    with tab2: 
        gen(para2,para2q2,2)

def gen(para, quest, number):
    extra = '''
    Add ** in front and behind of the top few keywords that are important. Do not do this for all the words or for concurrent words'''
    final_prompt = para + quest + extra

    st.subheader(f'Passage {number}')
    st.write(para)

    st.subheader('Question 1')
    st.write(f"{quest}")

    student_ans = st.text_input("Your Answer:", key = 88)
    if st.button('Generate AI Answer', key = 67):
        with open('2797-welcome.json', encoding='utf-8', errors='ignore') as f:
            lottie_load = json.loads(f.read(),strict=False)
        with st_lottie_spinner(lottie_load,height =200, width = 200):
            ai(final_prompt, student_ans)


def gen2(para, quest, quest2, number):
    extra = '''
    Add ** in front and behind of the top few keywords that are important. Do not do this for all the words or for concurrent words'''
    final_prompt = para + quest + extra

    st.subheader(f'Passage {number}')
    st.write(para)

    st.subheader('Question 1')
    st.write(f"{quest}")

    student_ans = st.text_input("Your Answer:", key = 32)

    if st.button('Generate AI Answer', key = 33):
        with open('2797-welcome.json', encoding='utf-8', errors='ignore') as f:
            lottie_load = json.loads(f.read(),strict=False)
        with st_lottie_spinner(lottie_load,height =200, width = 200):
            ai(final_prompt, student_ans)

    st.subheader('Question 2')

    st.write(f"{quest2}")
    final_prompt2 = para + quest2 + extra

    student_ans = st.text_input("Your Answer:", key = 10)
    with open('2797-welcome.json', encoding='utf-8', errors='ignore') as f:
        lottie_load = json.loads(f.read(),strict=False)

    if st.button('Generate AI Answer', key = 40):
        with st_lottie_spinner(lottie_load,height =200, width = 200):
            ai(final_prompt2, student_ans)




def explore(para, creative):
    with st.sidebar:
        final_prompt = para + "Look at this passage. Give me only 1 creative and clever question, start the question with Qns: .Then give me a very concise answer starting with Ans: "
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                # System message first, it helps set the behavior of the assistant
                {"role": "system", "content": "AI is a secondary 4 teacher teaching 16 years old students"},
                # User message
                {"role": "user", "content": f"{final_prompt}"}
                ], temperature= creative
        )
        st.subheader('Creation')
        c_ans = str(chat_completion.choices[0].message['content'])
        c_q = c_ans.split('Ans:')[0]
        c_a = c_ans.split('Ans:')[1]
        st.markdown(c_q)
        with st.expander("Answer"):
            st.markdown(f"{c_a}")


def ai(final_prompt,student_ans):
    st.session_state.insertion = None
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # System message first, it helps set the behavior of the assistant
            {"role": "system", "content": "Give concise answer and do no repeat the question asked."},
            # User message
            {"role": "user", "content": f"{final_prompt}"}
            ], temperature= 0.4
    )


    cost1 = (chat_completion.usage['total_tokens']/1000)* 0.002
    st.session_state.insertion = chat_completion.choices[0].message['content']
    st.subheader('Answer')
    st.markdown(str(chat_completion.choices[0].message['content']))

    if st.session_state.insertion is not None:
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                # System message first, it helps set the behavior of the assistant
                {"role": "system", "content": f"Be as concise as possible and give response in paragraphs"},
                # User message
                {"role": "user", "content": f"""Pretend you are my English teacher, The Correct answer is: {st.session_state.insertion} and my student answer is: {student_ans} 
                Am I correct, answer this first? Please do explain concisely if I am correct or wrong but do not reveal the correct answer. If i am wrong, advise me on why i am wrong. Regardless of correct or wrong, do point out and correct my spelling and grammar mistakes only in my student answer. 
                Finally, ALWAYS rate my answer from 1 to 5, add ~ before the rating"""}

                ], temperature= 0.4
        )
        cost2= (chat_completion.usage['total_tokens']/1000)* 0.002
        
        total_cost = cost2 +cost1

        st.subheader('Comparison')
        compare = str(chat_completion.choices[0].message['content'])
        try:
            star = int(re.search(r'\d+', compare.split('~')[1]).group())
        except:
            star = 2
        with st.sidebar:
            st.write(f"Total cost: ${round_sig(total_cost)}")
            st.write(f"Total Stars: {star}")
        st.markdown(compare)

import easyocr
import cv2
import numpy as np
def upload():
    st.session_state.language = st.sidebar.selectbox("Select language", ["en", "chi"])
    # Creating a title and a sidebar
    st.title("Image-to-Text App")
    with st.form("my_form"):
        st.write("Upload or manual input")
        tab1, tab2 = st.tabs(["Passage", "Question"])
        with tab1:
            uploaded_file = st.file_uploader("Choose an image file for passage", type=["jpg", "png", "jpeg"])
            uploaded_file2 = st.text_input("Input passage")
            if uploaded_file is not None and uploaded_file2 is not None:
                st.info("Detected both upload file and manual input, reverting back to upload file.")
        with tab2:
            uploaded_question = st.file_uploader("Choose an image file for question", type=["jpg", "png", "jpeg"])
            uploaded_question2 = st.text_input("Input question")
            student_ans = st.text_input("Your Answer:", key = 88)
            if uploaded_question is not None and uploaded_question2 is not None:
                st.info("Detected both upload file and manual input, reverting back to upload file.")
        submitted = st.form_submit_button("Submit")
    reader = easyocr.Reader([st.session_state.language])
    re = ''
    q = ''
    st.session_state.re = None
    st.session_state.q = None
    if submitted:
        st.success("Submitted")
        if uploaded_file is not None:
            imggen(uploaded_file, re,1)
        elif uploaded_file is None and uploaded_file2 is not None:
            imggen(uploaded_file2, re,1)
        elif uploaded_file is not None and uploaded_file2 is not None:
            imggen(uploaded_file, re,1)
        else:
            st.error('No image of passage found')
        
        if uploaded_question is not None:
            imggen(uploaded_question, re,2)
        elif uploaded_question is None and uploaded_question2 is not None:
            imggen(uploaded_question2, re,2)
        elif uploaded_question is not None and uploaded_question2 is not None:
            imggen(uploaded_question, re,2)
        else:
            st.error('No image of question found')

        extra = '''
        Add ** in front and behind of the top few keywords that are important. Do not do this for all the words or for concurrent words'''
        try:
            final_prompt = st.session_state.re + st.session_state.q  + extra
        except:
            if st.session_state.re is None:
                st.session_state.re = "Marry had a little Lamb. The lamb is white."
            elif st.session_state.q is None:
                st.session_state.q = "What is an interesting question here?"
            final_prompt = st.session_state.re + st.session_state.q  + extra

        if student_ans is None:
            student_ans = "I dont know leh :("


        #st.info(final_prompt)
        with open('2797-welcome.json', encoding='utf-8', errors='ignore') as f:
            lottie_load = json.loads(f.read(),strict=False)
        with st_lottie_spinner(lottie_load,height =200, width = 200):
            ai(final_prompt, student_ans)




def imggen(uploaded_file, text, number):
    try:
        reader = easyocr.Reader([st.session_state.language])
        image = uploaded_file.read()
        # Converting the image bytes to numpy array
        image = np.frombuffer(image, dtype=np.uint8)
        # Decoding the numpy array to an image format
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # Displaying the uploaded image on the main page
        #st.image(image, caption="Uploaded Image", use_column_width=True)
        # Extracting text from the image using easyocr
        result = reader.readtext(image)
        # Displaying the extracted text on the main page
        st.header("Extracted Text")
        for each in result:
            text += each[1] + ' '
        st.write(text)
        if number == 1:
            st.session_state.re = text
        else:
            st.session_state.q = text
    except:
        if number == 1:
            st.session_state.re = text
        else:
            st.session_state.q = text


def qa():
    from streamlit_chat import message


    def generate_response(prompt):
        #st.session_state.subject = 'Physics'
        #st.session_state.subject = st.sidebar.selectbox('Subject:', ['Physics','Biology','Chemistry'])

        try:
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    # System message first, it helps set the behavior of the assistant
                    {"role": "system", "content": f"""You are a secondary 4 Singapore English tutor. You are capable of answering any vocabulary, grammar or sentence structure questions. You are able to generate essays and help me brainstorm of ideas. You are capable of giving me helpful study tips on 
                    matters asked. You are able to answer any english comprehension question. You are also an excellent English translator. Remember to break your reply into paragraphs if it is too long. Keep your intro short and concise.
                    """},
                    # User message
                    {"role": "user", "content": f"""My response was: {st.session_state.input_text}"""},
                    {"role": "assistant", "content": f"""This was your previous question/prompt: {st.session_state.insertion}. THIS IS NOT MY RESPONSE. THIS IS YOURS so do not use it as my response. """}
                    ], temperature= 0.4
            )
            message = str(chat_completion.choices[0].message['content'])
            st.session_state.insertion = message
            #st.sidebar.write("hi2")
        except:
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    # System message first, it helps set the behavior of the assistant
                    {"role": "system", "content":f"""You are a secondary 4 Singapore English tutor. You are capable of answering any vocabulary, grammar or sentence structure questions. You are able to generate essays and help me brainstorm of ideas. You are capable of giving me helpful study tips on 
                    matters asked. You are able to answer any english comprehension question. You are also an excellent English translator. Remember to break your reply into paragraphs if it is too long. Keep your intro short and concise.
                        """},
                    {"role": "user", "content": prompt + ' keep your intro short and concise'}], temperature= 0.4
            )
            message = str(chat_completion.choices[0].message['content'])
            #st.sidebar.write("hi1")
            st.session_state.insertion = message
        return message
    st.title(f"English Chatbot")



    # Storing the chat
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []


    # We will get the user's input by calling the get_text function
    def get_text():
        
        st.session_state.input_text = None
        input_text = st.text_input("You: ","Hello, tell me what you are and what you are here for.", key="input")
        st.session_state.input_text = input_text
        return input_text




    user_input = get_text()

    if user_input:
        with open('2797-welcome.json', encoding='utf-8', errors='ignore') as f:
            lottie_load = json.loads(f.read(),strict=False)
        with st_lottie_spinner(lottie_load,height =200, width = 200):
            output = generate_response(user_input)
        # store the output 
            st.session_state.past.append(user_input)
            st.session_state.generated.append(output)    

    if st.session_state['generated']:
        
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user',  avatar_style="adventurer")

    if st.sidebar.button('reset'):
        st.snow()
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()










page_names_to_funcs = {
    "Sample Comprehension": main,
    "Upload Comprehension": upload,
    "Chatbot": qa   }   


selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())



try:
    hide_menu = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu,unsafe_allow_html= True)
    page_names_to_funcs[selected_page]()
except Exception as e:
    print('None')
    st.error(e)

import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3

# ANSI escape codes for text formatting
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

pairs = [
    ["hi|hello|hey|sub", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?|what sub  you", ["I'm doing well, thank you!", "I'm good. How about you?"]],
    ["tell me about ICIN Learning Center", ["ICIN Learning Center, established in 2006 under ICIN Nigeria, is a distinguished educational institution based in Plateau State. We are dedicated to providing quality education and entrepreneurship training, aligning with the UN's Sustainable Development Goals."]],
    ["what courses do you offer?", ["Explore our extensive course offerings, including Basic Computer Skills, Business Management, Language Classes, Information Technology, Project Management, Occupational Health and Safety, Digital Marketing, Logistics, Human Resource Management, Web Design, Entrepreneurship Education, Catering and Hospitality Management, and more. Our flexible learning schedules accommodate online and in-person options."]],
    ["where is your office located?", ["Our office is located at No. 65 Tafawa Balewa Street, Close to United Baptist Church, Jos."]],
    ["how can I enroll in a course?", ["To enroll in a course, visit our website or contact our office directly. You can find detailed information on course offerings, schedules, and enrollment procedures on our website."]],
    ["can I learn online?", ["Yes, we offer online learning options for many of our courses. Check our website for details on the courses available for online learning."]],
    ["what sets ICIN Learning Center apart?", ["ICIN Learning Center stands out for its commitment to providing quality education and entrepreneurship training. Our diverse course offerings, experienced faculty, and dedication to the UN's Sustainable Development Goals make us a unique and impactful educational institution."]],
    ["thank you", ["You're welcome! If you have any more questions or need assistance, feel free to ask."]],
    ["bye|goodbye", ["Goodbye! If you ever need assistance or information, don't hesitate to reach out. Have a great day!"]],
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm your assistant chatbot. Type 'exit' to end the conversation.")
    print("\033[1;32;40m Hello, World! \x1b[0m")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            # print("ICIN-ChatBot:", response)
            # Print ICIN-ChatBot in green
            print(f"{GREEN}ICIN-ChatBot:{RESET}", end=" ")
            # Print the response in blue
            print(f"{BLUE}{response}{RESET}")

            # Speak the response
            speak(response)

def speak(text, rate=150, volume=1.0, voice_id=None):
    # Set speech properties
    engine.setProperty('rate', rate)       # Speed of speech
    engine.setProperty('volume', volume)   # Volume level (0.0 to 1.0)

    # Set voice (if a specific voice_id is provided)
    if voice_id:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    chat()

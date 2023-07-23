import random
import webbrowser
import cv2
import subprocess
import sys
import datetime
import pyttsx3

def open_website(website_url):
    webbrowser.open(website_url)

def open_camera():
    try:
        cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

        while True:
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the camera stream
                break

        cap.release()
        cv2.destroyAllWindows()

    except cv2.error:
        print("Error: Could not access the camera. Make sure it is properly connected.")

def open_camera_app():
    if sys.platform.startswith('win32'):
        subprocess.run("start microsoft.windows.camera:", shell=True)
    elif sys.platform.startswith('darwin'):
        subprocess.run("open -a FaceTime", shell=True)
    elif sys.platform.startswith('linux'):
        print("Sorry, opening the camera app is not supported on Linux.")
    else:
        print("Sorry, opening the camera app is not supported on this platform.")

def show_datetime():
    current_datetime = datetime.datetime.now()
    print("Current Date and Time:")
    print(current_datetime.strftime("Date: %Y-%m-%d"))
    print(current_datetime.strftime("Time: %H:%M:%S"))
    print("Day:", current_datetime.strftime("%A"))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def introduce_yourself():
    introduction = "Hello! I am a friendly chatbot. My name is Alex. I'm created by Sachinhe. My purpose is to assist you with various tasks and have enjoyable conversations. Feel free to ask me anything!"
    print(introduction)
    speak(introduction)

def suggest_books(genre):
    books_by_genre = {
        "fantasy": ["Harry Potter and the Sorcerer's Stone", "The Hobbit", "Mistborn: The Final Empire", "The Name of the Wind", "The Lies of Locke Lamora"],
        "science fiction": ["Dune", "Ender's Game", "Neuromancer", "Foundation", "The Three-Body Problem"],
        "mystery": ["And Then There Were None", "The Girl with the Dragon Tattoo", "Gone Girl", "The Da Vinci Code", "The Silent Patient"],
        "romance": ["Pride and Prejudice", "The Notebook", "Me Before You", "The Hating Game", "Outlander"],
        "thriller": ["The Girl on the Train", "Gone Girl", "The Silent Patient", "The Da Vinci Code", "The Woman in the Window"],
        "adventure": ["The Lord of the Rings", "The Hunger Games", "Jurassic Park", "Treasure Island", "The Adventures of Tom Sawyer"],
        "horror": ["Dracula", "It", "The Shining", "The Exorcist", "Frankenstein"],
    }

    book_summaries = {
        "Harry Potter and the Sorcerer's Stone": "Harry Potter, a young wizard, discovers his magical heritage and begins his journey at Hogwarts School of Witchcraft and Wizardry.",
        "The Hobbit": "Bilbo Baggins, a hobbit, joins a group of dwarves on a quest to reclaim a stolen treasure from the dragon Smaug.",
        "Mistborn: The Final Empire": "In a world ruled by a dark lord, a young street thief named Vin discovers she has magical abilities and joins a rebellion against the empire.",
        "The Name of the Wind": "Kvothe, a gifted musician and arcanist, narrates the story of his life, adventures, and pursuit of knowledge.",
        "The Lies of Locke Lamora": "Locke Lamora, a skilled thief and con artist, leads a group of fellow thieves known as the Gentlemen Bastards in the city of Camorr.",
        "Dune": "In a distant future, the desert planet of Arrakis becomes the center of political intrigue and conflict over its valuable resource, the spice melange.",
        "Ender's Game": "Child prodigy Ender Wiggin is trained at a military school in a space war against an alien race known as the Formics.",
        "Neuromancer": "A washed-up computer hacker is hired for a high-stakes heist in cyberspace, leading to a world of virtual reality and dangerous conspiracies.",
        "Foundation": "The story of the rise and fall of a galactic empire, and a group of individuals who aim to preserve knowledge and shorten the dark age to come.",
        "The Three-Body Problem": "A series of strange events related to a video game send a nanomaterials researcher into a world of conspiracy and the mysteries of the universe.",
        "And Then There Were None": "Ten strangers are invited to an isolated island, where they are accused of past crimes and start dying one by one.",
        "The Girl with the Dragon Tattoo": "A journalist and a hacker team up to investigate the disappearance of a wealthy industrialist's niece.",
        "Gone Girl": "On their fifth wedding anniversary, a man's wife goes missing, and he becomes the prime suspect in her disappearance.",
        "The Da Vinci Code": "A professor and a cryptographer follow a trail of clues left by Leonardo da Vinci to uncover a secret that could shake the foundations of Christianity.",
        "The Silent Patient": "A psychotherapist becomes obsessed with uncovering the motive behind a woman's act of shooting her husband and then never speaking again.",
        "Pride and Prejudice": "Elizabeth Bennet's journey of self-discovery and romance with Mr. Darcy in the world of 19th-century England.",
        "The Notebook": "A poignant love story about Noah and Allie, whose lives are deeply connected despite their social differences.",
        "Me Before You": "The emotional journey of a young woman who becomes a caregiver for a man left paralyzed after an accident.",
        "The Hating Game": "Two colleagues with a mutual hatred for each other find their feelings starting to change.",
        "Outlander": "Claire Randall, a WWII nurse, is transported back in time to 18th-century Scotland, where she encounters adventure and romance.",
        "The Girl on the Train": "A woman becomes entangled in a missing person investigation after witnessing something peculiar from her daily train ride.",
        "The Woman in the Window": "An agoraphobic woman observes her neighbors through her window and becomes convinced she witnessed a crime.",
        "Dracula": "Count Dracula's attempt to move from Transylvania to England and the battle between him and a group of people led by Professor Abraham Van Helsing.",
        "It": "A group of childhood friends reunite to battle an ancient evil that takes the shape of a clown named Pennywise.",
        "The Shining": "Jack Torrance, an aspiring writer, takes a job as an off-season caretaker at the haunted Overlook Hotel with his wife and son.",
        "The Exorcist": "A mother seeks the help of two priests to save her daughter from demonic possession.",
        "Frankenstein": "Victor Frankenstein creates a living creature in an unorthodox scientific experiment, leading to tragic consequences.",
    }

    genre = genre.lower()

    if genre in books_by_genre:
        suggestions = books_by_genre[genre]
        suggestion = random.choice(suggestions)
        print(f"Based on the {genre} genre, I suggest you read: {suggestion}")
        speak(f"Based on the {genre} genre, I suggest you read: {suggestion}")

        if suggestion in book_summaries:
            summary = book_summaries[suggestion]
            print("Summary:", summary)
            speak("Summary: " + summary)
        else:
            print("Sorry, I don't have a summary for this book.")
            speak("Sorry, I don't have a summary for this book.")
    else:
        print("Sorry, I don't have any book suggestions for that genre.")
        speak("Sorry, I don't have any book suggestions for that genre.")


def chatbot():
    responses = {
        "hello": ["Hi there!", "Hello!", "Hi!"],
        "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking!"],
        "what's your name": ["My name is Alex!", "I'm Alex!"],
        "introduction": [introduce_yourself],
        "open website": ["Sure! Which website would you like me to open?", "Opening the website you requested."],
        "open camera": ["Sure! Opening the camera.", "Let's open the camera."],
        "open camera app": ["Sure! Opening the camera app.", "Let's open the camera app."],
        "show date and time": ["Sure! Here's the current date and time.", "Let me show you the date and time."],
        "suggest books": ["Sure! What genre are you interested in?", "I can suggest books based on different genres. What genre do you prefer?"],
        "bye": ["Goodbye!,sir have a nice day", "Bye!"]
    }

    print("Hi! I'm Alex. What's your name?")
    speak("Hi! I'm Alex. What's your name?")
    name = input()
    print(f"Nice to meet you, {name}!")
    speak(f"Nice to meet you, {name}!")
    print("How may I help you?")
    speak("How may I help you?")

    while True:
        user_input = input("Text something: ")

        if user_input.lower() == "bye":
            print(random.choice(responses["bye"]))
            speak(random.choice(responses["bye"]))
            break
        elif "open website" in user_input.lower():
            print(random.choice(responses["open website"]))
            speak(random.choice(responses["open website"]))
            website_url = input("Please enter the website URL: ")
            open_website(website_url)
        elif "open camera" in user_input.lower():
            print(random.choice(responses["open camera"]))
            speak(random.choice(responses["open camera"]))
            open_camera()
        elif "open camera app" in user_input.lower():
            print(random.choice(responses["open camera app"]))
            speak(random.choice(responses["open camera app"]))
            open_camera_app()
        elif "show date and time" in user_input.lower():
            print(random.choice(responses["show date and time"]))
            speak(random.choice(responses["show date and time"]))
            show_datetime()
        elif "introduce yourself" in user_input.lower():
            introduce_yourself()
        elif "suggest books" in user_input.lower():
            print(random.choice(responses["suggest books"]))
            speak(random.choice(responses["suggest books"]))
            user_genre = input("Please enter the genre you are interested in: ")
            suggest_books(user_genre)
        else:
            for key in responses:
                if key in user_input.lower():
                    if callable(responses[key]):
                        responses[key]()
                    else:
                        print(random.choice(responses[key]))
                        speak(random.choice(responses[key]))
                    break

chatbot()


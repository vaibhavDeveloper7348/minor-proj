# pip install pyttsx3 SpeechRecognition pyaudio numpy scikit-learn nltk pyautogui
import json
import pyttsx3
import speech_recognition as sr
import os
import time
import pyautogui
import webbrowser
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

class HostelAssistant:
    def __init__(self):
        self.faqs = {
            "what are the hostel facilities": "guru nanak dev engineering college provides well furnished rooms wifi common room mess gym and 24x7 security",
            "how can i apply for a hostel": "you need to fill out the hostel application form available on the college website or collect it from the hostel office",
            "what are the hostel fees": "fees vary based on room type and facilities it is best to check the official website or contact the hostel office",
            "is wifi available in the hostel": "yes wifi is provided but there may be usage restrictions",
            "are visitors allowed in the hostel": "only parents or guardians are allowed during visiting hours",
            "what are the hostel entry and exit timings": "entry and exit are restricted after 10 pm for security reasons",
            "is hostel mess food good": "the food quality is decent and the menu is planned with student preferences in mind",
            "are electric appliances allowed": "no most electric appliances are not allowed due to safety concerns",
            "is there 247 security in the hostel": "yes the hostel has cctv surveillance and security guards",
            "which programs are offered by it department": "the department offers btech in information technology and mtech in computer science and it full time",
            "what is the intake capacity for btech it": "the annual intake for btech it is 180 students as per website",
            "what postgraduate program is available": "mtech in computer science and information technology is offered full time",
            "who is the head of the it department": "the head of department is dr kulvinder singh mann",
            "how can i contact it department": "you can contact via email it at gndec ac in or phone number 9915507920",
            "does the department have nptel courses": "yes the department provides access to nptel moocs for honour degree",
            "what is the vision of the it department": "to groom technically competent it professionals especially from rural punjab",
            "what is the mission of the it department": "to uplift rural students and provide technical solutions to local society",
            "is gndec it ncat accredited": "yes the it department has nba accreditation till june 2025",
            "what facilities are available for students": "facilities include departmental library laboratories infrastructure central library training and placement sports",
            "where can i find time table": "class teacher and room time tables are available on the it department website under time tables section",
            "how can i view syllabus and study scheme": "you can download btech syllabus and study schemes on the website under programs section",
            "does the department organize training programs": "yes short induction programs and four week summer training ai ml iot are organized annually",
            "who is coordinator for summer training": "dr randeep kaur and prof himani sharma coordinate the summer training programme",
            "is there an induction program": "yes an induction program for new btech lateral entry and mtech students is organized in department library",
            "where to find archives and notices": "archives with notices such as datesheets and project notices are listed under the archives section",
            "does department organize technical workshops": "yes technical workshops hackathons leadership initiatives and career development programmes are organized",
            "how to download guidelines for training and project": "training guidelines formats and rubrics are available under guidelines section on website",
            "is the department involved in research": "yes faculty are active in ai ml iot image processing big data cloud computing and network security research",
            "where is the departmental lab located": "departmental laboratories and infrastructure details are available in the facilities section",
            "what courses are offered at gndec": "gndec offers undergraduate programs including btech in civil electrical mechanical electronics communication computer science information technology robotics and ai, barch, bca, bba, bvoc interior design; postgraduate mtech mba mca msc physics msc chemistry and doctoral programs.",
            "how long is the btech program": "the btech program duration is four years divided into eight semesters.",
            "what is the intake for civil engineering btech": "intake for civil engineering is 120 seats.",
            "what is the intake for mechanical engineering btech": "intake for mechanical engineering is 150 seats.",
            "what is the intake for cse btech": "intake for computer science and engineering is either 180 or 300 depending on intake year.",
            "what is the intake for electrical engineering btech": "intake for electrical engineering is 90 seats.",
            "what is the intake for electronics and communication engineering btech": "intake for ece is 90 seats.",
            "what is the intake for information technology btech": "intake for information technology is 120 or 180 seats.",
            "is robotics and ai offered at btech": "yes btech in robotics and artificial intelligence is available with 30 seats intake.",
            "what postgraduate courses are available": "mtech in various specializations mba mca msc physics and msc chemistry are offered.",
            "what is the mtech cse intake": "intake for mtech computer science and engineering is 12 seats.",
            "what is the mtech ece intake": "intake for mtech electronics and communication engineering is 12 seats.",
            "what is the mtech environmental intake": "intake for mtech environmental science and engineering is 6 or 12 depending on document.",
            "what undergraduate commerce courses are available": "bba bca and bvoc interior design are offered at undergraduate level.",
            "how many seats are there for bba": "bba has an intake of 60 students.",
            "how many seats are there for bca": "bca intake is 60 or 180 depending on intake year.",
            "what is the duration of mtech program": "mtech programs are two years full time or three years part time.",
            "is doctorate (phd) offered": "yes phd admission is accepted under qip and ai in all engineering branches.",
            "which authority is gndec affiliated to": "gndec is affiliated to ikg pt university and is an autonomous college under ugc act.",
            "is gndec accredited": "yes accredited with naac a grade and most ug programs are nba accredited.",
            "when was gndec established": "gndec was established in 1956 under nankana sahib education trust.",
            "what is the vision of gndec": "its vision is excellence in rural india serving rural communities through technical education.",
            "does gndec have hostels": "yes boys and girls hostel facilities are available.",
            "does gndec hostels have wifi": "yes 24 hours internet facility with leased line backup.",
            "is there security in hostels": "yes cctv surveillance and security guards are present.",
            "does gndec have ncc and nss": "yes it has an ncc company and three and a half units of nss.",
            "has gndec won sports championships": "yes it has been overall sports champion of ikgptu.",
            "does gndec have an fm radio station": "yes gndec has an fm radio station under community fm scheme.",
            "does gndec have central library": "yes central library with print journals and ebooks is available.",
            "does gndec have auditorium and workshop": "yes there is an auditorium and well equipped workshops.",
            "does gndec have a dispensary on campus": "yes a dispensary is available on campus.",
            "does gndec have a bank and post office": "yes bank branch and post office are located on campus.",
            "is gndec campus urban": "yes located in urban area at gill road ludhiana spanning about 88 acres.",
            "how far is gndec from railway station": "the campus is approximately 2 km from ludhiana railway station.",
            "does gndec offer scholarships": "yes scholarships are available details in brochure pages 17 18.",
            "what is the fee for btech first year": "first year btech fee is approximately ₹96400.",
            "what is lateral entry in btech": "yes lateral entry is allowed for diploma holders under specific eligibility.",
            "what is eligibility for btech": "10+2 with physics and mathematics and one of chemistry biology cs biotech.",
            "is diploma accepted for entry": "yes diploma holders are eligible for lateral entry under ptu guidelines.",
            "what entrance exam is needed for btech": "admission via jee main and ptu online counselling.",
            "is nata required for barch": "yes for barch natascore based counselling is followed.",
            "how many rural seats are there": "70 percent seats reserved for rural area candidates.",
            "what is the quota for state vs other": "85 percent seats are for punjab candidates 15 percent for other states.",
            "does gndec have sports facilities": "yes sports ground gymnasium and indoor sports are available.",
            "is transportation available": "yes college runs bus service and public transport is available nearby.",
            "is there cafeteria or mess": "yes mess and cafeteria is available on campus.",
            "does gndec have placement cell": "yes there is a training and placement cell with strong industry ties.",
            "which companies visit for placements": "companies like tcs wipro infosys accenture amongst others recruit from gndec.",
            "do alumni work abroad": "yes alumni are placed in companies in india usa uk germany canada etc.",
            "is there testing and consultancy cell": "yes a consultancy cell provides industry services and testing.",
            "what research funding has gndec received": "funding under teqip ii teqip iii and dst fist has been received.",
            "does gndec have iso certification": "yes iso 9001 2015 certified.",
            "does gndec offer online classes": "yes ug pg online classes are conducted per academic calendar.",
            "does gndec have e library": "yes off campus access through knimbus digital library app.",
            "what cultural festivals are held": "anand utsav genesis and atharva are annual cultural and tech festivals.",
            "is there a grievance redressal committee": "yes gndec has grc to address student and staff complaints.",
            "is there anti ragging squad": "yes anti ragging squads are present with punjab police helpline.",
            "does gndec have disability resource centre": "yes a centre exists to support students with disabilities.",
            "does gndec have campus magazine": "yes harmony is annual college magazine and newsletter is published.",
            "does gndec have mooc courses": "yes mooc courses and minor degrees offered via cse dept.",
            "what software labs are available": "cse dept has ac labs with licensed software and internet.",
            "is teqip project active": "yes teqip ii iii funded modernization of teaching labs.",
            "are students eligible for visa work permit": "nba accredited graduates eligible for 1 5 year work visa.",
            "what is rural education certificate": "document required for rural quota admission issued by school.",
            "is residence certificate required": "yes punjab residents must provide certificate for admission.",
            "does gndec have anti discrimination policy": "yes a caste based discrimination complaint form is available.",
            "can i apply online for admission": "yes through admission gndec ac in with login credentials.",
            "can i change details after login": "yes use ask query tab for making changes or guidance.",
            "what is counselling fee": "counselling fees include one time rs 1200 plus university charges.",
            "are spot counselling rounds held": "yes multiple spot counselling rounds are conducted till seats fill.",
            "are fee waivers available": "yes limited fee waiver seats allotted by university.",
            "is archive of notices available": "yes public notice and important documents are on admission portal.",
            "does gndec have qip centre": "yes phd qip centre approved by ai was established.",
            "is architecture program offered": "yes 5 year barch program with 40 seats is offered.",
            "does gndec have mba program": "yes 2 year full time mba program with 60 seats is offered.",
            "does gndec have mca program": "yes mca program of 2 years with 30 seats intake is offered.",
            "is lateral entry bca allowed": "yes bca lateral entry intake is available as per document.",
            "does gndec have msc physics program": "yes 2 year msc physics with 30 seats is offered.",
            "does gndec have msc chemistry program": "yes 2 year msc chemistry with 30 seats is offered.",
            "is campus female friendly": "yes womens safety app shakti and guardian helpline support is available.",
            "is there a hostels help desk": "yes hostel help desk and helpline numbers are listed in public notice.",
            "is remote access to library possible": "yes remote access self registration available for knimbus app.",
            "are entrance exam results displayed online": "yes merit list and counselling results displayed on website.",
            "can i ask query online": "yes ask query tab is available after login on admission portal.",
            "is informal admission helpline available": "yes separate helpline numbers listed for each program.",
            "where to mail admission issues": "email admission@gndec ac in with registration number for issues.",
            "is gndec minority institution": "yes it is a sikh minority institution functioning under nset.",
            "is counselling held at auditorium": "yes first counselling held in college auditorium as per schedule.",
            "what documents needed for counselling": "original certificates 10th 12th aadhaar photos and xerox copies are required.",
            "what registration charge is required": "registration requires rs 200 non refundable + rs 1000 processing fee.",
            "is jee main score accepted": "yes eligibility includes jee main merit for btech admissions.",
            "is diploma holders eligible for btech": "yes diploma holders eligible for direct entry into btech per norms.",
            "what is punjab versus other state quota": "85% punjab state quota rest 15% open to other state candidates.",
            "is selection based on inter se merit": "yes admission based purely on merit of qualifying exam inter se.",
            "are academic departments available": "yes departments include civil me electrical ece cse it mechanical production etc.",
            "is erp portal available": "yes erp portal provides updates notices admission information with login."
        }

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

        # NLP setup
        self.vectorizer = TfidfVectorizer()
        self.questions = list(self.faqs.keys())
        self.tfidf_matrix = self.vectorizer.fit_transform(self.questions)

    def _retrain_vectorizer(self):
        self.questions = list(self.faqs.keys())
        self.tfidf_matrix = self.vectorizer.fit_transform(self.questions)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_answer(self, user_question):
        user_question = user_question.lower()
        user_vec = self.vectorizer.transform([user_question])
        similarities = cosine_similarity(user_vec, self.tfidf_matrix)
        max_sim_index = similarities.argmax()
        max_sim_score = similarities[0, max_sim_index]

        if max_sim_score >= 0.4:
            matched_question = self.questions[max_sim_index]
            answer = self.faqs[matched_question]
        else:
            answer = "Sorry, I don't have an answer to that question."

        print("Assistant:", answer)
        self.speak(answer)
        return answer

    def add_faq(self, question, answer):
        self.faqs[question] = answer
        self._retrain_vectorizer()
        print("FAQ added successfully!")

    def save_faqs(self, filename="faqs.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.faqs, file, indent=4, ensure_ascii=False)
        print("FAQs saved successfully!")

    def load_faqs(self, filename="faqs.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.faqs = json.load(file)
            self._retrain_vectorizer()
            print("FAQs loaded successfully!")
        except FileNotFoundError:
            print("No saved FAQs found. Starting with default FAQs.")

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("I am listening, please speak.")
            print("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                query = recognizer.recognize_google(audio).lower()
                print(f"You said: {query}")
                return query
            except sr.UnknownValueError:
                self.speak("Sorry, I did not understand that.")
                return ""
            except sr.RequestError:
                self.speak("Sorry, please check your internet connection.")
                return ""
            except Exception as e:
                self.speak("An error occurred.")
                print(e)
                return ""

    def search_google(self, query):
        try:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            self.speak(f"Searching for {query} on Google.")
            webbrowser.open(search_url)
        except Exception as e:
            self.speak("Failed to perform the search.")
            print(e)

    def open_application(self, app_name):
        try:
            if "notepad" in app_name:
                self.speak("Opening Notepad.")
                os.system("notepad")
            elif "calculator" in app_name:
                self.speak("Opening Calculator.")
                os.system("calc")
            elif "camera" in app_name:
                self.speak("Opening Camera.")
                os.system("start microsoft.windows.camera:")
            else:
                self.speak("Sorry, I cannot open that application right now.")
        except Exception as e:
            self.speak("Failed to open the application.")
            print(e)

    def close_application(self, app_name):
        try:
            if "notepad" in app_name:
                os.system("taskkill /IM notepad.exe /F")
                self.speak("Notepad closed.")
            elif "calculator" in app_name:
                os.system("taskkill /IM CalculatorApp.exe /F")
                self.speak("Calculator closed.")
            elif "camera" in app_name:
                os.system("taskkill /IM WindowsCamera.exe /F")
                self.speak("Camera closed.")
            else:
                self.speak("Sorry, I cannot close that application right now.")
        except Exception as e:
            self.speak("Failed to close the application.")
            print(e)

    def click_photo(self):
        try:
            self.speak("Clicking photo in 3 seconds.")
            time.sleep(3)
            pyautogui.press("enter")
            self.speak("Photo clicked and saved in gallery.")
        except Exception as e:
            self.speak("Failed to click the photo.")
            print(e)

    def open_website(self, website_name):
        try:
            url = f"https://www.{website_name}.com"
            self.speak(f"Opening {website_name}")
            webbrowser.open(url)
        except Exception as e:
            self.speak("Failed to open the website.")
            print(e)

    def close_website(self):
        try:
            self.speak("Closing the current website.")
            pyautogui.hotkey("ctrl", "w")
            time.sleep(1)
            self.speak("Website closed.")
        except Exception as e:
            self.speak("Failed to close the website.")
            print(e)

    def close_browser(self):
        try:
            self.speak("Closing the browser.")
            os.system("taskkill /IM chrome.exe /F")
            os.system("taskkill /IM msedge.exe /F")
            os.system("taskkill /IM firefox.exe /F")
            os.system("taskkill /IM brave.exe /F")
            self.speak("Browser closed.")
        except Exception as e:
            self.speak("Failed to close the browser.")
            print(e)


college_faq = {
    "btech programs": ["what programs does gndec offer", "what undergraduate courses are available", "tell me about gndec degree programs"],
    "btech duration": ["how long is the btech program", "what is the duration of btech at gndec"],
    "mtech specializations": ["what are the mtech specialisation", "which branches are available in mtech"],
    "departments": ["how many departments does gndec have", "which academic departments exist at gndec"],
    "btech fees": ["what is the btech fee structure", "how much is the first year fee for btech"],
    "lateral entry": ["does gndec allow diploma holders in btech", "can i join btech after diploma"],
    "hostel facilities": ["are hostels available at gndec", "does gndec provide student accommodation"]
}

faq_answers = {
    "btech programs": "GNDEC offers UG, PG, and PhD programs in engineering, management, and sciences.",
    "btech duration": "The B.Tech program at GNDEC lasts for 4 years.",
    "mtech specializations": "M.Tech specializations include CSE, Mechanical, Electrical, Structural, and more.",
    "departments": "GNDEC has departments in Civil, Mechanical, Electrical, CS, IT, Business, and more.",
    "btech fees": "The first-year B.Tech fee is approximately ₹96,400.",
    "lateral entry": "Yes, GNDEC allows lateral entry into B.Tech for diploma holders.",
    "hostel facilities": "Yes, GNDEC provides hostel facilities for students."
}

def answer_college_question(command, assistant):
    for key, variations in college_faq.items():
        if any(variation in command for variation in variations):
            assistant.speak(faq_answers[key])
            return True
    return False

if __name__ == "__main__":
    assistant = HostelAssistant()
    assistant.load_faqs()
    assistant.speak("Hello! I am Jack, your assistant. How can I help you today?")

    while True:
        command = assistant.listen()
        if not command:
            command = input("You: ").lower()

        if command in ["exit", "quit", "bye", "goodbye"]:
            assistant.save_faqs()
            assistant.speak("Goodbye!")
            break

        elif "add" in command:
            question = input("Enter the new question: ").lower()
            answer = input("Enter the answer: ")
            assistant.add_faq(question, answer)

        elif "search" in command:
            query = command.replace("search", "").strip()
            assistant.search_google(query)

        elif "click photo" in command:
            assistant.click_photo()

        elif "open" in command and "notepad" in command:
            assistant.open_application("notepad")

        elif "open" in command and "calculator" in command:
            assistant.open_application("calculator")

        elif "open camera" in command:
            assistant.open_application("camera")

        elif "close" in command and "notepad" in command:
            assistant.close_application("notepad")

        elif "close" in command and "calculator" in command:
            assistant.close_application("calculator")

        elif "close camera" in command:
            assistant.close_application("camera")

        elif "open" in command:
            words = command.split()
            if len(words) > 1:
                website_name = words[-1]
                assistant.open_website(website_name)

        elif "close website" in command or "close tab" in command:
            assistant.close_website()

        elif "close browser" in command:
            assistant.close_browser()

        elif answer_college_question(command, assistant):
            continue

        else:
            assistant.get_answer(command)

## Dictionaries
scale_names = {
    "PF": "Фізичне функціонування",
    "RP": "Рольове функціонування (фізичне)",
    "BP": "Біль",
    "GH": "Загальне здоров’я",
    "VT": "Життєздатність / енергійність",
    "SF": "Соціальне функціонування",
    "RE": "Рольове функціонування (емоційне)",
    "MH": "Психічне здоров’я"
}

sections = {
    'PF': ['Q3a','Q3b'],
    'RP': ['Q4a'],
    'BP': ['Q7','Q8'],
    'GH': ['Q1','Q11a'],
    'VT': ['Q9a'],
    'SF': ['Q6','Q10'],
    'RE': ['Q5a'],
    'MH': ['Q9b','Q9c','Q9d','Q9f','Q9h']
}

answer_texts = {
    "gh_rating": {
        1: "Відмінне",
        2: "Дуже добре",
        3: "Добре",
        4: "Задовільне",
        5: "Погане"
    },
    "limitations": {
        1: "Так, сильно обмежує",
        2: "Так, трохи обмежує",
        3: "Ні, зовсім не обмежує"
    },
    "yes_no": {
        1: "Так",
        2: "Ні"
    },
    "interference": {
        1: "Зовсім не заважало",
        2: "Трохи заважало",
        3: "Помірно заважало",
        4: "Сильно заважало",
        5: "Дуже сильно заважало"
    },
    "pain_severity": {
        1: "Біль був відсутній",
        2: "Дуже слабкий",
        3: "Слабкий",
        4: "Помірний",
        5: "Сильний",
        6: "Дуже сильний"
    },
    "frequency_6": {
        1: "Весь час",
        2: "Більшу частину часу",
        3: "Часто",
        4: "Іноді",
        5: "Рідко",
        6: "Жодного разу"
    },
    "frequency_5": {
        1: "Весь час",
        2: "Більшу частину часу",
        3: "Іноді",
        4: "Рідко",
        5: "Жодного разу"
    },
    "expectations": {
        1: "Цілком правильно",
        2: "Здебільшого правильно",
        3: "Важко сказати",
        4: "Здебільшого неправильно",
        5: "Цілком неправильно"
    }
}

questions = {
    "Q1": {"text": "Як ви оцінюєте своє загальне здоров’я?",
           "min": 1, "max": 5, "reverse": True, "variant": "gh_rating"},

    "Q3a": {"text": "Чи обмежує вас здоров’я у виконанні важких фізичних навантажень (біг, підйом важкого)?",
            "min": 1, "max": 3, "reverse": False, "variant": "limitations"},

    "Q3b": {"text": "Чи обмежує вас здоров’я у помірних навантаженнях (наприклад, переносити покупки)?",
            "min": 1, "max": 3, "reverse": False, "variant": "limitations"},

    "Q4a": {"text": "Через фізичне здоров’я: Чи доводилося вам скорочувати час, приділений роботі?",
            "min": 1, "max": 2, "reverse": False, "variant": "yes_no"},

    "Q5a": {"text": "Через емоційний стан: Чи доводилось вам скорочувати обсяг роботи?",
            "min": 1, "max": 2, "reverse": False, "variant": "yes_no"},

    "Q6": {"text": "Наскільки ваше фізичне або емоційне здоров’я заважало вашому звичайному соціальному життю?",
           "min": 1, "max": 5, "reverse": True, "variant": "interference"},

    "Q7": {"text": "Наскільки сильний фізичний біль ви відчували за останні 4 тижні?",
           "min": 1, "max": 6, "reverse": True, "variant": "pain_severity"},

    "Q8": {"text": "Наскільки біль заважав вашій нормальній роботі (вдома чи поза домом)?",
           "min": 1, "max": 5, "reverse": True, "variant": "interference"},

    "Q9a": {"text": "Як часто ви відчували себе повним сил та енергії?",
            "min": 1, "max": 6, "reverse": True, "variant": "frequency_6"},

    "Q9b": {"text": "Як часто ви відчували себе сильно знервованим?",
            "min": 1, "max": 6, "reverse": False, "variant": "frequency_6"},

    "Q9c": {"text": "Як часто ви відчували себе так пригнічено, що ніщо не могло вас підбадьорити?",
            "min": 1, "max": 6, "reverse": False, "variant": "frequency_6"},

    "Q9d": {"text": "Як часто ви відчували себе спокійним і умиротвореним?",
            "min": 1, "max": 6, "reverse": True, "variant": "frequency_6"},

    "Q9f": {"text": "Як часто ви відчували себе пригніченим і сумним?",
            "min": 1, "max": 6, "reverse": False, "variant": "frequency_6"},

    "Q9h": {"text": "Як часто ви відчували себе щасливим?",
            "min": 1, "max": 6, "reverse": True, "variant": "frequency_6"},

    "Q10": {"text": "Як часто ваше фізичне або емоційне здоров’я заважало вашій соціальній активності (спілкуванню)?",
            "min": 1, "max": 5, "reverse": False, "variant": "frequency_5"},

    "Q11a": {"text": "Мені здається, що моє здоров’я погіршується:",
             "min": 1, "max": 5, "reverse": False, "variant": "expectations"}
}

TOKEN = '8520830685:AAGvGEkMvKkecglIwAcfgVORvGYlq7Vd81w'
SHEET_ID = '12LRWieZfu0jYaErqehTYbL4BdkAzPgdJ0v0emMYH8Bc'
CREDENTIALS_FILE = 'credentials.json'
KEY_FILE_DRIVE_ID = '1BXsZIO1fdwADwBTA1kilhKW4pVWAdlZX'

user_answers = {}
user_answers_text = {}
user_names = {}
### End OF Dictionaries

###Bot
#t.me/Health_Survey_SF_36_bot
## Health SurveySF-36
##HealthSurvey_SF_36_bot
# 8096191207:AAEDPwIqTluvKPKWC-iICRKdXybE9cyrfvY

###previous
###bot = telebot.TeleBot('2083742394:AAEyjXFgdSXxnXOWaC3rVyfcRawCQcqQcvs')
###@HealthSurvey_SF_36_bot

bot = telebot.TeleBot(TOKEN)

for q_key, q_data in questions.items():
    variant = q_data.get("variant")
    if variant and variant in answer_texts:
        options_map = answer_texts[variant]
        sorted_options = [options_map[k] for k in sorted(options_map.keys())]
        q_data['options'] = sorted_options
    else:
        q_data['options'] = []

def download_credentials():
    if not os.path.exists(CREDENTIALS_FILE):
        url = f'https://drive.google.com/uc?export=download&id={KEY_FILE_DRIVE_ID}'
        try:
            urllib.request.urlretrieve(url, CREDENTIALS_FILE)
        except Exception:
            pass

download_credentials()

def save_full_data(chat_id, raw_answers_text, user_name):
    if not os.path.exists(CREDENTIALS_FILE):
        return

    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SHEET_ID).sheet1
        q_keys = list(questions.keys())
        existing_data = sheet.col_values(1)
        if not existing_data:
            header_row = ["No", "Date", "Name"] + q_keys
            sheet.append_row(header_row)
            next_id = 1
        else:
            next_id = len(existing_data)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [next_id, current_time, user_name]
        for q in q_keys:
            val = raw_answers_text.get(q)
            row.append(val if val is not None else "")
        sheet.append_row(row)

    except Exception as e:
        print(f"Error saving: {e}")

def transform_score(x, q):
    q_info = questions[q]
    if q_info["reverse"]:
        return ((q_info["max"] - x) / (q_info["max"] - q_info["min"])) * 100
    else:
        return ((x - q_info["min"]) / (q_info["max"] - q_info["min"])) * 100

def calculate_scales(answers):
    transformed = {}
    for q, val in answers.items():
        if q in questions:
            transformed[q] = transform_score(val, q)

    results = {}
    for scale, items in sections.items():
        vals = [transformed[q] for q in items if q in transformed]
        if vals:
            results[scale] = round(np.mean(vals), 1)
        else:
            results[scale] = None
    return results

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_answers[chat_id] = {}
    user_answers_text[chat_id] = {}
    user_names[chat_id] = ""
    msg = bot.send_message(chat_id, "Вітаю! Будь ласка, введіть Ваше ім'я та прізвище:")
    bot.register_next_step_handler(msg, process_name)

def process_name(message):
    chat_id = message.chat.id
    name = message.text
    user_names[chat_id] = name
    bot.send_message(chat_id, f"Дякую, {name}. Розпочинаємо опитування SF-36.")
    ask_next_question(chat_id)

@bot.message_handler(func=lambda message: message.text == "Повтор")
def repeat_survey(message):
    send_welcome(message)

def ask_next_question(chat_id):
    answers = user_answers.get(chat_id, {})
    remaining = [q for q in questions if q not in answers]
    if remaining:
        q = remaining[0]
        q_info = questions[q]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for option in q_info['options']:
            markup.add(option)

        msg = bot.send_message(chat_id, q_info["text"], reply_markup=markup)
        bot.register_next_step_handler(msg, process_answer, q)
    else:
        finalize(chat_id)

def process_answer(message, q):
    chat_id = message.chat.id
    text = message.text

    if text == "Повтор":
        repeat_survey(message)
        return
    q_info = questions[q]

    if text not in q_info['options']:
        msg = bot.send_message(chat_id, "Будь ласка, оберіть варіант із меню знизу екрана.")
        bot.register_next_step_handler(msg, process_answer, q)
        return

    val = q_info['options'].index(text) + q_info['min']
    if chat_id not in user_answers:
        user_answers[chat_id] = {}
    if chat_id not in user_answers_text:
        user_answers_text[chat_id] = {}

    user_answers[chat_id][q] = val
    user_answers_text[chat_id][q] = text
    ask_next_question(chat_id)

def finalize(chat_id):
    if chat_id not in user_answers:
        return

    raw_answers = user_answers[chat_id]
    raw_texts = user_answers_text.get(chat_id, {})
    name = user_names.get(chat_id, "Unknown")
    results = calculate_scales(raw_answers)
    save_full_data(chat_id, raw_texts, name)
    response_text = f"📊*{name}*, ваші результати SF-36:\n(0 - найгірше, 100 - найкраще)\n\n"

    for scale, value in results.items():
        full_name = scale_names.get(scale, scale)
        if value is not None:
            response_text += f"▫️ {full_name}: *{value}*\n"
        else:
            response_text += f"▫️ {full_name}: _недостатньо даних_\n"
    response_text += "\nЗ усіх питань та за додатковою інформацією звертайтесь: 093 544 34 61, test@gmail.com"

    del user_answers[chat_id]
    del user_answers_text[chat_id]
    del user_names[chat_id]

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add("Повтор")

    bot.send_message(chat_id, response_text, parse_mode="Markdown", reply_markup=markup)

bot.infinity_polling()

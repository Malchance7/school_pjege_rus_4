import tkinter as tk
from tkinter import font as tkfont
import random
import os

def start_training():
    print("Начало подготовки к ЕГЭ мда")
    root.destroy()

#создаю окно
root = tk.Tk()
root.title("Инструкция")
root.geometry("1600x1500")
root.resizable(False, False)

#шрифты
try:
    title_font = tkfont.Font(family="Roboto", size=28, weight="bold")
    text_font = tkfont.Font(family="Open Sans", size=16)
    button_font = tkfont.Font(family="Open Sans", size=18, weight="bold")
except:
    title_font = tkfont.Font(family="Helvetica", size=28, weight="bold")
    text_font = tkfont.Font(family="Helvetica", size=16)
    button_font = tkfont.Font(family="Helvetica", size=18, weight="bold")

# Заголовок
tk.Label(
    root,
    text="Тренажёр ударений ЕГЭ",
    font=title_font,
    pady=20
).pack()

#текст инструкции
instruction_text = """
Перед вами тренажёр для подготовки к 4 заданию ЕГЭ по русскому языку
(постановка ударений в словах).

Как работать:
1. Вам будет показано слово
2. Введите номер буквы, на которую падает ударение
3. Например, для слова "баловАть" нужно ввести 6
   (б-1, а-2, л-3, О-4, в-5, а-6, т-7, ь-8)

Программа будет вести статистику ваших ответов
и выставлять оценку по следующим критериям:
• 5 (отлично) - 90% и более правильных ответов
• 4 (хорошо) - от 75% до 89%
• 3 (удовлетворительно) - от 50% до 74%
• 2 (неудовлетворительно) - менее 50%
"""

tk.Label(
    root,
    text=instruction_text,
    font=text_font,
    justify=tk.LEFT,
    padx=30
).pack(pady=20)

#тык для начала
tk.Button(
    root,
    text="помчали",
    font=button_font,
    bg="#4CAF50",
    fg="white",
    padx=30,
    pady=10,
    command=start_training
).pack(pady=30)

root.mainloop()

#щас внизу будет куча слов которые я сидела долго ударение проставляла по орфоэпичческому словарю
words = {
        "аэропорты": 6,
        "банты": 2,
        "бороду": 2,
        "бухгалтеров": 5,
        "вероисповедание": 10,
        "водопровод": 9,
        "газопровод": 9,
        "гражданство": 6,
        "дефис": 4,
        "дешевизна": 6,
        "диспансер": 8,
        "досуг": 4,
        "еретик": 5,
        "жалюзи": 6,
        "значимость": 3,
        "иксы": 1,
        "каталог": 6,
        "километр": 6,
        "конусов": 2,
        "корысть": 4,
        "краны": 3,
        "кремень": 5,
        "кремня": 6,
        "лекторов": 2,
        "локтя": 2,
        "лыжня": 5,
        "местностей": 2,
        "намерение": 4,
        "нарост": 4,
        "недруг": 2,
        "недуг": 4,
        "некролог": 7,
        "нефтепровод": 10,
        "ногтя": 2,
        "отзыв (о книге)": 1,
        "отзыв (посла из страны)": 4,
        "отрочество": 1,
        "партер": 5,
        "портфель": 6,
        "поручни": 2,
        "приданое": 5,
        "призыв": 5,
        "сироты": 4,
        "созыв": 4,
        "сосредоточение": 9,
        "средства": 3,
        "столяр": 5,
        "таможня": 4,
        "торты": 2,
        "туфля": 2,
        "цемент": 4,
        "центнер": 2,
        "цепочка": 4,
        "шарфы": 2,
        "верна": 5,
        "значимый": 3,
        "красивее": 5,
        "кухонный": 2,
        "ловка": 5,
        "мозаичный": 5,
        "оптовый": 4,
        "прозорливый": 8,
        "сливовый": 3,
        "ждала": 5,
        "кашлянуть": 2,
        "клала": 3,
        "клеить": 3,
        "кралась": 3,
        "кровоточить": 9,
        "лгала": 5,
        "лила": 4,
        "наделит": 6,
        "надорвалась": 9,
        "назвалась": 7,
        "облегчить": 7,
        "ободрала": 8,
        "ободрить": 6,
        "озлобить": 4,
        "опошлить": 3,
        "осведомиться": 4,
        "отбыла": 6,
        "откупорить": 4,
        "плодоносить": 9,
        "пломбировать": 10,
        "повторит": 7,
        "щемит": 4,
        "щёлкать": 2,
        "довезённый": 6,
        "загнутый": 2,
        "занятый": 2,
        "занята": 6,
        "кормящий": 5,
        "кровоточaщий": 9,
        "снята": 5,
        "согнутый": 2,
        "вовремя": 2,
        "доверху": 2,
        "донельзя": 4,
        "донизу": 2,
        "досуха": 2,
        "засветло": 2,
        "затемно": 2,
        "надолго": 4,
        "ненадолго": 6   
}

class StressTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тренажёр ударений ЕГЭ")
        self.root.geometry("700x550")

        
        #тут красота наводится в виде разных цветов(ну типо чтоб кратко чтоб потом писать просто название а не искать код какой-то расшифровывать как заядлый шифровальщик)
        self.bg_color = "#F5F5F5"
        self.main_color = "#333333"
        self.accent_color = "#4A6FA5"
        self.correct_color = "#4CAF50"
        self.incorrect_color = "#F44336"
        
        #тут шрифты
        try:
            self.title_font = tkfont.Font(family="Roboto", size=24, weight="bold")
            self.main_font = tkfont.Font(family="Open Sans", size=16)
            self.grade_font = tkfont.Font(family="Open Sans", size=18, weight="bold")
        except:
            self.title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
            self.main_font = tkfont.Font(family="Helvetica", size=16)
            self.grade_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.header = tk.Label(
            self.main_frame,
            text="Тренажёр ударений",
            font=self.title_font,
            bg=self.bg_color,
            fg=self.main_color
        )
        self.header.pack(pady=20)
        
        self.word_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.word_frame.pack(pady=10)
        
        self.word_label = tk.Label(
            self.word_frame,
            text="",
            font=self.main_font,
            bg=self.bg_color,
            fg=self.main_color
        )
        self.word_label.pack()
        
        #поле для ввода
        self.entry_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.entry_frame.pack(pady=10)
        
        self.entry = tk.Entry(
            self.entry_frame,
            font=self.main_font,
            justify="center",
            width=10,
            bd=2,
            relief=tk.FLAT
        )
        self.entry.pack()
        
        #тыктык
        self.check_button = tk.Button(
            self.main_frame,
            text="Проверить",
            font=self.main_font,
            command=self.check_answer,
            bg=self.accent_color,
            fg="white",
            bd=0,
            padx=20,
            pady=5
        )
        self.check_button.pack(pady=10)
        
        #резулььтаты
        self.result_label = tk.Label(
            self.main_frame,
            text="",
            font=self.main_font,
            bg=self.bg_color,
            fg=self.main_color
        )
        self.result_label.pack(pady=5)
        
        #стата
        self.stats_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.stats_frame.pack(pady=15)
        
        self.stats_label = tk.Label(
            self.stats_frame,
            text="Правильно: 0 | Неправильно: 0",
            font=self.main_font,
            bg=self.bg_color,
            fg=self.main_color
        )
        self.stats_label.pack()
        
        self.percentage_label = tk.Label(
            self.stats_frame,
            text="Процент: 0%",
            font=self.main_font,
            bg=self.bg_color,
            fg=self.main_color
        )
        self.percentage_label.pack()
        
        #оценка
        self.grade_label = tk.Label(
            self.stats_frame,
            text="Оценка: -",
            font=self.grade_font,
            bg=self.bg_color
        )
        self.grade_label.pack(pady=10)
        
        
        self.correct = 0
        self.incorrect = 0
        self.next_word()

    
    def next_word(self):
        self.current_word, self.correct_stress = random.choice(list(words.items()))
        self.word_label.config(text=f"Слово: {self.current_word.upper()}")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
    
    def check_answer(self):
        user_input = self.entry.get().strip()
        
        if not user_input.isdigit():
            self.result_label.config(text="Введите число!", fg=self.incorrect_color)
            return
        
        user_stress = int(user_input)
        
        if user_stress == self.correct_stress:
            self.result_label.config(text="ура верно!", fg=self.correct_color)
            self.correct += 1
        else:
            self.result_label.config(
                text=f"учи слова, грамотей, неверно! Правильно: {self.correct_stress}",
                fg=self.incorrect_color
            )
            self.incorrect += 1
        
        self.update_stats()
        self.root.after(1500, self.next_word)
    
    def update_stats(self):
        total = self.correct + self.incorrect
        percentage = (self.correct / total) * 100 if total > 0 else 0
        
        self.stats_label.config(text=f"Правильно: {self.correct} | Неправильно: {self.incorrect}")
        self.percentage_label.config(text=f"Процент: {percentage:.1f}%")
        
        grade, color = self.calculate_grade(percentage)
        self.grade_label.config(text=f"Оценка: {grade}", fg=color)
    
    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "5", self.correct_color
        elif 75 <= percentage < 90:
            return "4", self.accent_color
        elif 50 <= percentage < 75:
            return "3", "#FFC107"  #тут мне лень стало
        else:
            return "2", self.incorrect_color

if __name__ == "__main__":
    root = tk.Tk()
    app = StressTrainerApp(root)
    root.mainloop()
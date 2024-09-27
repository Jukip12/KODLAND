from flask import Flask
import random

app = Flask(__name__)

numbers_list = [1, 2, 3, 4, 5]
facts_list = ["Мозг слона реагирует на человека так же, как человеческий мозг на щенка", "В США говорят на испанском больше чем в Испании", "Запасы воды на земле невосполнимы", "Женщины живут дольше всех", "Если бы человек был блохой он смог бы запрыгнуть на останкинскую телебашню"]


@app.route("/")
def hello_world():
    return f'<p>ваше случайное число (от 1 до 10): { random.choice(numbers_list) }</p>' '<a href="/random_fact">Посмотреть случайный факт!</a>'

@app.route("/random_fact")
def rand_fact():
    return f'<a>{ random.choice(facts_list) }</a>'

@app.route("/moneta")
def monye_reshka():
    a = random.randint(1, 2)
    if a == 1:
        a = "решка"
    if a == 2:
        a = 'орёл'


    return f'<p>выпал: {a}</p>'

app.run(debug=True)



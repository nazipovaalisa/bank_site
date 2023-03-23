import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

class Ling_var:
    def __init__(self, name):
        self.name = name
        self.terms = {}
        self.term_x = None

    #определяем к какому терму относится x
    def term_init(self, x):
        keys = list(self.terms.keys())
        values = [term.membership(x) for term in self.terms.values()]
        max_val = max(values)
        max_index = values.index(max_val)
        self.term_x = keys[max_index]
        self.membership = max_val


class Term:
    def __init__(self, a=None, b=None, c=None, d=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def membership(self, x):
        if self.d is None:
            if self.a is None:
                return left(x, self.b, self. c)
            elif self.c is None:
                return right(x, self.a, self. b)
            else:
                return triangle(x, self.a, self.b, self.c)
        else:
            if self.a is None:
                return left(x, self.b, self. c)
            elif self.c is None:
                return right(x, self.a, self. b)
            else:
                return trapezoid(x, self.a, self.b, self.c, self.d)


# Todo написать функции для концов интервало
def trapezoid(x, a, b, c, d):
    if a <= x <= b:
        return 1 - (b - x) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return 1 - (x - c) / (d - c)
    else:
        return 0


def triangle(x, a, b, c):
    if a <= x <= b:
        return 1 - (b - x) / (b - a)
    elif b <= x <= c:
        return 1 - (x - b) / (c - b)
    else:
        return 0


def left(x, b, c):
    if x <= b:
        return 1
    elif b <= x <= c:
        return 1 - (x - b) / (c - b)
    else:
        return 0


def right(x, a, b):
    if x <= a:
        return 0
    elif a <= x <= b:
        return 1 - (b - x) / (b - a)
    else:
        return 1


def fuzzy_output(income, payment, experience, age, i, p, e, a, credit_ability):
    r = [[0.15, income.terms['L'].membership(i), payment.terms['VL'].membership(p)],
             [0.2, income.terms['L'].membership(i), payment.terms['L'].membership(p)],
             [0.25, income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['VL'].membership(e)],
             [0.3, income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['L'].membership(e)],
             [0.35, income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['M'].membership(e)],
             [0.4, income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['H'].membership(e)],
             [0.6, income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['VH'].membership(e)],
             [0.4, income.terms['L'].membership(i), payment.terms['H'].membership(p), age.terms['L'].membership(a)],
             [0.5, income.terms['L'].membership(i), payment.terms['H'].membership(p), age.terms['M'].membership(a)],
             [0.6, income.terms['L'].membership(i), payment.terms['H'].membership(p), age.terms['H'].membership(a)],
             [0.4, income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['VL'].membership(e)],
             [0.45, income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['L'].membership(e)],
             [0.5, income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['M'].membership(e)],
             [0.7, income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['H'].membership(e)],
             [0.75, income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['VH'].membership(e)],
             [0.8, income.terms['VH'].membership(i)],
             [0.8, income.terms['H'].membership(i), age.terms['M'].membership(a)],
             [0.8, income.terms['H'].membership(i), age.terms['H'].membership(a)],
             [0.5, income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['VL'].membership(p)],
             [0.53, income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['L'].membership(p)],
             [0.55, income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['M'].membership(p)],
             [0.6, income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['H'].membership(p)],
             [0.65, income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['VH'].membership(p)],
             [0.7, income.terms['M'].membership(i), payment.terms['H'].membership(p)],
             [0.75, income.terms['M'].membership(i), payment.terms['VH'].membership(p)],
             [0.55, income.terms['M'].membership(i), payment.terms['VL'].membership(p)],
             [0.5, income.terms['M'].membership(i), payment.terms['M'].membership(p), age.terms['L'].membership(a)],
             [0.7, income.terms['M'].membership(i), payment.terms['M'].membership(p), age.terms['M'].membership(a)],
             [0.75, income.terms['M'].membership(i), payment.terms['M'].membership(p), age.terms['H'].membership(a)],
             [0.4, income.terms['M'].membership(i), payment.terms['L'].membership(p), experience.terms['VL'].membership(e)],
             [0.45, income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['L'].membership(e)],
             [0.55, income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['M'].membership(e)],
             [0.58, income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['H'].membership(e)],
             [0.55, income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['VH'].membership(e), age.terms['M'].membership(a)],
             [0.75, income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['VH'].membership(e), age.terms['H'].membership(a)],
             ]
    rules = [[0.15, min(income.terms['L'].membership(i), payment.terms['VL'].membership(p))],
             [0.2, min(income.terms['L'].membership(i), payment.terms['L'].membership(p))],
             [0.25, min(income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['VL'].membership(e))],
             [0.3, min(income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['L'].membership(e))],
             [0.35, min(income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['M'].membership(e))],
             [0.4, min(income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['H'].membership(e))],
             [0.58, min(income.terms['L'].membership(i), payment.terms['M'].membership(p), experience.terms['VH'].membership(e))],
             [0.4, min(income.terms['L'].membership(i), payment.terms['H'].membership(p), age.terms['L'].membership(a))],
             [0.5, min(income.terms['L'].membership(i), payment.terms['H'].membership(p), age.terms['M'].membership(a))],
             [0.6, min(income.terms['L'].membership(i), payment.terms['H'].membership(p), age.terms['H'].membership(a))],
             [0.4, min(income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['VL'].membership(e))],
             [0.45, min(income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['L'].membership(e))],
             [0.5, min(income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['M'].membership(e))],
             [0.7, min(income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['H'].membership(e))],
             [0.75, min(income.terms['L'].membership(i), payment.terms['VH'].membership(p), experience.terms['VH'].membership(e))],
             [0.9, income.terms['VH'].membership(i)],
             [0.8, min(income.terms['H'].membership(i), age.terms['M'].membership(a))],
             [0.85, min(income.terms['H'].membership(i), age.terms['H'].membership(a))],
             [0.5, min(income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['VL'].membership(p))],
             [0.53, min(income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['L'].membership(p))],
             [0.55, min(income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['M'].membership(p))],
             [0.6, min(income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['H'].membership(p))],
             [0.65, min(income.terms['H'].membership(i), age.terms['L'].membership(a), payment.terms['VH'].membership(p))],
             [0.7, min(income.terms['M'].membership(i), payment.terms['H'].membership(p))],
             [0.75, min(income.terms['M'].membership(i), payment.terms['VH'].membership(p))],
             [0.55, min(income.terms['M'].membership(i), payment.terms['VL'].membership(p))],
             [0.5, min(income.terms['M'].membership(i), payment.terms['M'].membership(p), age.terms['L'].membership(a))],
             [0.7, min(income.terms['M'].membership(i), payment.terms['M'].membership(p), age.terms['M'].membership(a))],
             [0.75, min(income.terms['M'].membership(i), payment.terms['M'].membership(p), age.terms['H'].membership(a))],
             [0.4, min(income.terms['M'].membership(i), payment.terms['L'].membership(p), experience.terms['VL'].membership(e))],
             [0.45, min(income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['L'].membership(e))],
             [0.55, min(income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['M'].membership(e))],
             [0.58, min(income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['H'].membership(e))],
             [0.55, min(income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['VH'].membership(e), age.terms['M'].membership(a))],
             [0.75, min(income.terms['M'].membership(i), payment.terms['L'].membership(p),
                     experience.terms['VH'].membership(e), age.terms['H'].membership(a))],
             ]

    output = np.array([rule[0] for rule in rules])
    input = np.array([rule[1] for rule in rules])
    result = sum(output * input) / sum(input)

    approve = 0
    if result >= 0.6:
        approve = 1
    credit_ability.term_init(result)

    return approve, result

def plot_credit(credit_ability, ability_val):
    values = [term.membership(ability_val) for term in credit_ability.terms.values()]
    labels = list(credit_ability.terms.keys())
    fig, ax = plt.subplots()
    ax.pie(x=values, labels=labels, autopct='%1.1f%%', colors=['red', 'yellow', 'green'])
    plt.show()
    return fig


def fuzzy_result(income_value, payment_value, experience_value, age_value):
    income = Ling_var('Доход')
    payment = Ling_var('Взнос')
    experinence = Ling_var('Опыт работы')
    age = Ling_var('Возраст')

    # Todo определить нечеткие числа
    income.terms['L'] = Term(b=16000, c=30000)
    income.terms['M'] = Term(a=18000, b=30000, c=55000)
    income.terms['H'] = Term(a=40000, b=70000, c=100000)
    income.terms['VH'] = Term(a=70000, b=150000)

    payment.terms['VL'] = Term(b=0, c=5)
    payment.terms['L'] = Term(a=3, b=7, c=10)
    payment.terms['M'] = Term(a=8, b=15, c=20)
    payment.terms['H'] = Term(a=15, b=25, c=30)
    payment.terms['VH'] = Term(a=25, b=40)

    experinence.terms['VL'] = Term(b=0, c=1)
    experinence.terms['L'] = Term(a=1, b=2, c=3)
    experinence.terms['M'] = Term(a=2, b=8, c=15)
    experinence.terms['H'] = Term(a=10, b=20, c=25)
    experinence.terms['VH'] = Term(a=20, b=30)

    age.terms['L'] = Term(b=20, c=25)
    age.terms['M'] = Term(a=23, b=30, c=45)
    age.terms['H'] = Term(a=35, b=55)

    credit_ability = Ling_var('Кредитоспособность')
    credit_ability.terms['Низкая'] = Term(b=0.2, c=1)
    credit_ability.terms['Средняя'] = Term(a=0, b=0.5, c=1)
    credit_ability.terms['Высокая'] = Term(a=0, b=0.8)

    input_dict = {
        income: income_value,
        payment: payment_value,
        experinence: experience_value,
        age: age_value
    }

    for key, value in input_dict.items():
        key.term_init(value)

    result_approve, credit_ability_value = fuzzy_output(income, payment, experinence, age,
                                          input_dict[income],
                                          input_dict[payment],
                                          input_dict[experinence],
                                          input_dict[age],
                                          credit_ability)

    return result_approve, credit_ability_value, credit_ability


    
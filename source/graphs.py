import matplotlib.pyplot as plt
import numpy as np

from source.settings import max_age, ages_step
from source.tools import get_username


def find_qual_of_age(ages, ages_quals):
    quals = []
    found = False

    for age in ages:
        for pair in ages_quals:
            if age <= pair[0] < age + ages_step:
                quals.append(pair[1])
                found = True
                break

        if not found:
            quals.append(0)

        found = False

    return quals


def make_age_hist(uid, ages_quals):
    ages = [age for age in range(0, max_age, ages_step)]
    quals = find_qual_of_age(ages, ages_quals)

    # Построение графика
    fig, axe = plt.subplots(1, 1)
    fig.set_facecolor('whitesmoke')
    fig.suptitle('VK Friends age distribution', size=25)

    axe.bar(ages, quals, color='teal')
    axe.set_title('User: ' + get_username(uid), size=20)
    axe.legend(['Number of friends'])

    plt.show()

# Mini Project: Generating a List of Health Promoting Behaviors Based on Personal Health History

# Introduction

This project interacts with the OpenAI API to provide a text file of health-promoting behaviors
based on user input of lifestyle, health, and family history.

<br />

# Necessary Packages and Setup

1. Before interacting with this, either as a user or developer, you must first install the `openai`
package via the terminal.

    1. If you have pip or pip3, this would be `pip install openai` or `pip3 install openai`.
    2. If you have anaconda, run `conda install -c conda-forge openai`.

2. Next, [follow the instructions at this link to generate your own API key.](https://platform.openai.com/account/api-keys)

    :exclamation: Note that you _must_ copy the key as soon as you see it. Once you close out of
    the tab, you will no longer be able to view that key again.

3. Lastly, [follow the instructions here to use environment variables in place of your key for
safety purposes.](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety).
Note that you should follow the setup instructions that aligns with your operating system.

<br />

# Generating Text File of Behaviors

1. Clone the repository from Github.
2. Navigate to the file titled `healthhistory.py`.
3. Modify the reponses to each variable in the `healthhistory.py` file based on your personal
health history.
    1. `bp` refers to blood pressure. Valid answers are `'low'`, `'normal'`, or `'high'`. Respond to this question based on what you
    were told at your last medical visit.
    2. `diabetes_father` refers to whether or not your father has/had
    diabetes. Valid answers are `'has'` or `'does not have'`.
    3. `diabetes_mother` refers to whether or not your mother has/had
    diabetes. Valid answers are `'has'` or `'does not have'`.
    4. `stress` refers to the average amount of stress you feel on a
    daily basis. Valid answers are `'low'`, `'moderate'`, or `'high'`.
    5. `exercise` refers to the average amount of exercise you engage
    in per week. Valid answers are `'low'`, `'moderate'`, or `'high'`.
    6. `health_health_issues_father` refers to whether or not your
    father has/had heart health issues. Valid answers are `'has'` or `'does not have'`.
    7. `health_health_issues_mother` refers to whether or not your
    mother has/had heart health issues. Valid answers are `'has'` or `'does not have'`.
    8. `smoking` refers to whether or not you smoke cigarettes. Valid
    answers are `does` or `does not`.

4. Once you have saved your answers, run `miniproject.py` in the code editor of your choice or
using the command `python miniproject.py` or `python3 miniproject.py` in the terminal.
5. Check the file `personal_health_advice.txt` for your personalized health-promoting behaviors.

<br />

# Modifying the tool as a Developer

1. Clone the repository from Github.
2. Navigate to the file titled `healthhistory.py`. Feel free to add or remove any health variables
of your choice.
3. Navigate to the file titled `miniproject.py`. Ensure you edit the `generate_prompt()` function as
needed based on your changes to `healthhistory.py`.
4. Once you have saved your changes, run `miniproject.py` in the code editor of your choice or
using the command `python miniproject.py` or `python3 miniproject.py` in the terminal.
5. Check the file `personal_health_advice.txt` for updated personalized health-promoting behaviors.
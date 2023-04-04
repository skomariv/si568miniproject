# This file interacts with the OpenAI API in order to provide helpful tips on health-promoting
# behaviors based on a user's inputs of lifestyle and family health history
import os
import openai
import healthhistory as health

openai.api_key = os.getenv("OPENAI_API_KEY")


def check_health_history_answers():
    """
    Checks the validity of health history answers input by the user in the health history form.
    The function takes no arguments and performs a series of checks on the user's input data for
    health history. If any of the user's inputs are not valid, the function will print an error
    message asking the user to correct their response.
    Valid responses for each question are as follows:

    diabetes_father: "has" or "does not have"
    heart_health_issues_father: "has" or "does not have"
    diabetes_mother: "has" or "does not have"
    heart_health_issues_mother: "has" or "does not have"
    bp: "low", "normal", or "high"
    stress: "low", "moderate", or "high"
    exercise: "low", "moderate", or "high"
    smoking: "does" or "does not"

    Parameters: None

    Returns: True if all inputs are valid, False otherwise
    """
    questions = {
        "diabetes_father": ("has", "does not have"),
        "heart_health_issues_father": ("has", "does not have"),
        "diabetes_mother": ("has", "does not have"),
        "heart_health_issues_mother": ("has", "does not have"),
        "bp": ("low", "normal", "high"),
        "stress": ("low", "moderate", "high"),
        "exercise": ("low", "moderate", "high"),
        "smoking": ("does", "does not")
    }

    correct = True
    for question, valid_responses in questions.items():
        if getattr(health, question).strip().lower() not in valid_responses:
            print(f"Please return to healthhistory.py and fix your response to <{question}>. \
                    Valid responses are: {valid_responses}")
            correct = False

    return correct


def generate_prompt():
    """
    Generates a prompt for the user based on their input data for the health history form. The
    function generates a health promotion prompt based on the user's input data for the health
    history form. It takes no arguments and returns a formatted string that includes the user's
    answers to the health history questions. The string prompt asks for health promoting behaviors
    that a person with the given health history can adopt to prevent future health issues.
    The user's input data for each health history question is used to populate the string with
    specific information about the person's health history.

    Parameters: None

    Returns:
    str: A string containing a health promotion prompt based on the user's health history data.
    """
    return f"What are health promoting behaviors someone whose father \
        {health.diabetes_father.lower().strip()} diabetes and \
            {health.heart_health_issues_father.lower().strip()} heart health issues, \
        whose mother {health.diabetes_mother.lower().strip()} diabetes and \
            {health.heart_health_issues_mother.lower().strip()} heart \
        health issues, with {health.bp.lower().strip()} blood pressure, \
            has {health.stress.lower().strip()} stress levels, who {health.smoking.lower().strip()} \
                smoke cigarettes, and engages in {health.exercise.lower().strip()} amounts of exercise \
        can take to prevent future health issues?"


def write_txt_file(filename, text):
    """
    Writes the text to a file with the filename.

    Parameters:
        filename (str): The name of the file to write the text to.
        text (str): The text to write to the file.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        sentences = text.split('\n')
        for sentence in sentences:
            if sentence.strip():
                f.write(f"{sentence}\n")


def main():
    answer_check = check_health_history_answers()
    if answer_check:
        prompt = generate_prompt()
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.7,
            max_tokens=4000
        )['choices'][0]['text']
        # response is a dictionary, we are only interested in the text response

        write_txt_file('personal_health_advice.txt', response)


if __name__ == "__main__":
    main()

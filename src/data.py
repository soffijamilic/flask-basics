import pandas as pd


def get_questions(id=None):
    questions = pd.read_csv("data/questions.csv", header=0, index_col=0)
    if id is None:
        return questions
    else:
        return questions.loc[id]


def add_question(question):
    try:
        questions = pd.read_csv("data/questions.csv", header=0, index_col=0)
    except:
        questions = pd.DataFrame(question, index=[0])
        questions.to_csv("data/questions.csv", index=True)
        return
    question = pd.DataFrame(question, index=[questions.index.max() + 1])
    questions = pd.concat([questions, question], axis=0, ignore_index=False)
    questions.to_csv("data/questions.csv")

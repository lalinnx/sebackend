class QuizGroupObject:

    def __init__(self,

                 ) -> None:
        self.QuizGroup = []

    def addQuizGroup(self,
                     groupName: str,  # The name of the question group.
                     # The number of questions to pick from the group to display to the student.
                     pickCount: int,
                     # # The amount of points allotted to each question in the group.
                     # questionPoints: int,
                    
                     ) -> None:
        self.QuizGroup.append({
            "name": groupName,
            "pick_count": pickCount,
            # "question_points": questionPoints,
        })
    def getQuizGroup(self)->list:
        return self.QuizGroup


class QuizQuestionObject:

    def __init__(self) -> None:
        self.QuizQuestion = []  # An array of Quiz

    def addQuizQuestion(self,
                        question_name: str,  # The name of the question.
                        question_text: str,  # The text of the question.
                        # The id of the quiz group to assign the question to.
                        quiz_group_id: int,
                        # The type of question. Multiple optional fields depend upon the type of question to be used.
                        # always multiple_choice_question
                        question_type: str,
                        # The order in which the question will be displayed in the quiz in relation to other questions.
                        position: int,
                        # The maximum amount of points possible received for getting this question correct.
                        points_possible: int,
                        # The comments to display if the student answers the question correctly.
                        correct_comments: str,
                        # The comments to display if the student answers incorrectly.
                        incorrect_comments: str,
                        # The comments to display regardless of how the student answered.
                        neutral_comments: str,
                        # Used in missing word questions.  The text to follow the missing word
                        text_after_answers: str,
                        # An array of available answers to display to the student.
                        answers: list) -> None:
        self.QuizQuestion.append(
            {
                "question_name": question_name,
                "question_text": question_text,
                "quiz_group_id": quiz_group_id,
                "question_type": question_type,
                "position": position,
                "points_possible": points_possible,
                "correct_comments": correct_comments,
                "incorrect_comments": incorrect_comments,
                "neutral_comments": neutral_comments,
                "text_after_answers": text_after_answers,
                "answer": answers
            }
        )

    # Returns a list of QuizQuestion *** Only Create a single quiz question, So use loop to call canvas api ***
    def getQuizQuestion(self) -> list:
        return self.QuizQuestion


class Answer:
    def __init__(self

                 ) -> None:
        self.answer = []

    def addAnswer(self,
                  answer_text: str,  # The text of the answer.
                  # An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be 100.
                  answer_weight: int,) -> None:  # Preparing list of answer
        self.answer.append({
            "answer_text": answer_text,
            "answer_weight": answer_weight
        })

    def getAnswer(self) -> list:  # Return an list of answer
        return self.answer

from QuizObject import Answer, QuizGroupObject, QuizQuestionObject
from lexer import Lexer
from parser_ import Parser


def parse_quiz(quiz_text):

    # Tokenize the quiz text using the Lexer class
    lexer = Lexer(quiz_text)
    tokens = lexer.generate_tokens()

    # Parse the tokens using the Parser class
    parser = Parser(tokens)
    parse_tree = parser.parse()

    # Prepare the quiz group and question objects
    quiz_group = QuizGroupObject()
    quiz_question = QuizQuestionObject()
    group_id = 0

    # Loop through each group in the parse tree
    for group in parse_tree:
        group_id += 1
        question_list = group.Question

        # Add the quiz group object to the prepared_quizGroup
        quiz_group.addQuizGroup(
            groupName=group.name,
            pickCount=len(question_list),
            questionPoints=1,
            assessmentID=1
        )

        # Loop through each question in the group
        for question in question_list:
            choices = question.choice.choice
            prepared_answer = Answer()

            # Loop through each choice in the question
            for choice in choices:
                if choice == question.choice.Ans:
                    print("answer choice: ", choice)
                    prepared_answer.addAnswer(
                        answer_text=choice, answer_weight=100)
                else:
                    print("choice: ", choice)
                    prepared_answer.addAnswer(
                        answer_text=choice, answer_weight=0)

            # Add the quiz question object to the prepared_quizQuestion
            quiz_question.addQuizQuestion(
                question_name="Question"+str(group_id),
                question_text=question.name,
                quiz_group_id=group_id,
                question_type="multiple_choice_question",
                position=1,
                points_possible=1,
                correct_comments="",
                incorrect_comments="",
                neutral_comments="",
                text_after_answers="",
                answers=prepared_answer.getAnswers()
            )

    return quiz_group.getQuizGroup(), quiz_question.getQuizQuestion()
from QuizObject import QuizGroupObject, QuizQuestionObject
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
    order_id = 0

    # Loop through each group in the parse tree
    for group in parse_tree:
        order_id += 1
        
        question_list = group.Question
        if (group.name != None):
            # Add the quiz group object to the prepared_quizGroup
            quiz_group.addQuizGroup(
                groupName=group.name,
                pickCount=len(question_list),
                questionPoints=1
            )

        # Loop through each question in the group
        for question in question_list:
            count = 0
            choices = question.choice.choice
            preparedQuizQuestion = {}
            print(str(question))
            # The name of the question.
            preparedQuizQuestion['question[question_name]'] = 'Question {}'.format(order_id)
            # The text of the question.
            preparedQuizQuestion['question[question_text]'] = question.name
            if (group.name != None):
                # The id of the quiz group to assign the question to.
                preparedQuizQuestion['question[quiz_group_id]'] = 0
                # Because we dont know the group id, we need to check with the name of group name.
                preparedQuizQuestion['group_belong_to'] = group.name
            # The type of question. Multiple optional fields depend upon the type of question to be used.
            # always multiple_choice_question
            preparedQuizQuestion['question[question_type]'] = 'multiple_choice_question'
            # The maximum amount of points possible received for getting this question correct.
            preparedQuizQuestion['question[points_possible]'] = 1
            # Loop through each choice in the question
            for choice in choices:
                if choice == question.choice.Ans:
                    print("answer choice: ", choice)
                    preparedQuizQuestion[f'question[answers][{count}][answer_text]'] = choice
                    preparedQuizQuestion[f'question[answers][{count}][answer_weight]'] = 100
                else:
                    print("choice: ", choice)
                    preparedQuizQuestion[f'question[answers][{count}][answer_text]'] = choice
                    preparedQuizQuestion[f'question[answers][{count}][answer_weight]'] = 0
                count += 1

            # Add the quiz question object to the prepared_quizQuestion
            quiz_question.addQuizQuestion(
                preparedQuizQuestion=preparedQuizQuestion
            )

    return {"quiz_groups": quiz_group.getQuizGroup(), "quiz_questions": quiz_question.getQuizQuestion()}

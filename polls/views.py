from django.shortcuts import render
from .models import Question, Choice


def index(request):

    # Query all questions
    questions = Question.objects.all()

    # Render index template with questions
    return render(request, 'polls/index.html', {'questions': questions})

def vote(request,pk):

    # get question object using pk
    question = Question.objects.get(id=pk)

    # get all choices of the question
    options = question.choices.all()

    # render the vote page with question and options
    return render(request, 'polls/vote.html', {'question':question, 'options': options })

def result(request, pk):

    # Retrieve the question
    question = Question.objects.get(id=pk)

    # Get all the options
    options = question.choices.all()

    # Check if request is POST
    if request.method == 'POST':

        # Get the selected option's id
        inputvalue = request.POST['choice']

        # Retrieve the selected option
        selection_option = options.get(id=inputvalue)

        # Increment the vote count of the selected option
        selection_option.votes += 1

        # Save the changes to the selected option
        selection_option.save()

    # Render the result page    
    return render(request, 'polls/result.html', {'question': question, 'options': options})
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory



# Create your views here.
def index(request):
    llm = OpenAI(temperature=0)
    conversation = ConversationChain(llm=llm, verbose=True, memory=ConversationBufferMemory())

    chat_history = request.session.get('chat_history', [])


    if request.method == 'POST':
        user_input = request.POST.get('message')
        if user_input:
            response = conversation.predict(input=user_input)
            # chat_history = request.session.get('chat_history', [])
            chat_history.append({'You': user_input, 'bot': response})
            request.session['chat_history'] = chat_history
    return render(request, 'index.html', {'chat_history': chat_history})
        
    
    # render the page
    # return render(request, 'index.html')

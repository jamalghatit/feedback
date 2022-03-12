from django.shortcuts import render, redirect
from django.contrib import messages
# adiciona mensagens no contexto da pagina
# aparece essas mensagens na pagina quando declarado
# na pagina {% bootstrap_messages %}

from core.forms import FeedbackForms

def feedback_view(request):
    form = FeedbackForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pesquisa enviada com sucesso!')
            form = FeedbackForms()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    """
    Tudo aquilo que quiser enviar no contexto do template,
    é colocado nesse dicionário
    """
    context = {
        'form' : form
    }
    return render(request, 'feedback.html', context=context)

def sobre_view(request):
    return render(request, 'sobre.html')

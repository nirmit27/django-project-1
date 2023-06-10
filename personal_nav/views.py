from django.http import HttpResponse as response
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def analyze(request):

    params = {
        'purpose': '',
        'analyzed_text': ''
    }

    # Getting the text
    djtxt = str(request.POST.get('text', 'default text'))

    temp = djtxt

    # Checkbox values
    removepunc = str(request.POST.get('removepunc', 'off'))
    allcaps = str(request.POST.get('allcaps', 'off'))
    allsmalls = str(request.POST.get('allsmalls', 'off'))
    nlrem = str(request.POST.get('nlrem', 'off'))
    sprem = str(request.POST.get('sprem', 'off'))
    chcnt = str(request.POST.get('chcnt', 'off'))

    # Text analysis
    if removepunc == 'on':
        djtxt = djtxt.translate(str.maketrans('', '', string.punctuation))
        (params['purpose'], params['analyzed_text']) = (
            'Removed punctuations', djtxt)

    if allcaps == 'on':
        djtxt = djtxt.upper()
        (params['purpose'], params['analyzed_text']) = ('UPPERCASE', djtxt)

    if allsmalls == 'on':
        djtxt = djtxt.lower()
        (params['purpose'], params['analyzed_text']) = ('lowercase', djtxt)

    if nlrem == 'on':
        res = str()
        for x in djtxt:
            if x != '\n' and x != '\r':
                res += x
        djtxt = res
        (params['purpose'], params['analyzed_text']) = (
            'Removed newlines', djtxt)

    if sprem == 'on':
        res = str()
        for x, y in enumerate(djtxt):
            if not (djtxt[x] == ' ' and djtxt[x+1] == ' '):
                res += y
        djtxt = res
        (params['purpose'], params['analyzed_text']) = (
            'Removed extra spaces', djtxt)

    if chcnt == 'on':
        ctr = 0
        for x in djtxt:
            if x != ' ':
                ctr += 1

        if djtxt != temp:
            (params['purpose'], params[
                'analyzed_text']) = ('', f'Analyzed Text : {djtxt}\nNumber of Characters : {ctr}')
        else:
            (params['purpose'], params['analyzed_text']) = (
                'Number of Characters', f'{ctr}')

    if (chcnt == 'off' and sprem == 'off' and nlrem == 'off' and allsmalls == 'off' and allcaps == 'off' and removepunc == 'off'):
        (params['purpose'], params['analyzed_text']) = (
            'Please select any operation and try again!', djtxt)

    # Rendering the results
    return render(request, 'analyze.html', params)

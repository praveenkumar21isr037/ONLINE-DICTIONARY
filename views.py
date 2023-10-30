from django.shortcuts import render
from .models import Word

from django.shortcuts import render
from .models import Word

def words_starting_with(request, letter):
    letter = letter.lower()  # Convert to lowercase
    words = Word.objects.filter(word__istartswith=letter)
    context = {'letter': letter, 'words': words}
    return render(request, 'dictionary_app/word_list.html', context)

from django.shortcuts import redirect

def default_letter(request):
    # Redirect to the letter 'a' by default
    return redirect('words_starting_with', letter='a')
from django.shortcuts import render
from .models import Word

def alphabet_index(request):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    context = {'alphabet': alphabet}
    return render(request, 'dictionary_app/alphabet_index.html', context)

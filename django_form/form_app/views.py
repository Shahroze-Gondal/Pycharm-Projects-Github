from django.shortcuts import render, redirect
from form_app.forms import UserForm


def home_view(request):
    context = {}

    # create object of form
    form = UserForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('/')

    context['form'] = form
    return render(request, "index.html", context)

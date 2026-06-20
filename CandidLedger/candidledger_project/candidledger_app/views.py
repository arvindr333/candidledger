from django.shortcuts import render, redirect
from .models import TaxUpdate, Feedback
from .forms import ContactEnquiryForm


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):

    if request.method == 'POST':

        form_type = request.POST.get('form_type')

        # Enquiry Form
        if form_type == 'enquiry':

            form = ContactEnquiryForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('contact')

        # Feedback Form
        elif form_type == 'feedback':

            Feedback.objects.create(
                name=request.POST.get('feedback_name'),
                message=request.POST.get('feedback_message')
            )

            return redirect('contact')

    form = ContactEnquiryForm()

    return render(
        request,
        'contact.html',
        {
            'form': form
        }
    )


def tax_updates(request):

    posts = TaxUpdate.objects.filter(
        is_published=True
    ).order_by('-created_at')

    return render(
        request,
        'tax_updates.html',
        {
            'posts': posts
        }
    )



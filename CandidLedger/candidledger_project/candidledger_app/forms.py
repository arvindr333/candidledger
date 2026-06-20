from django import forms
from .models import TaxUpdate, ContactEnquiry


class TaxUpdateForm(forms.ModelForm):

    class Meta:
        model = TaxUpdate

        fields = [
            'title',
            'image',
            'short_description',
            'content',
            'meta_title',
            'meta_description',
            'is_published'
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Title'
                }
            ),

            'short_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Short Description'
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 10,
                    'placeholder': 'Full Content'
                }
            ),

            'meta_title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Meta Title'
                }
            ),

            'meta_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Meta Description'
                }
            ),

        }


class ContactEnquiryForm(forms.ModelForm):

    class Meta:
        model = ContactEnquiry

        fields = [
            'name',
            'email',
            'phone',
            'service',
            'message'
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Your Name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Your Email'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Your Phone Number'
                }
            ),

            'service': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Enter Your Message'
                }
            ),

        }




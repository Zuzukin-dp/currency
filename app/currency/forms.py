from currency.models import Analytics, ContactUs, Rate, Source

from django import forms


class RateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bank'].empty_label = "Select Bank"
        self.fields['cur_type'].empty_label = "Select Currency"

    class Meta:
        model = Rate
        fields = (
            'cur_type',
            'sale',
            'buy',
            'bank',
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'name',
            'code_name',
            'url',
            'original_url',
            'phone',
            'source_logo',

        )


class AnalyticsForm(forms.ModelForm):
    class Meta:
        model = Analytics
        fields = (
            'path',
            'counter',
            'request_method',
            'status',
        )

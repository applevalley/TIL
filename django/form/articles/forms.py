from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(max_length=150)
# from django import forms
# from .models import Article


# # class ArticleForm(forms.Form):
# #     REGION_A = 'seoul'
# #     REGION_B = 'deajeon'
# #     REGIONS = [
# #         (REGION_A, '서울'),
# #         (REGION_B, '대전'),
# #     ]


# #     title = forms.CharField(max_length=10)
# #     content = forms.CharField(widget=forms.Textarea)
# #     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)

# class ArticleForm(forms.ModelForm):
#     title = forms.CharField(
#         label='제목',
#         widget=forms.TextInput(attrs={
#             'class': 'my-title form-control',
#             'placeholder': 'Enter the title',
#             'maxlength': 10,
#         })
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(attrs={
#             'class': 'my-content form-control',
#             'rows': 5,
#             'cols': 50,
#         }),
#         error_messages={
#             'required': '내용 넣어라...'
#         }
#     )

#     class Meta:
#         model = Article
#         fields = '__all__'

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content',]


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length = 10,
#         label = '제목',
#         widget = forms.TextInput(
#             attrs = {
#                 'class': 'my-title',
#                 'placeholder': 'Enter the title',
#             }
#         )
#     )
#     content = forms.CharField(
#         label = '내용',
#         widget = forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content',
#                 'rows': 5, 
#                 'cols': 50,
#             }
#         )
#     )
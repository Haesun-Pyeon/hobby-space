# blog/forms.py
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'content', 'head_image', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목'},),
        }
        labels = {
            'title': '',
            'content': '',
            'head_image': '썸네일 사진',
            'category': '카테고리',
            'tags': '태그 선택',
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = '카테고리를 선택해주세요.'
        self.fields['tags'].empty_label = '태그를 선택해주세요. 없으면 아래에 입력해주세요. (복수선택은 컨트롤+클릭!)'


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '댓글을 입력해 주세요.', 'style': 'resize:none;'},),
        }
        labels = {
            'content': '',
        }

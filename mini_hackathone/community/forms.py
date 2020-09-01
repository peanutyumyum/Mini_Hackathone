from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        modelt = Post
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = "댓글"
        self.fields['content'].widget.attrs.update({
            'class' : 'content',
            'placeholder' : '댓글을 입력하세요'
        })

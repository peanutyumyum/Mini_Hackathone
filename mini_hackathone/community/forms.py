from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        modelt = Post
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['title'].widget.attrs.update({
            'class' : 'title',
            'placeholder' : '제목을 입력하세요'
        })        
        self.fields['content'].label = "내용"
        self.fields['content'].widget.attrs.update({
            'class' : 'content',
            'placeholder' : '내용을 입력하세요'
        })

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

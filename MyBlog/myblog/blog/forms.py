# coding = utf-8
from django import forms
"""借此完成博客的评论功能"""

class CommentForm(forms.Form):

    name = forms.CharField(max_length=16,error_messages={
        'required':'请填写您的称呼',
        'max_length':'称呼太长了'
    })
    email= forms.EmailField(error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式不正确'
    })
    content = forms.CharField(error_messages={
        'required':'请填写您的评论内容!',
        'max_length':'评论内容太长了'
    })
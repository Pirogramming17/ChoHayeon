from django import forms
from .models import Comment

# Model Form (모델 폼)
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = '__all__' # '__all__' 설정시 전체 필드 추가
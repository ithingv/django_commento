from django import forms

from blog.models import Post, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'description', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance:
            tagStr = ', '.join(t.name for t in instance.tags.all())
            self.initial.update({'tags': tagStr})

    def clean_tags(self):
        tagStr = self.cleaned_data['tags']
        tagList = []
        for s in tagStr.split(','):
            tag, _ = Tag.objects.get_or_create(name=s.strip())
            tagList.append(tag)
        return tagList

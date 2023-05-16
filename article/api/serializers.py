from rest_framework import serializers
from article.models import Article,Comment


class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='articleapi:detail',
        lookup_field='slug'
    )
    author = serializers.StringRelatedField() #Authorun tam adini gormek istersek...
    
        
    class Meta:
        model = Article
        fields = [
            'author', 
            "title", 
            "content", 
            "url", 
            "article_image", 
            "created_date"
        ]
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField() #Authorun tam adini gormek istersek...
            
        
    class Meta:
        model = Comment
        fields = '__all__'

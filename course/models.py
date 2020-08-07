from django.db import models
from django.urls import reverse
from datetime import datetime , date
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='images/profile')
    website_url=models.CharField(max_length=200,null=True,blank=True)
    facebook_url=models.CharField(max_length=200,null=True,blank=True)
    instagram_url=models.CharField(max_length=200,null=True,blank=True)
    twitter_url=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
    	return reverse('index') 


        
class 	Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
    	return reverse('blog-home')     


class Post(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='images/')
	#body=models.TextField()
	body=RichTextField(blank=True,null=True)
	post_date=models.DateField(auto_now_add=True)
	category=models.CharField(max_length=200,default='Speaking')
	likes=models.ManyToManyField(User,related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		#return reverse('detail',args=(str(self.id)))
		return reverse('blog-home') 	


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title,self.name)
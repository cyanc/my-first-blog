from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Post (models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=50, null=True, unique=True)
	text = models.TextField()
	image = models.ImageField(upload_to='images/', null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs): 
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

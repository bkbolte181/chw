from django.db import models
from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class SiteUserManager(BaseUserManager):
	"""
		Manager for SiteUser model. This replaces the default manager used by Django, since the model
		is custom. The UserManager needs two methods, create_user and create_superuser. Most other methods
		are subclassed from BaseUserManager.
	"""
    
	def _create_user(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, **extra_fields):
		if not email:
			raise ValueError('An email must be provided to create the user.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save(using=self._db)
		return user
		
	def create_user(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, **extra_fields):
		return self._create_user(email, password)
		
	def create_superuser(self, email, password, first_name=None, last_name=None, department=None, lab=None, pi=None, **extra_fields):
		return self._create_user(email, password)

class SiteUser(AbstractBaseUser):
    """
        Custom User model. Set the user model to this one in the settings.py file:
        AUTH_USER_MODEL = 'PeerReviewApp.SiteUser' # Add this variable to settings.py file
        This will tell Django to use this model as the default user model. There are a fe
        required attributes for custom user models:
            -> USERNAME_FIELD: Unique identifier for log in (in this case, email)
            -> REQUIRED_FIELDS: Required fields (update this to include required fields)
            -> get_full_name(): Return the "full name" of the user
            -> get_short_name(): Return a "short name" identifier for the user
        Additionally, this model requires a custom user manager, and some custom handlers
        for forms to replace the built-ins that Django provides.
    """

    email = models.EmailField('email address', max_length=200, unique=True,
        error_messages={
            'unique': 'A user with that email already exists.',
        }, help_text="Emory Email Address")

    first_name = models.CharField(max_length=100, help_text="First Name")
    last_name = models.CharField(max_length=100, help_text="Last Name")

    # User Type: Student or Teacher
    user_type = models.CharField(max_length=100, help_text="Student or Teacher")

    # Custom user manager
    objects = SiteUserManager()

    # Semantic elements required for custom user model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def get_full_name(self): return self.first_name, self.last_name
    def get_short_name(self): return self.first_name

class Section(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='teacher_sections', related_query_name='teacher_section', default=0)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='student_sections', related_query_name='student_section', default=0)
    enrollment_number = models.CharField(max_length=100, help_text='Enrollment Number')
    
class Assignment(models.Model):
    title = models.CharField(max_length=100, help_text='Assignment Name')
    description = models.CharField(max_length=1000, help_text='Assignment Description')
    section = models.ForeignKey('Section', related_name='assignments', related_query_name='assignment', default=0)
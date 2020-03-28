from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models
from datetime import date

class UserManager(auth_models.BaseUserManager):
  
    def create_user(self, username, first_name, 
                        last_name, dob, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.dob = dob
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, first_name, 
                        last_name, dob, email, password ) :

        user = self.create_user(username=username, first_name=first_name, 
                                last_name=last_name, dob=dob, 
                                email=email, password=password)

        user.is_superuser = user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    dob = models.DateField(
        _('date of birth')
    )
    email = models.EmailField(
		_('email address'),
		unique=True,
		blank=True
	)
    cellphone = models.CharField(
		_('cell phone'),
		max_length=20,
		null=True, blank=True
	)

    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'dob']

    class Meta:
        verbose_name = 'Organizer / Participant'
        verbose_name_plural = 'Organizers / Participants'
        ordering = ('id', )

    def get_age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def __unicode__(self):
        return u'{0} ({1})'.format(self.get_full_name(), self.email)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

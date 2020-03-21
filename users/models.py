from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
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

    class Meta:
        verbose_name = 'Organizer / Participant'
        verbose_name_plural = 'Organizers / Participants'
        ordering = ('id', )

    def get_age(self):
        today = date.today()

        try:
            birthday = self.dob.replace(year=today.year)
        # raised February 29
        except ValueError:
            birthday = self.dob.replace(year=today.year, day=born.day-1)

        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    def __unicode__(self):
        return u'{0} ({1})'.format(self.get_full_name(), self.email)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

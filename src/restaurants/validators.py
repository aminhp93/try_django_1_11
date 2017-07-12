from django.core.exceptions import ValidationError

def validate_even(value):
	if value % 2 != 0:
		raise ValidationError(
				'%(value)s is not an even number',
				params={'value': value},
			)

def clean_email(self):
	email = self.cleaned_data.get("email")
	if ".edu" in email:
		raise ValidationError("We do not accept edu emails")
	return email

CATEGORIES = ['Mexican', 'Asian', "American", 'Pizza']

def validate_category(value):
	cat = value.capitalize()
	if not value in CATEGORIES and not cat in CATEGORIES:
		raise ValidationError("{} is not a valid category".format(value))

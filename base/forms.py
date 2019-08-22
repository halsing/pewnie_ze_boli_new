from django import forms

CONTACT_CHOICE = [
	('Email', 'Email',),
	('Telefon', 'Telefon',),
]

TATOO_MAKER_CHOICE = [
	('Crystal Skull', 'Crystal Skull'),
	('Bima', 'Bima'),
	('Heksa Beksa', 'Heksa Beksa'),
	('Dziaria Antonina', 'Dziaria Antonina'),
	('Ola Piekło','Ola Piekło'),
	('Sana Ink','Sana Ink'),
	('Ink Von D','Ink Von D'),
	('Iza Byczyńska','Iza Byczyńska'),
	("Jakub JW TTT'S ","Jakub JW TTT'S "),
	('Brocat','Brocat'),
	('Waleria Piercing','Waleria Piercing'),
]

class ContactForm(forms.Form):

	name = forms.CharField(
		max_length=40 ,
		label='Imię',
		widget=forms.TextInput(attrs={
									'class':'form-control col-12',
									'placeholder':'np. Janusz Kowalski',
									}))

	from_email = forms.EmailField(
		required=True,
		label='Email',
		widget=forms.EmailInput(attrs={
									'class':'form-control',
									'placeholder':'np. Janusz98@sexfotka.pl',
									}))

	phone_number = forms.CharField(
		max_length=20,
		label='Numer kontaktowy',
		widget=forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'np. 666 666 666',
									}))

	preferred_contact = forms.ChoiceField(
		choices=CONTACT_CHOICE,
		widget=forms.RadioSelect(),
		label='Preferowany rodzaj kontaktu ',)

	tatoo_place = forms.CharField(
		max_length=30,
		label='Miejsce tatuażu',
		widget=forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'np. Pośladek',
									}))

	tatoo_size = forms.CharField(
		max_length=20,
		label='Wielkość tatuażu',
		widget=forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'np. 5/20 cm',
									}))

	tatoo_maker = forms.ChoiceField(
		choices=TATOO_MAKER_CHOICE,
		label='Tatuator / Piercer')

	description = forms.CharField(
		widget=forms.Textarea(
			attrs={'class':'form-control',
				'width':'80%' ,
				'cols': '40',
				'placeholder':'np. Chciałbym motylka z \
				trupią czaszką na płonącej róży'}),
		label='Opisz co byś chciał/a' )

	attach = forms.FileField(required=False,
		label='Prześlij plik',
		widget=forms.ClearableFileInput(attrs={
											'class':'form-control',
											'multiple': True
                                            }))
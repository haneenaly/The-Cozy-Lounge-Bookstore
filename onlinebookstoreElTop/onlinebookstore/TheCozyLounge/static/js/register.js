document.querySelector('[name="username"]').placeholder = 'Username..';
		document.querySelector('[name="email"]').placeholder = 'Email..';
		document.querySelector('[name="password1"]').placeholder = 'Enter password...';
		document.querySelector('[name="password2"]').placeholder = 'Re-enter password...';

		const form_fields = document.querySelectorAll('input');
		form_fields.forEach(field => {
			field.classList.add('form-control');
		});
#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('/home/david-mk/Documents/Sytème_bancaire')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_system.settings')

# Setup Django
django.setup()

from accounts.models import CustomUser
from django.contrib.auth.hashers import check_password

def test_passwords():
    try:
        test_user = CustomUser.objects.get(username='testuser')
        print('Test user found')
        passwords = ['admin', 'admin123', 'password', '123456', 'admin1234', 'furie', 'bank', 'test', 'test123', 'testuser', '123456789', 'qwerty', 'abc123']
        for pwd in passwords:
            if check_password(pwd, test_user.password):
                print(f'PASSWORD FOUND: {pwd}')
                return pwd
        print('No common password found')
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    test_passwords()
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms.settings")
import django
django.setup()

from django.contrib.auth import get_user_model
from selection.models import Warden, Hostel

User = get_user_model()

# Step 1: Delete existing Wardens
print("Deleting existing wardens...")
Warden.objects.all().delete()

# Step 2: Delete users who are wardens (is_warden=True but not superuser)
User.objects.filter(is_warden=True, is_superuser=False).delete()

# Step 3: Create a dummy hostel (if none exist)
if not Hostel.objects.exists():
    hostel = Hostel.objects.create(name='Mens Hostel', gender='M')
else:
    hostel = Hostel.objects.first()

# Step 4: Create fresh warden users + Warden profiles
print("Creating new wardens...")
for i in range(1, 3):
    username = f'warden{i}'
    user = User.objects.create_user(
        username=username,
        password=f'password',
        email=f'{username}@example.com',
        is_warden=True
    )
    Warden.objects.create(
        user=user,
        name=f'Warden {i}',
        hostel=hostel
    )

print("✅ New wardens created successfully.")

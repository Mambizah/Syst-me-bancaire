# Generated migration for updating ATM locations to Togo (Lome)

from django.db import migrations

def update_atm_locations(apps, schema_editor):
    """Update ATM locations to Lome, Togo with proper coordinates"""
    ATM = apps.get_model('atm', 'ATM')
    
    # Update GAB Centre - Lome 1
    atm1 = ATM.objects.filter(id=1).first()
    if atm1:
        atm1.name = "GAB Centre Lomé"
        atm1.city = "Lomé"
        atm1.address = "Boulevard du 13 Janvier, Centre-Ville"
        atm1.latitude = 6.125056  # Coordinates for Lome center
        atm1.longitude = 1.234608
        atm1.save()
    
    # Update GAB Gare - Lome 2
    atm2 = ATM.objects.filter(id=2).first()
    if atm2:
        atm2.name = "GAB Quartier du Port"
        atm2.city = "Lomé"
        atm2.address = "Rue de la Gare, Quartier du Port"
        atm2.latitude = 6.120000  # Coordinates for Port area
        atm2.longitude = 1.240000
        atm2.save()

def reverse_update(apps, schema_editor):
    """Reverse the update if needed"""
    ATM = apps.get_model('atm', 'ATM')
    
    atm1 = ATM.objects.filter(id=1).first()
    if atm1:
        atm1.name = "GAB Centre"
        atm1.city = "Paris"
        atm1.address = "123 Rue Principale"
        atm1.latitude = 48.8566
        atm1.longitude = 2.3522
        atm1.save()
    
    atm2 = ATM.objects.filter(id=2).first()
    if atm2:
        atm2.name = "GAB Gare"
        atm2.city = "Lyon"
        atm2.address = "456 Avenue de la Gare"
        atm2.latitude = 45.7640
        atm2.longitude = 4.8357
        atm2.save()

class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_atm_locations, reverse_update),
    ]

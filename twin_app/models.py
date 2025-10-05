from django.db import models

# Create your models here.
class PatientProfile(models.Model):
    # 1. Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)

    age = models.IntegerField()
    sex = models.CharField(max_length=10) # We'll store 'male', 'female', 'other'
    height_cm = models.FloatField()
    weight_kg = models.FloatField()
    waist_cm = models.FloatField(null=True, blank=True) # Optional field

    # 2. Vital & Physical Activity Data
    steps_last_24h = models.IntegerField()
    activity_minutes = models.IntegerField()
    sleep_hours_last_24h = models.FloatField()
    water_intake_liters = models.FloatField()
    calories_intake_last_24h = models.IntegerField(null=True, blank=True) # Optional

    # 3. Lifestyle & Habits
    diet_quality_score = models.IntegerField()
    smoking_status = models.CharField(max_length=20) # e.g., 'never', 'former', 'current'
    alcohol_units_week = models.IntegerField(null=True, blank=True) # Optional

    # 4. Medical Background
    medications = models.TextField(blank=True) # Storing as comma-separated text
    known_conditions = models.TextField(blank=True) # Storing as comma-separated text
    menstrual_cycle_phase = models.CharField(max_length=20, null=True, blank=True) # Optional

    # 5. Mental & Emotional Health
    mood_score = models.IntegerField()
    stress_score = models.IntegerField()
    
    # Auto-generated timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - Age {self.age}"
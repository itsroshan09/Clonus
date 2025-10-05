# twin_app/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import PatientProfile
from .health_logic import calculate_health_score, get_recommendations

# ... (index_page view remains the same) ...
def index_page(request):
    return render(request, 'app_home.html')

# ... (register_user view is already correct) ...
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # (Your data cleaning and saving logic)
            waist_cm_val = data.get('waist_cm')
            calories_val = data.get('calories_intake_last_24h')
            alcohol_val = data.get('alcohol_units_week')
            waist_cm = waist_cm_val if waist_cm_val else None
            calories = calories_val if calories_val else None
            alcohol = alcohol_val if alcohol_val else None
            
            profile = PatientProfile(
                full_name=data.get('full_name'),
                email=data.get('email'),
                age=data.get('age'),
                sex=data.get('sex'),
                height_cm=data.get('height_cm'),
                weight_kg=data.get('weight_kg'),
                waist_cm=waist_cm,
                steps_last_24h=data.get('steps_last_24h'),
                activity_minutes=data.get('activity_minutes'),
                sleep_hours_last_24h=data.get('sleep_hours_last_24h'),
                water_intake_liters=data.get('water_intake_liters'),
                calories_intake_last_24h=calories,
                diet_quality_score=data.get('diet_quality_score'),
                smoking_status=data.get('smoking_status'),
                alcohol_units_week=alcohol,
                medications=', '.join(data.get('medications', [])),
                known_conditions=', '.join(data.get('known_conditions', [])),
                menstrual_cycle_phase=data.get('menstrual_cycle_phase'),
                mood_score=data.get('mood_score'),
                stress_score=data.get('stress_score')
            )
            profile.save()
            
            return JsonResponse({
                'status': 'success',
                'redirect_url': f'/dashboard/{profile.id}/'
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error saving profile: {e}'}, status=400)

    return render(request, 'register.html')


# ... (dashboard_list view remains the same) ...
def dashboard_list(request):
    all_profiles = PatientProfile.objects.all().order_by('-created_at')
    context = {'profiles': all_profiles}
    return render(request, 'dashboard_list.html', context)


# --- VIEW TO UPDATE ---
def update_user(request, profile_id):
    profile = PatientProfile.objects.get(id=profile_id)

    if request.method == 'POST':
        # THIS IS THE KEY CHANGE: We now read JSON data, just like in register_user
        data = json.loads(request.body)
        
        # Update the profile fields with the new data from the JSON
        profile.full_name = data.get('full_name')
        profile.age = data.get('age')
        profile.sex = data.get('sex')
        profile.height_cm = data.get('height_cm')
        profile.weight_kg = data.get('weight_kg')
        profile.waist_cm = data.get('waist_cm') or None
        profile.steps_last_24h = data.get('steps_last_24h')
        profile.activity_minutes = data.get('activity_minutes')
        profile.sleep_hours_last_24h = data.get('sleep_hours_last_24h')
        profile.water_intake_liters = data.get('water_intake_liters')
        profile.calories_intake_last_24h = data.get('calories_intake_last_24h') or None
        profile.diet_quality_score = data.get('diet_quality_score')
        profile.smoking_status = data.get('smoking_status')
        profile.alcohol_units_week = data.get('alcohol_units_week') or None
        # Handle lists correctly when updating
        profile.medications = ', '.join(data.get('medications', []))
        profile.known_conditions = ', '.join(data.get('known_conditions', []))
        profile.menstrual_cycle_phase = data.get('menstrual_cycle_phase')
        profile.mood_score = data.get('mood_score')
        profile.stress_score = data.get('stress_score')
        
        profile.save()
        
        # Send back a JSON response, which the JavaScript will handle
        return JsonResponse({
            'status': 'success',
            'redirect_url': f'/dashboard/{profile.id}/'
        })

    # For a GET request, the logic is the same: show the pre-filled form
    context = {'profile': profile}
    return render(request, 'register.html', context)


# ... (profile_dashboard view remains the same) ...
def profile_dashboard(request, profile_id):
    try:
        profile = PatientProfile.objects.get(id=profile_id)
        
        # Calculate health score and reasons dynamically
        health_data = calculate_health_score(profile)
        health_score = health_data['score']
        reasons = health_data['reasons']

        # Get AI-generated recommendations
        recommendations = get_recommendations(profile)

        # --- Doctor Recommendations (Qualification only, no name) ---
        doctor_recommendations = []
        for reason in reasons:
            text_lower = reason['text'].lower()
            
            if "blood pressure" in text_lower or "cardio" in text_lower or "heart" in text_lower:
                doctor_recommendations.append({
                    'title': "Consult a Cardiologist (MD Cardiology)",
                    'details': f"Reason: {reason['text']}. Your cardiovascular indicators suggest consulting a cardiologist."
                })
            elif "blood sugar" in text_lower or "diabetes" in text_lower or "glucose" in text_lower:
                doctor_recommendations.append({
                    'title': "Consult an Endocrinologist (MD Endocrinology)",
                    'details': f"Reason: {reason['text']}. Based on your glucose or metabolic indicators, an endocrinologist consultation is advised."
                })
            elif "stress" in text_lower or "mental" in text_lower or "anxiety" in text_lower:
                doctor_recommendations.append({
                    'title': "Consult a Psychologist (M.Psych, PhD Clinical Psychology)",
                    'details': f"Reason: {reason['text']}. Your mood or stress scores indicate that consulting a psychologist would be beneficial."
                })
            elif "weight" in text_lower or "diet" in text_lower or "nutrition" in text_lower:
                doctor_recommendations.append({
                    'title': "Consult a Nutritionist (M.Sc Nutrition & Dietetics)",
                    'details': f"Reason: {reason['text']}. A nutritionist can help optimize your diet and lifestyle."
                })
            else:
                doctor_recommendations.append({
                    'title': "Consult a General Physician (MBBS, MD)",
                    'details': f"Reason: {reason['text']}. A general checkup is recommended to address this issue."
                })

        # Context to pass to template
        context = {
            'profile': profile,
            'health_score': health_score,
            'reasons': reasons,
            'recommendations': recommendations,
            'doctor_recommendations': doctor_recommendations
        }

        return render(request, 'dashboard.html', context)

    except PatientProfile.DoesNotExist:
        return redirect('dashboard_list')

def roshan_demo_view(request):
    """
    Renders the static health trajectory demo page for Roshan.
    This view doesn't need to pass any data because the demo is self-contained.
    """
    return render(request, 'roshan_demo.html')

def landing_page(request):
    """
    Renders the main project landing page (the new index.html).
    """
    return render(request, 'index.html')   

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def send_email(request, email):
    # Fetch the profile by email
    profile = get_object_or_404(PatientProfile, email=email)

    # Calculate health score and recommendations dynamically
    health_data = calculate_health_score(profile)
    health_score = health_data['score']
    reasons = health_data['reasons']
    recommendations = get_recommendations(profile)

    # Render HTML template as string
    html_content = render_to_string('email_dashboard.html', {
        'profile': profile,
        'health_score': health_score,
        'reasons': reasons,
        'recommendations': recommendations
    })

    # Fallback plain text
    text_content = strip_tags(html_content)

    subject = "Your Digital Twin Health Report"
    email_message = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email="clonus.healthsystem@example.com",
        to=[profile.email]
    )

    email_message.attach_alternative(html_content, "text/html")
    email_message.send(fail_silently=False)

    messages.success(request, f"Email sent successfully to {profile.email}")
    return redirect('profile_dashboard', profile_id=profile.id)

def delete_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(PatientProfile, id=user_id)
        user.delete()
        messages.success(request, f"User {user.full_name} deleted successfully!")
    return redirect('dashboard_list')  # redirect to dashboard after deletion

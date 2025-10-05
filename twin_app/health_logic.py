# twin_app/health_logic.py

def calculate_health_score(profile):
    score = 100
    reasons = []

    # BMI Calculation
    try:
        height_m = profile.height_cm / 100
        bmi = profile.weight_kg / (height_m * height_m)
        if bmi >= 25:
            score -= 15
            reasons.append({'severity': 'high', 'text': f"Your BMI of {bmi:.1f} is in the overweight range, which can strain your joints and increase cardiovascular risk."})
        elif bmi < 18.5:
             score -= 15
             reasons.append({'severity': 'high', 'text': f"Your BMI of {bmi:.1f} is in the underweight range. It's important to ensure you're getting enough nutrients."})
    except (ZeroDivisionError, TypeError):
        pass

    # Sleep Scoring
    if profile.sleep_hours_last_24h < 6:
        score -= 20
        reasons.append({'severity': 'high', 'text': "Getting less than 6 hours of sleep can significantly impair cognitive function and recovery."})
    elif profile.sleep_hours_last_24h < 7:
        score -= 10
        reasons.append({'severity': 'medium', 'text': "While not critical, consistently getting 7-9 hours of sleep improves long-term health outcomes."})
        
    # Activity Scoring
    if profile.steps_last_24h < 5000:
        score -= 15
        reasons.append({'severity': 'high', 'text': "A daily step count under 5,000 is considered sedentary and is a major risk factor for chronic diseases."})

    # Smoking Status
    if profile.smoking_status == 'current':
        score -= 25
        reasons.append({'severity': 'critical', 'text': "Smoking is the single most significant negative factor, impacting nearly every organ in your body."})
        
    # Stress Score
    if profile.stress_score > 7:
        score -= 10
        reasons.append({'severity': 'medium', 'text': "Chronic high stress can disrupt sleep, affect mood, and contribute to cardiovascular issues."})

    final_score = max(0, score)
    return {'score': int(final_score), 'reasons': reasons}


def get_recommendations(profile):
    tips = []
    
    # Each tip is a dictionary with an icon, title, and details.
    if profile.steps_last_24h < 7500:
        tips.append({
            "icon": "fa-solid fa-person-walking",
            "title": "Increase Your Daily Movement",
            "details": "Aim for at least 7,500 steps a day. A simple 30-minute brisk walk can help you reach this goal and significantly boost your cardiovascular health."
        })
    if profile.water_intake_liters < 2:
        tips.append({
            "icon": "fa-solid fa-glass-water",
            "title": "Focus on Hydration",
            "details": "Drinking at least 2 liters (about 8 glasses) of water a day is essential for energy levels, brain function, and overall wellness. Carry a reusable bottle as a reminder."
        })
    if profile.diet_quality_score < 60:
        tips.append({
            "icon": "fa-solid fa-leaf",
            "title": "Enhance Your Diet Quality",
            "details": "Incorporate more whole foods like fruits, vegetables, and lean proteins. Reducing processed foods and sugary drinks can have a massive impact on your energy."
        })
    if profile.sleep_hours_last_24h < 7:
        tips.append({
            "icon": "fa-solid fa-bed",
            "title": "Prioritize Consistent Sleep",
            "details": "Target 7-9 hours of quality sleep per night. Create a relaxing bedtime routine and avoid screens an hour before bed to improve your sleep quality."
        })
    if profile.stress_score > 5:
        tips.append({
            "icon": "fa-solid fa-brain",
            "title": "Manage Your Stress Levels",
            "details": "Practice mindfulness or short meditation sessions for 5-10 minutes a day. Taking brief walks can also be highly effective at reducing stress hormones."
        })
        
    return tips
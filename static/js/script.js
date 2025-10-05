document.addEventListener('DOMContentLoaded', function() {
    const nextButtons = document.querySelectorAll('.btn-next');
    const backButtons = document.querySelectorAll('.btn-back');
    const form = document.getElementById('digitalTwinForm');
    const progressSteps = document.querySelectorAll('.progress-step');
    const progressLine = document.querySelector('.progress-bar .progress-line');
    const formCards = document.querySelectorAll('.form-card');
    
    let currentStep = 1;

    // --- EVENT LISTENERS for Next/Back Buttons ---
    nextButtons.forEach(button => {
        button.addEventListener('click', () => {
            // The validation is key. If it fails, we don't proceed.
            if (validateStep(currentStep)) {
                currentStep++;
                updateFormSteps();
                updateProgressBar();
            }
        });
    });

    backButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentStep--;
            updateFormSteps();
            updateProgressBar();
        });
    });
    
    // --- FULL FORM SUBMISSION LOGIC (Restored) ---
    form.addEventListener('submit', async (e) => {
        // This line is CRITICAL. It stops the browser from trying to submit the form on its own.
        e.preventDefault();

        if (!validateStep(currentStep)) {
            return;
        }

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            // Handle lists from comma-separated strings
            if (key === 'known_conditions' || key === 'medications') {
                data[key] = value.split(',').map(item => item.trim()).filter(item => item);
            } else {
                data[key] = value;
            }
        });
        
        // Remove CSRF token from data object before sending
        delete data['csrfmiddlewaretoken'];
        
        console.log('Submitting data:', data);

        try {
            // We use the form's 'action' attribute as the URL
            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            handleSubmissionResult(result);
        } catch (error) {
            console.error('Error submitting form:', error);
            handleSubmissionResult({ status: 'error', message: 'An unexpected error occurred.' });
        }
    });

    // Conditional logic for gender field
    const sexSelect = document.getElementById('sex');
    const menstrualCycleGroup = document.getElementById('menstrual-cycle-group');
    // Ensure correct state on page load for edits
    if (sexSelect.value === 'female') {
        menstrualCycleGroup.style.display = 'block';
    }
    sexSelect.addEventListener('change', (e) => {
        if (e.target.value === 'female') {
            menstrualCycleGroup.style.display = 'block';
        } else {
            menstrualCycleGroup.style.display = 'none';
        }
    });
    
    // --- HELPER FUNCTIONS ---
    function updateFormSteps() {
        formCards.forEach(card => {
            card.classList.remove('active');
        });
        document.querySelector(`.form-card[data-step="${currentStep}"]`).classList.add('active');
    }

    function updateProgressBar() {
        progressSteps.forEach((step, index) => {
            if (index < currentStep) {
                step.classList.add('active');
            } else {
                step.classList.remove('active');
            }
        });
        
        const activeSteps = document.querySelectorAll('.progress-step.active');
        const progressWidth = ((activeSteps.length - 1) / (progressSteps.length - 1)) * 100;
        progressLine.style.width = `${progressWidth}%`;
    }

    function validateStep(step) {
        const currentCard = document.querySelector(`.form-card[data-step="${step}"]`);
        const inputs = currentCard.querySelectorAll('input[required], select[required]');
        let isValid = true;
        
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                input.style.borderColor = '#c62828'; // error color
            } else {
                input.style.borderColor = ''; // reset
            }
        });
        return isValid;
    }
    
    // This function now handles the final result for both create and update
    function handleSubmissionResult(result) {
        if (result.status === 'success' && result.redirect_url) {
            // Redirect the user to their dashboard page
            window.location.href = result.redirect_url;
        } else {
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = result.message || 'An unexpected error occurred.';
            resultDiv.className = 'result-message error';
        }
    }
    
    updateProgressBar();
});
from django.shortcuts import render
from .forms import BMICalculatorForm

def calculate_bmi(request):
    if request.method == 'POST':
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height'] / 100  
            weight = form.cleaned_data['weight']
            bmi = weight / (height * height)
            bmi=round(bmi,2)
            bmi_status = get_bmi_status(bmi)
            return render(request, 'result.html', {'bmi': bmi, 'bmi_status': bmi_status})
    else:
        form = BMICalculatorForm()
    return render(request, 'bmi_calculator.html', {'form': form})

def get_bmi_status(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    else:
        return 'Overweight'

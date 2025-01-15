from django.shortcuts import render

# Create your views here.






# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import SurveyForm
# import pandas as pd
# import os

# # Define the path for the Excel file
# EXCEL_FILE_PATH = 'survey_responses.xlsx'

# def survey_view(request):
#     if request.method == 'POST':
#         form = SurveyForm(request.POST)
        
#         if form.is_valid():
#             # Collecting the responses
#             responses = {}
#             total_score = 0  # Initialize the total score variable
            
#             # Skip the first four fields (name, phone, email, unit) and sum only survey responses
#             for field in form:
#                 if field.name not in ['Name', 'Phone Number', 'Gmail', 'Unit']:
#                     answer = form.cleaned_data.get(field.name)
#                     responses[field.label] = answer  # Save the answer with the question label
#                     total_score += answer  # Add the answer (numeric value) to the total score
            
#             # Get the user's name, unit, and total score
#             name = form.cleaned_data.get('Name')
#             unit = form.cleaned_data.get('Unit', 'N/A')  # Default to 'N/A' if no unit is provided
            
#             # Create or load the Excel file
#             if os.path.exists(EXCEL_FILE_PATH):
#                 # Load the existing Excel file if it exists
#                 df = pd.read_excel(EXCEL_FILE_PATH)
#             else:
#                 # Create a new DataFrame if the Excel file doesn't exist
#                 df = pd.DataFrame(columns=['Name', 'Unit', 'Total Score'])

#             # Append the new row (user's data) to the DataFrame
#             new_data = {'Name': name, 'Unit': unit, 'Total Score': total_score}
#             df = df.append(new_data, ignore_index=True)
            
#             # Save the DataFrame back to the Excel file
#             df.to_excel(EXCEL_FILE_PATH, index=False)

            
#             return render(request, 'survey_result.html', {'responses': responses, 'total_score': total_score})
    
#     else:
#         form = SurveyForm()

#     return render(request, 'survey_form.html', {'form': form})

















from django.shortcuts import render
from django.http import HttpResponse
from .forms import SurveyForm
import pandas as pd
import os

# Define the path for the Excel file
EXCEL_FILE_PATH = 'survey_responses.xlsx'

def calculate_category(total_score):
    """
    Calculate the category based on the total score.
    """
    if total_score >= 28:
        return "Extremely Severe"
    elif total_score >= 21:
        return "Severe"
    elif total_score >= 14:
        return "Moderate"
    elif total_score >= 10:
        return "Mild"
    else:
        return "Normal"

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        
        if form.is_valid():
            # Collecting the responses
            responses = {}
            total_score = 0  # Initialize the total score variable
            
            # Skip the first four fields (name, phone, email, unit) and sum only survey responses
            for field in form:
                if field.name not in ['name', 'number', 'email', 'unit']:
                    answer = form.cleaned_data.get(field.name)
                    responses[field.label] = answer
                    numeric_answer = int(answer)
                    total_score += numeric_answer# Save the answer with the question label
                     # Add the answer (numeric value) to the total score
            
            # Get the user's name, unit, and total score
            name = form.cleaned_data.get('name')
            unit = form.cleaned_data.get('unit', 'N/A')  # Default to 'N/A' if no unit is provided
            category = calculate_category(total_score)  # Calculate the category based on the total score

            # Create or load the Excel file
            if os.path.exists(EXCEL_FILE_PATH):
                # Load the existing Excel file if it exists
                df = pd.read_excel(EXCEL_FILE_PATH)
            else:
                # Create a new DataFrame if the Excel file doesn't exist
                df = pd.DataFrame(columns=['Name', 'Unit', 'Total Score', 'Category'])

            # Append the new row (user's data) to the DataFrame
            new_data = {'Name': name, 'Unit': unit, 'Total Score': total_score, 'Category': category}
            # df = df.append(new_data, ignore_index=True)
            new_row = pd.DataFrame([new_data])  # Convert new data into a DataFrame
            df = pd.concat([df, new_row], ignore_index=True)  # Concatenate the new row

            # Save the DataFrame back to the Excel file
            df.to_excel(EXCEL_FILE_PATH, index=False)

            # Render the result page
            return render(request, 'thanks.html', {'responses': responses, 'total_score': total_score, 'category': category})
    
    else:
        form = SurveyForm()

    return render(request, 'survey_form.html', {'form': form})

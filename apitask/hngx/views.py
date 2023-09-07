from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Get current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Get current UTC time
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs
    github_file_url = "https://github.com/liferacer333/hngx-backend/blob/main/apitask/manage.py"
    github_repo_url = "https://github.com/liferacer333/hngx-backend"

    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response)


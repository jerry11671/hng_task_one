from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timezone

@api_view(['GET',])
def index(request):
    data = {
        "slack_name": request.GET['slack_name'],
        "current_day": datetime.now().strftime('%A'),
        "utc_time": datetime.now(timezone.utc),
        "track": request.GET['track'],
        "github_file_url": "good",
        "github_repo_url": "https://github.com/jerry11671/hng_task_one.git",
        "status_code": 200
    }

    return Response(data)
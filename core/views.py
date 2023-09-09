from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import pytz

@api_view(['GET',])
def index(request):
    current_time = datetime.now(pytz.utc)

    data = {
        "slack_name": request.GET['slack_name'],
        "current_day": datetime.now().strftime('%A'),
        "utc_time": current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": request.GET['track'],
        "github_file_url": "https://github.com/jerry11671/hng_task_one/tree/main/core/view.py",
        "github_repo_url": "https://github.com/jerry11671/hng_task_one.git",
        "status_code": 200
    }

    return Response(data)
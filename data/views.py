import pandas as pd
from django.shortcuts import redirect, render

from .models import Purchase


def dashboard(request):
    query = Purchase.objects.all().values()
    df = pd.DataFrame.from_dict(query)
    df['date'] = pd.to_datetime(df['date'],
                                errors='coerce')
    df['week'] = df['date'].dt.week
    muestra = df.head()
    return render(request, 'data/dashboard.html', {
        "muestra": muestra.to_html,
        'df': df.to_html
    })

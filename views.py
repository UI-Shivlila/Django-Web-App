import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from django.shortcuts import render, redirect
from .forms import UploadFileForm

def home(request):
    return redirect('upload_file')

def upload_file(request):
    context = {'form': UploadFileForm()}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)

            summary_stats = df.describe().to_html()
            missing_values = df.isnull().sum().reset_index().to_html(index=False)
            first_rows = df.head().to_html()

            # Generate a histogram
            img = io.BytesIO()
            sns.histplot(df.select_dtypes(include=[np.number]).melt(), kde=True)
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()

            context.update({
                'data': first_rows,
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'plot_url': plot_url
            })
    return render(request, 'analysis/upload.html', context)

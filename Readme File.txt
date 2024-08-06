## This project is a Django-based web application that allows user to upload CSV file,
perform data analysis using pandas and numpy for data analysis and visualization. 
User can upload CSV files and receive immediate insights and visual feedback on their data.


## Features:
File Upload: Upload CSV files through a simple web form.
Data Processing: Perform basic data analysis including displaying the first few rows, calculating summary statistics, and identifying missing values.
Data Visualization: Generate and display plots (histograms) for numerical columns.


## Views: Handle file uploads, data processing
Forms: Manage file upload through Django forms.
Template: Display results and visualizations using HTML template.
Data Analysis: Used pandas to read CSV files, compute statistics, and handle missing values.
Data Visualization: Generate histograms using matplotlib and seaborn.


Handling Missing Values: Solved by using pandas functions to identify and summarize missing data.
Data Visualization: Used matplotlib and seaborn to generate plots.
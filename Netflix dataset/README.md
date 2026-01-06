# Netflix_Data_Visulaization
Visual analysis of Netflix content using Python and Matplotlib


Here’s a **clean, professional README** you can copy-paste directly into your GitHub repo.
Simple, clear, recruiter-friendly. No fluff.

---

# 📊 Netflix Data Visualization Project (Matplotlib)

## 📌 Overview

This project explores and visualizes the Netflix titles dataset using **Python**, **Pandas**, and **Matplotlib**.
The goal is to analyze Netflix’s content distribution and trends through multiple types of data visualizations.

---

## 📂 Dataset

* **Source:** Netflix titles dataset (`netflix_titles.csv`)
* **Key columns used:**

  * `type` (Movie / TV Show)
  * `release_year`
  * `duration`
  * `country`
  * `rating`

Rows with missing values in critical columns were removed to ensure clean and reliable analysis.

---

## 🛠️ Tools & Libraries

* Python
* Pandas
* Matplotlib

---

## 📈 Visualizations Included

The project answers the following questions:

1. **What is the distribution of Movies vs TV Shows on Netflix?**
   → Bar Chart

2. **What are the top 10 content ratings on Netflix?**
   → Pie Chart

3. **How long are Netflix movies typically?**
   → Histogram of movie durations

4. **How has Netflix content grown over the years?**
   → Line Plot of titles released per year

5. **Which countries contribute the most content?**
   → Horizontal Bar Chart (Top 10 countries)

6. **How do Movies and TV Shows compare over time?**
   → Subplots comparing yearly releases

All plots are saved as image files for reporting and reuse.

---

## 📁 Project Structure

```
netflix-data-visualization/
│
├── netflix_visualization.py
├── netflix_titles.csv
├── images/
│   ├── netflix_content_types_bar_chart.png
│   ├── netflix_ratings_pie_chart.png
│   ├── netflix_movie_durations_histogram.png
│   ├── netflix_release_years_line_plot.png
│   ├── netflix_top_countries_bar_chart.png
│   └── moviestvshows_comparision.png
│
└── README.md
```

---

## 🎯 Key Skills Demonstrated

* Data cleaning with Pandas
* Aggregation and grouping
* Multiple visualization types
* Saving figures programmatically
* Using both Pyplot and Object-Oriented Matplotlib APIs
* Working with a real-world dataset




---

If you want, next I can:

* tailor this README for **internship applications**
* help you write a **GitHub bio**
* suggest the **next project** that builds on this one
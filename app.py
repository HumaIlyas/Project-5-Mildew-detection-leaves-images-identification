import streamlit as st
from app_pages.dashboard import DashBoard

# load pages scripts
from app_pages.page_project_summary import page_project_summary_content
from app_pages.page_leaf_visualizer import page_leaf_visualizer_content
from app_pages.page_mildew_detector import page_mildew_detector_content
from app_pages.page_project_hypotheses import page_project_hypotheses_content
from app_pages.page_ml_performance import page_ml_performance_metrics_content

# Create an instance of the app
app = DashBoard(app_name="Mildew Detector")

# Add app pages using .add_page()
app.add_page("Project Summary", page_project_summary_content)
app.add_page("Leaf Vizualizer", page_leaf_visualizer_content)
app.add_page("Mildew Detection", page_mildew_detector_content)
app.add_page("Project Hypothesis", page_project_hypotheses_content)
app.add_page("ML Performance Metrics", page_ml_performance_metrics_content)

# Run the app
app.run()

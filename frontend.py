# frontend.py

import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import os

def display_results(final_summaries, answers):
    """Display final summaries and allow users to save them as PDF."""

    # Create Tkinter window
    root = tk.Tk()
    root.title("Summary Report")

    # Display final summaries for each folder
    for i, (final_summary, folder_answers) in enumerate(zip(final_summaries, answers), start=1):
        folder_name = f"Folder {i}"
        folder_summary = final_summary
        folder_answers_str = "\n\n".join([f"{key}: {', '.join(value)}" for key, value in folder_answers.items()])
        full_summary = f"{folder_summary}\n\nAnswers:\n{folder_answers_str}"

        # Label for folder summary
        label_folder = tk.Label(root, text=f"{folder_name} Summary:", font=("Helvetica", 12, "bold"))
        label_folder.pack(pady=5, anchor=tk.W)

        # Text area to display summary
        summary_text = tk.Text(root, height=10, width=80)
        summary_text.insert(tk.END, full_summary)
        summary_text.pack(pady=5)

        # Button to save summary as PDF
        save_button = tk.Button(root, text=f"Save {folder_name} Summary to PDF", command=lambda summary=full_summary, folder_name=folder_name: save_pdf(summary, folder_name))
        save_button.pack(pady=5)

        # Separator between folder summaries
        separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)

    # Run Tkinter main loop
    root.mainloop()

def save_pdf(summary, folder_name):
    """Save summary as PDF."""

    # Ask user for file path to save PDF
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile=f"{folder_name}_summary")
    if not file_path:
        return  # User canceled operation

    # Create PDF document
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    body_style = styles['Normal']
    section_body_style = ParagraphStyle('SectionBody', parent=body_style, spaceBefore=5, spaceAfter=10)

    content = []

    # Add summary paragraph to PDF
    summary_paragraph = Paragraph(summary, section_body_style)
    content.append(summary_paragraph)

    # Build PDF document
    doc.build(content)

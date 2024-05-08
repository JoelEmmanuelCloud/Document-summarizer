# Document Summarization Project

This project aims to summarize legal documents by processing them through a natural language processing model. The summarization process is guided by specific questions provided by a supervisor to ensure that key points are captured accurately.

## Overview

The project consists of several Python scripts responsible for different aspects of the document summarization process:

- `main.py`: The main script that orchestrates the document summarization process. It iterates through folders containing legal documents, summarizes each document, and displays the final summaries.

- `document_processing.py`: Contains functions for processing individual documents, including reading PDF files, removing special characters, and normalizing text.

- `frontend.py`: Provides a graphical user interface (GUI) for displaying final summaries and allowing users to save them as PDF files.

- `summarization.py`: Handles the interaction with a natural language processing model (implemented using Bedrock) for generating document summaries.

- `prompt.py`: Contains the prompt strings used to guide the summarization process, as provided by the supervisor.


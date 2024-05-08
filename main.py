import os
from summarization import summarize_folder
from frontend import display_results

def main():
    """Main function to summarize documents in folders."""
    final_summaries = []
    answers = []
    documents_path = "Documents"
    for folder_name in os.listdir(documents_path):
        folder_path = os.path.join(documents_path, folder_name)
        if os.path.isdir(folder_path):
            final_summary, folder_answers = summarize_folder(folder_path)
            final_summaries.append(final_summary)
            answers.append(folder_answers)

    display_results(final_summaries, answers)

if __name__ == "__main__":
    main()
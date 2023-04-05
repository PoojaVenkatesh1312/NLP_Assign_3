import csv
import difflib
import gradio as gr

# Load the CSV data
with open('updated_dataset.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Define function to generate answer to user question
def generate_answer(question, context):
    # Find matching row based on context and question
    match_rows = []
    for row in data:
        if context.lower() in row['context'].lower() and difflib.SequenceMatcher(None, question.lower(), row['question'].lower()).ratio() > 0.8:
            match_rows.append(row)

    # Return the answer(s)
    if match_rows:
        return [row['answer'] for row in match_rows]
    else:
        return "No answer found."

# Create the input and output interfaces
question = gr.inputs.Textbox(label="Question")
context = gr.inputs.Textbox(label="Context")
output = gr.outputs.Textbox(label="Answer")

# Create the Gradio interface
gradio_interface = gr.Interface(fn=generate_answer, inputs=[question, context], outputs=output, title="QA System")

# Launch the interface
gradio_interface.launch()

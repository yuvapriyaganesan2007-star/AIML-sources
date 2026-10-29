
import gradio as gr

def explain_topic(topic, level):
    if not topic.strip():
        return "Please enter a topic."

    return (
        f"Study Topic: {topic}\n"
        f"Level: {level}\n\n"
        f"1. Understand the definition of {topic}.\n"
        f"2. Learn the basic concepts.\n"
        f"3. Study practical examples.\n"
        f"4. Practise related problems.\n"
        f"5. Revise what you learned."
    )

def make_study_plan(topic, hours):
    if not topic.strip():
        return "Please enter a topic."

    return (
        f"Study Plan: {topic}\n\n"
        f"Total hours: {hours}\n"
        f"Session 1: Fundamentals ({hours * 0.4:.1f} hours)\n"
        f"Session 2: Examples ({hours * 0.3:.1f} hours)\n"
        f"Session 3: Practice ({hours * 0.3:.1f} hours)"
    )

def generate_quiz(topic):
    if not topic.strip():
        return "Please enter a topic."

    return "\n\n".join([
        f"1. What is {topic}?",
        f"2. Explain the main concepts of {topic}.",
        f"3. Give an example of {topic}.",
        f"4. What are common mistakes in {topic}?",
        f"5. How is {topic} used in practice?"
    ])

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# 📚 AI Study Assistant")
    gr.Markdown("Your personal study companion.")

    with gr.Tab("Study Guide"):
        topic1 = gr.Textbox(label="Enter a topic")
        level = gr.Dropdown(
            ["Beginner", "Intermediate", "Advanced"],
            value="Beginner",
            label="Learning level"
        )
        guide_btn = gr.Button("Create Study Guide")
        guide_out = gr.Textbox(lines=8)
        guide_btn.click(
            explain_topic, [topic1, level], guide_out
        )

    with gr.Tab("Study Planner"):
        topic2 = gr.Textbox(label="Subject or topic")
        hours = gr.Slider(1, 10, value=2, step=1)
        plan_btn = gr.Button("Generate Plan")
        plan_out = gr.Textbox(lines=6)
        plan_btn.click(
            make_study_plan, [topic2, hours], plan_out
        )

    with gr.Tab("Practice Quiz"):
        topic3 = gr.Textbox(label="Quiz topic")
        quiz_btn = gr.Button("Generate Questions")
        quiz_out = gr.Textbox(lines=8)
        quiz_btn.click(generate_quiz, [topic3], quiz_out)

if __name__ == "__main__":
    app.launch()

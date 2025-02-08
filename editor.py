import markdown

def convert_to_html(md_text):
    return markdown.markdown(md_text)

sample_md = "# Hello, Markdown!"
print(convert_to_html(sample_md))

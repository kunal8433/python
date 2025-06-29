

class HomePage:
    def __init__(self):
        self.title = "My Awesome Website"
        self.theme = "light"
        self.sections = []
    
    def header(self, text):
        return f"<h1 class='text-4xl font-bold'>{text}</h1>"
    
    def paragraph(self, text):
        return f"<p class='text-lg my-4'>{text}</p>"
    
    def image(self, src, alt):' alt='
    
    def button(self, text, url):
        return f"<a href='{url}' class='px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 inline-block'>{text}</a>"
    
    def add_section(self, content):
        self.sections.append(f"<section class='p-8 my-6 bg-white rounded-lg shadow'>{content}</section>")
    
    def generate(self):
        sections_html = "\n".join(self.sections)
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.title}</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-gray-100">
            {sections_html}
        </body>
        </html>
        """

# Example usage
page = HomePage()
page.add_section(page.header("Welcome to PySite Builder"))
page.add_section(page.paragraph("Create beautiful websites using Python-inspired syntax."))
page.add_section(page.image("https://placehold.co/600x300", "Modern workspace with laptop and notebook"))
page.add_section(page.button("Get Started", "#"))
                    
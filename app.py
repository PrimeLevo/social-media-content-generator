import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
from forms import URLForm

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    result = None
    
    if form.validate_on_submit():
        url = form.url.data
        content = scrape_url(url)
        if content:
            result = generate_social_content(content, form.platform.data)
    
    return render_template('index.html', form=form, result=result)

def scrape_url(url):
    """Scrape content from the given URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else ""
        
        # Extract main content (p tags from the main content area)
        # This is a simple approach - real implementation may need custom selectors based on the site
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        
        # Limit content length for API calls
        content = content[:3000] if content else ""
        
        return {"title": title, "content": content, "url": url}
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None

def generate_social_content(page_data, platform="general"):
    """Generate social media content based on scraped data using OpenAI"""
    try:
        prompt = f"""Generate a compelling social media post for {platform} based on this content:
        
Title: {page_data['title']}
        
Content summary: {page_data['content']}
        
URL: {page_data['url']}
        
The post should be engaging, informative, and designed to encourage clicks to the original URL.
"""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a social media marketing expert who creates engaging posts."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating content: {e}")
        return "Error generating social media content. Please check your API key and try again."

if __name__ == '__main__':
    app.run(debug=True)
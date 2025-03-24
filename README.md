# Social Media Content Generator

A web application that generates social media content from URLs using web crawling and OpenAI's GPT.

## Features

- Enter any URL to generate social media content
- Customize content for different platforms (Twitter/X, LinkedIn, Facebook, Instagram)
- Simple and intuitive user interface

## Technologies Used

- Python 3.8+
- Flask web framework
- Beautiful Soup for web scraping
- OpenAI API for content generation
- Bootstrap for frontend styling

## Installation

1. Clone the repository

```bash
git clone https://github.com/PrimeLevo/social-media-content-generator.git
cd social-media-content-generator
```

2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

```bash
cp .env.example .env
```

Then edit the `.env` file and add your OpenAI API key

5. Run the application

```bash
python app.py
```

6. Visit `http://127.0.0.1:5000/` in your browser

## Usage

1. Enter a URL in the input field
2. Select the target social media platform
3. Click "Generate Content"
4. Copy the generated content for your social media post

## Future Improvements

- Add more customization options for content style
- Implement content previews for different platforms
- Add image extraction and generation
- Support for batch processing multiple URLs
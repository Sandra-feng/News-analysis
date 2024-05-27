import json
import os
from werkzeug.utils import secure_filename
from flask import Flask,jsonify
from flask import request
from flask_cors import *
import shutil
# import case_mark
# from mark import case_mark
# from mark import naive_bayes
from crawler import NewsScraper
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import logging
from logging.handlers import RotatingFileHandler
from urllib.parse import urljoin



# soup = BeautifulSoup(html_data, 'html.parser', from_encoding='utf-8')
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 解决跨域问题



@app.route('/data-science', methods=['GET', 'POST'])
def test_axios():
    return "HIT GOOD TRAP!"

#爬取功能，将抓取到的文本图片返回前端展示，且保存到本地
@app.route('/fetch-news', methods=['GET', 'POST'])  
def fetch_news():
    folder = 'flask_backend/crawler/crawler_download'
    news_url = request.args.get('newsUrl')
    base_path = os.path.abspath(folder)
    new_folder = os.path.join(base_path, "new_folder")
    os.makedirs(new_folder, exist_ok=True)  # creates the directory if it does not exist
    news_file_path = os.path.join(new_folder, "news.txt")
    try:
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
        title = soup.find('h1').text if soup.find('h1') else 'No title found'
        content = ' '.join(p.text for p in soup.find_all('p'))
        image_tag = soup.find('img')
        image_url = urljoin(news_url, image_tag['src'])
        image_url = image_tag['src'] if image_tag else 'No Image'
        with open(news_file_path, 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\nContent:\n{content}\n\nImage URL: {image_url}")
        
        if image_tag:
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_path = os.path.join(new_folder, "news_image.jpg")  # Specify the image filename
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_response.content)

        return jsonify({'title': title, 'content': content, 'image_url': image_url})
    except Exception as e:
        app.logger.error(f"Error fetching news from {news_url}: {str(e)}")
        return jsonify({'error': str(e)}), 500

#补充信息部分。

@app.route('/submit-supplement', methods=['POST'])
def submit_supplement():
    news_file_path = os.path.join(new_folder, "news.txt")
    try:
        text_data = request.form.get('text_data', None)
        image = request.files.get('image', None)

        if text_data:
            with open(news_file_path, 'a', encoding='utf-8') as file:
                file.write(f"\nSupplement Text: {text_data}\n")

        # Save the image to the local folder if it exists
        if image:
            image_path = os.path.join(new_folder, image.filename)
            image.save(image_path)
        return jsonify({'message': 'Data submitted successfully'}), 200
    except Exception as e:
        app.logger.error(f"Error handling supplement data: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/clear-cache', methods=['POST'])
def clear_cache():
    folder = 'flask_backend/crawler/crawler_download'
    base_path = os.path.abspath(folder)
    new_folder = os.path.join(base_path, "new_folder")
    
    try:
        # 检查文件夹是否存在
        if os.path.exists(new_folder):
            # 删除文件夹及其所有内容
            shutil.rmtree(new_folder)
            message = 'Cache cleared successfully.'
        else:
            message = 'No cache to clear.'

        return jsonify({'message': message}), 200
    except Exception as e:
        app.logger.error(f"Error clearing cache: {str(e)}")
        return jsonify({'error': str(e)}), 500

def configure_logging():
    handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024 * 10, backupCount=3)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

if __name__ == '__main__':
    configure_logging()
    app.run(debug=True)
# # app = Flask(__name__)
# # CORS(app)

# @app.route('/fetch-news', methods=['GET'])
# def fetch_news():
#     news_url = request.args.get('newsUrl')
#     if not news_url:
#         return jsonify({'error': 'No URL provided'}), 400

#     scraper = NewsScraper()
#     try:
#         news_data = scraper.fetch_news(news_url)
#         return jsonify(news_data)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         scraper.close()

# if __name__ == '__main__':
#     app.run(debug=True)
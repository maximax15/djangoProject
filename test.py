
from requests_html import HTMLSession   

session = HTMLSession()
response = session.get("https://react-amazon-bestsellers-books-dy.netlify.app/")
response.html.render()

print(response.html)
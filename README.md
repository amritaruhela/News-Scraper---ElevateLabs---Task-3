# 📰 News Headlines Web Scraper

A Python-based command-line application that automatically fetches the latest news headlines from a public news website using **Requests** and **BeautifulSoup**. The scraped headlines are displayed in the terminal and saved locally to a text file for future reference.

This project demonstrates the fundamentals of **web scraping**, **HTML parsing**, **file handling**, **exception handling**, and **modular Python programming**.

---

## 🚀 Features

- 🌐 Fetches live HTML content from a public news website
- 📰 Extracts the latest news headlines
- 📄 Parses HTML using BeautifulSoup
- 💾 Saves headlines to a local text file
- 🖥️ Displays headlines in a clean console format
- ⚡ Fast and lightweight implementation
- 🛡️ Includes exception handling for network and parsing errors
- 🧩 Modular and easy-to-understand code structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Requests | Fetch HTML content |
| BeautifulSoup4 | Parse HTML and extract headlines |
| VS Code | Development Environment |

---

## 📂 Project Structure

```
News-Scraper/
│
├── news_scraper.py       # Main Python script
├── headlines.txt         # Generated headlines
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/amritaruhela/news-headline-scraper.git
```

### 2. Navigate to the Project Folder

```bash
cd news-headline-scraper
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Execute the following command:

```bash
python news_scraper.py
```

After execution, the application will:

- Fetch the latest news webpage
- Extract the available headlines
- Display them in the terminal
- Save them into **headlines.txt**

---

## 💻 Sample Output

```
Top Headlines

1. Scientists discover new exoplanet...
2. Global markets rally after...
3. AI continues transforming healthcare...
4. Major sporting event concludes...
5. New technology trends emerge...
```

---

## 📄 Example headlines.txt

```
News Headlines
Generated: 2026-07-02 09:30:15

============================================================

1. Scientists discover new exoplanet...
2. Global markets rally after...
3. AI continues transforming healthcare...
```

---

## ⚠️ Error Handling

The application gracefully handles common issues including:

- No internet connection
- Website unavailable
- Timeout errors
- Invalid HTML responses
- Empty headline results

---

## 🧠 Concepts Demonstrated

This project showcases practical knowledge of:

- HTTP Requests
- Web Scraping
- HTML Parsing
- File Handling
- Functions
- Lists
- Loops
- Exception Handling
- Clean Code Principles

---

## 🎯 Learning Outcomes

By completing this project, you will gain experience in:

- Fetching data from live websites
- Working with HTML documents
- Parsing web elements using BeautifulSoup
- Saving scraped data into files
- Building reusable Python scripts
- Writing maintainable and modular code

---

## 🚀 Future Enhancements

- Export headlines to CSV
- Export headlines to JSON
- Scrape multiple news websites
- Save article links
- Add publication dates
- Search headlines by keyword
- Schedule automatic scraping
- Build a GUI using Tkinter
- Create a Flask web version

---

## 👨‍💻 Author

**Amrita Ruhela**

B.Tech Computer Science Engineering (Data Science & Machine Learning)

---

## 📜 License

This project was developed for educational purposes and internship assessment. Feel free to use and modify it for learning.

---

## ⭐ Acknowledgements

- Python Requests Library
- BeautifulSoup4
- BBC News (Publicly Accessible Website Used for Learning)

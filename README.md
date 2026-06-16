# 🦁 My-Zootopia

**My-Zootopia** is a Python tool that fetches animal data from the [API Ninja Animals API](https://api-ninjas.com/api/animals) and generates a static HTML page.  
You type an animal name, the program queries the API and produces a clean card‑based view showing:

- Name
- Diet
- First location from the `locations` list
- Type

---

## ✨ Features

- 🔍 **Interactive input** – enter an animal name right in the console.
- 🌐 **API integration** – uses the free Animals API from API Ninjas.
- 🧩 **Robust parsing** – missing fields (e.g., `diet` or `locations`) are handled safely.
- 📄 **HTML generation** – populates the `animals_template.html` template and saves the result as `animals.html`.
- 🔒 **Secure API key** – stored in a `.env` file, separate from source code.

---

## 🛠️ Technology Stack

| Area         | Technology                         |
|--------------|------------------------------------|
| Language     | Python 3.8+                        |
| HTTP client  | `requests`                         |
| Templating   | Python string replacement          |
| Environment  | `python-dotenv` (recommended)      |

---

## 📁 Project Structure

My-Zootopia/

├── .env # Contains API_KEY=...

├── .gitignore # Ignores .env, animals.html, pycache, etc.

├── animals_template.html # HTML skeleton with REPLACE_ANIMALS_INFO placeholder

├── animals_web_generator.py # Main script (input, template reading, file writing)

├── data_fetcher.py # API call + serialisation of animal data to HTML

├── README.md

├── requirements.txt # Dependencies (e.g., requests, python-dotenv)

└── animals.html # Generated output (ignored by Git)

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8 or higher**
- **Free API key from [API Ninjas](https://api-ninjas.com/register)**

### Step-by-Step

1. **Clone the repository**
2. **Create a virtual environment (optional but recommended)**
3. **Install dependencies**
4. **Set up your .env file**

    Create a .env file in the project root with: 
    **API_KEY=your_actual_api_key_here**

---

## 💻 Usage

### Run the main script:
- **python animals_web_generator.py**

### You will be prompted:
- **Enter a name of an animal:**

    Type an animal name (e.g., fox, lion, monkey...) and press Enter
- **The program will:**

    --call the API,
    
    --parse the JSON response,
    
    --replace the '_ _ REPLACE_ANIMALS_INFO _ _' placeholder in the template,
    
    --and write the output to animals.html.
    
    --Open animals.html in your browser to see the generated animal gallery.

---

## 📄 License

-  **This project is licensed under the MIT License – see the LICENSE file for details.**

---

## 🙏 Acknowledgements

- **API Ninjas for providing the free Animals API.**
- **All animal lovers who inspired this little tool.**
# 🧠 EntiScope – Smart NER Web App

**EntiScope** is an intelligent Named Entity Recognition (NER) web app built with **Streamlit** and powered by a fine-tuned **Hugging Face Transformer model**.  
It allows users to input any sentence or paragraph and instantly highlights named entities such as names, dates, locations, organizations, and more – using fine-grained BIO tagging.

---

## 🚀 Live Demo

🔗 [Click here to open the app](https://ner-model-002-arunnivaas.streamlit.app/)

---

## ✨ Features

- ✅ Loads custom fine-tuned model from Hugging Face Hub
- ✅ Real-time Named Entity Recognition (NER)
- ✅ Highlights 37 fine-grained entity types with BIO tagging
- ✅ Clean, responsive, and user-friendly UI built in Streamlit
- ✅ Dark theme interface with color-coded entity labels

---

## 📦 Tech Stack

- 🧠 [Hugging Face Transformers](https://huggingface.co/transformers/)
- 💻 [Streamlit](https://streamlit.io/)
- 🔥 PyTorch
- 🧾 BIO Tagging Scheme
- 🌐 Hugging Face Hub for model hosting

---

## 🧠 Named Entity Recognition (NER) Label Schema

This app supports a wide range of named entities using the **BIO format**:

- `B-TAG`: Beginning of an entity
- `I-TAG`: Inside of the entity
- `O`: Outside any named entity

### Supported Entity Tags (Total: 37)

| Tag              | Description                                      | Example                        | Emoji |
|------------------|--------------------------------------------------|--------------------------------|--------|
| `B-PERSON`       | Person's name                                    | Elon Musk                      | 👤     |
| `B-ORG`          | Organization                                     | Google, United Nations         | 🏢     |
| `B-GPE`          | Geopolitical location (city, country, state)     | India, New York                | 🌍     |
| `B-DATE`         | Date-related information                         | January, 2024                  | 🗓️     |
| `B-TIME`         | Time expressions                                 | 2:00 PM, noon                  | ⏰     |
| `B-MONEY`        | Monetary values                                  | $100, Rs.500                   | 💸     |
| `B-PRODUCT`      | Product names                                    | iPhone, Tesla                  | 📱     |
| `B-EVENT`        | Event names                                      | Olympics, G20 Summit           | 🎉     |
| `B-LAW`          | Legal documents or acts                          | Constitution, GDPR             | 📜     |
| `B-LANGUAGE`     | Spoken languages                                 | English, Tamil                 | 🗣️     |
| `B-WORK_OF_ART`  | Titles of books, paintings, films, etc.          | Mona Lisa, Hamlet              | 🎨     |
| ...              | And many more: `FAC`, `LOC`, `CARDINAL`, `ORDINAL`, `PERCENT`, `QUANTITY`, `NORP` |
| `I-TAG` variants | Inside the corresponding entity type             | (e.g., "Musk" in Elon Musk)    | ➕     |
| `O`              | Outside of any named entity                      | (e.g., "was", "the", "a")      | 🚫     |

---

## 🧪 Example

> "**Barack Obama** was born in **Hawaii** in **1961** and worked for the **United Nations**."

Detected Entities:
- **Barack Obama** → `PERSON` 👤  
- **Hawaii** → `GPE` 🌍  
- **1961** → `DATE` 🗓️  
- **United Nations** → `ORG` 🏢

---

## 🖼️ UI Preview

### 🔹 Input Example

![Input Screenshot](https://github.com/arun-nivaas/NER-model-streamlit-002/blob/main/asserts/input_example.png?raw=true)

---

### 🔹 Output with Detected Entities

![Output Screenshot](https://github.com/arun-nivaas/NER-model-streamlit-002/blob/main/asserts/output_example.png?raw=true)

---

## 🔖 About the Project

**EntiScope** was created as part of my transition from Android development into NLP. The model was trained on custom NER data with 37 distinct entity classes and fine-tuned for token classification using the Hugging Face Transformers library.

This app demonstrates the power of combining deep learning with simple UI tools to make machine learning more accessible and interactive.

---

## 📬 Contact

- 👨‍💻 GitHub: [@arunnivaas](https://github.com/arunnivaas)
- 🔗 LinkedIn: [linkedin.com/in/arunnivaas](https://www.linkedin.com/in/arunnivaas)
- 📧 Email: arcarunnivaas@gmail.com

---

> Made with ❤️ using Streamlit + Hugging Face  
> Project Name: **EntiScope – Smart NER Web App**

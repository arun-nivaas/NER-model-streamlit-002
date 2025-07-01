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

| Tag              | Description                                                                              | Example                            | Emoji |
|------------------|------------------------------------------------------------------------------------------|------------------------------------|--------|
| O              | Outside of any named entity                                                              | the, is, on                         | 🚫     |
| B-CARDINAL     | Beginning of a cardinal number                                                           | 1000, twenty                        | 🔢     |
| I-CARDINAL     | Continuation of a cardinal number                                                        | 000 in 1000                         | 🔢     |
| B-DATE         | Beginning of a date                                                                      | January, 2023                       | 🗓️     |
| I-DATE         | Inside a date                                                                            | 2024 in January 2024                | 🗓️     |
| B-EVENT        | Beginning of an event name                                                               | Olympics, World Cup                 | 🎉     |
| I-EVENT        | Inside an event name                                                                     | Games in Olympic Games              | 🎉     |
| B-FAC          | Beginning of a facility                                                                  | Eiffel Tower, Stanford Stadium      | 🏛️     |
| I-FAC          | Inside a facility                                                                         | Tower in Eiffel Tower               | 🏛️     |
| B-GPE          | Geopolitical entity (city, country, state)                                               | India, New York                     | 🌍     |
| I-GPE          | Inside a GPE                                                                              | York in New York                    | 🌍     |
| B-LANGUAGE     | Beginning of a language                                                                  | English, German                     | 🗣️     |
| I-LANGUAGE     | Inside a language name                                                                   | Mandarin in Chinese Mandarin        | 🗣️     |
| B-LAW          | Beginning of a law or legal document                                                     | Constitution, GDPR                  | 📜     |
| I-LAW          | Inside a law name                                                                        | Act in Clean Air Act                | 📜     |
| B-LOC          | Non-GPE location (mountains, oceans, etc.)                                              | Pacific Ocean, Himalayas            | 🗺️     |
| I-LOC          | Inside a location                                                                         | Ocean in Pacific Ocean              | 🗺️     |
| B-MONEY        | Beginning of a monetary value                                                            | $100, Rs. 500                       | 💸     |
| I-MONEY        | Inside a money value                                                                     | 000 in $1,000                       | 💸     |
| B-NORP         | Nationalities, religious or political groups                                             | American, Hindu, Republican         | 🏳️     |
| I-NORP         | Inside a NORP group                                                                      | Party in Democratic Party           | 🏳️     |
| B-ORDINAL      | Beginning of an ordinal number                                                           | First, Second                       | 🥇     |
| I-ORDINAL      | Inside an ordinal number                                                                 | th in 25th                          | 🥇     |
| B-ORG          | Beginning of an organization                                                             | Google, United Nations              | 🏢     |
| I-ORG          | Inside an organization name                                                              | Nations in United Nations           | 🏢     |
| B-PERCENT      | Beginning of a percentage                                                                | 50%, ten percent                    | 📊     |
| I-PERCENT      | Inside a percentage                                                                      | % in 90 %                           | 📊     |
| B-PERSON       | Beginning of a person’s name                                                             | Elon Musk, Marie Curie              | 👤     |
| I-PERSON       | Inside a person’s name                                                                   | Musk in Elon Musk                   | 👤     |
| B-PRODUCT      | Beginning of a product name                                                              | iPhone, PlayStation                 | 📱     |
| I-PRODUCT      | Inside a product name                                                                    | Pro in iPhone 13 Pro                | 📱     |
| B-QUANTITY     | Beginning of a quantity                                                                  | 2 liters, 5 kg                      | ⚖️     |
| I-QUANTITY     | Inside a quantity                                                                        | kg in 5 kg                          | ⚖️     |
| B-TIME         | Beginning of a time expression                                                           | noon, 2:00 PM                       | ⏰     |
| I-TIME         | Inside a time phrase                                                                     | PM in 2:00 PM                       | ⏰     |
| B-WORK_OF_ART  | Beginning of a work of art (book, movie, painting)                                       | Mona Lisa, Hamlet                   | 🎨     |
| I-WORK_OF_ART  | Inside a work of art title                                                               | Lisa in Mona Lisa                   | 🎨     |

---

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

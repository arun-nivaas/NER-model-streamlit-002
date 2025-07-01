# 🧠 NER Web App UI with Hugging Face & Streamlit

This repository contains the **Streamlit UI** for a Named Entity Recognition (NER) web app.  
It uses a fine-tuned Hugging Face Transformer model (uploaded to Hugging Face Hub) and provides a simple interface to highlight named entities from user input text.

---

## 🚀 Live Demo

🔗 [Click here to open the app](https://ner-model-002-arunnivaas.streamlit.app/)

---

## ✨ Features

- ✅ Loads model from Hugging Face Hub using `AutoTokenizer` and `AutoModelForTokenClassification`
- ✅ Real-time Named Entity Recognition (NER)
- ✅ Minimalistic and user-friendly Streamlit interface
- ✅ Supports any sentence or paragraph input

---

## 📦 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)

---

## 🧠 Named Entity Recognition (NER) Label Schema

This model was trained for fine-grained Named Entity Recognition using the **BIO tagging scheme**. Each label identifies the position (`B-`eginning, `I-`nside, `O`utside) and the type of named entity.

---

### 🧾 BIO Format

- `B-TAG`: Beginning of an entity of type `TAG`
- `I-TAG`: Continuation of the same entity
- `O`: Outside any named entity

---

### 📚 Entity Tag Descriptions

| Tag              | Description                                                                              | Example                            | Emoji |
|------------------|------------------------------------------------------------------------------------------|------------------------------------|--------|
| `O`              | Outside of any named entity                                                              | the, is, on                         | 🚫     |
| `B-CARDINAL`     | Beginning of a cardinal number                                                           | 1000, twenty                        | 🔢     |
| `I-CARDINAL`     | Continuation of a cardinal number                                                        | 000 in 1000                         | 🔢     |
| `B-DATE`         | Beginning of a date                                                                      | January, 2023                       | 🗓️     |
| `I-DATE`         | Inside a date                                                                            | 2024 in January 2024                | 🗓️     |
| `B-EVENT`        | Beginning of an event name                                                               | Olympics, World Cup                 | 🎉     |
| `I-EVENT`        | Inside an event name                                                                     | Games in Olympic Games              | 🎉     |
| `B-FAC`          | Beginning of a facility                                                                  | Eiffel Tower, Stanford Stadium      | 🏛️     |
| `I-FAC`          | Inside a facility                                                                         | Tower in Eiffel Tower               | 🏛️     |
| `B-GPE`          | Geopolitical entity (city, country, state)                                               | India, New York                     | 🌍     |
| `I-GPE`          | Inside a GPE                                                                              | York in New York                    | 🌍     |
| `B-LANGUAGE`     | Beginning of a language                                                                  | English, German                     | 🗣️     |
| `I-LANGUAGE`     | Inside a language name                                                                   | Mandarin in Chinese Mandarin        | 🗣️     |
| `B-LAW`          | Beginning of a law or legal document                                                     | Constitution, GDPR                  | 📜     |
| `I-LAW`          | Inside a law name                                                                        | Act in Clean Air Act                | 📜     |
| `B-LOC`          | Non-GPE location (mountains, oceans, etc.)                                              | Pacific Ocean, Himalayas            | 🗺️     |
| `I-LOC`          | Inside a location                                                                         | Ocean in Pacific Ocean              | 🗺️     |
| `B-MONEY`        | Beginning of a monetary value                                                            | $100, Rs. 500                       | 💸     |
| `I-MONEY`        | Inside a money value                                                                     | 000 in $1,000                       | 💸     |
| `B-NORP`         | Nationalities, religious or political groups                                             | American, Hindu, Republican         | 🏳️     |
| `I-NORP`         | Inside a NORP group                                                                      | Party in Democratic Party           | 🏳️     |
| `B-ORDINAL`      | Beginning of an ordinal number                                                           | First, Second                       | 🥇     |
| `I-ORDINAL`      | Inside an ordinal number                                                                 | th in 25th                          | 🥇     |
| `B-ORG`          | Beginning of an organization                                                             | Google, United Nations              | 🏢     |
| `I-ORG`          | Inside an organization name                                                              | Nations in United Nations           | 🏢     |
| `B-PERCENT`      | Beginning of a percentage                                                                | 50%, ten percent                    | 📊     |
| `I-PERCENT`      | Inside a percentage                                                                      | % in 90 %                           | 📊     |
| `B-PERSON`       | Beginning of a person’s name                                                             | Elon Musk, Marie Curie              | 👤     |
| `I-PERSON`       | Inside a person’s name                                                                   | Musk in Elon Musk                   | 👤     |
| `B-PRODUCT`      | Beginning of a product name                                                              | iPhone, PlayStation                 | 📱     |
| `I-PRODUCT`      | Inside a product name                                                                    | Pro in iPhone 13 Pro                | 📱     |
| `B-QUANTITY`     | Beginning of a quantity                                                                  | 2 liters, 5 kg                      | ⚖️     |
| `I-QUANTITY`     | Inside a quantity                                                                        | kg in 5 kg                          | ⚖️     |
| `B-TIME`         | Beginning of a time expression                                                           | noon, 2:00 PM                       | ⏰     |
| `I-TIME`         | Inside a time phrase                                                                     | PM in 2:00 PM                       | ⏰     |
| `B-WORK_OF_ART`  | Beginning of a work of art (book, movie, painting)                                       | Mona Lisa, Hamlet                   | 🎨     |
| `I-WORK_OF_ART`  | Inside a work of art title                                                               | Lisa in Mona Lisa                   | 🎨     |

---

### ✅ Example

> “**Barack Obama** was born in **Hawaii** in **1961** and worked for the **United Nations**.”

Entities:
- `Barack Obama` → `PERSON` 👤  
- `Hawaii` → `GPE` 🌍  
- `1961` → `DATE` 🗓️  
- `United Nations` → `ORG` 🏢  

---

## 🖼️ Example: Input Text

![Input Screenshot](https://github.com/arun-nivaas/NER-model-streamlit-002/blob/main/asserts/input_example.png?raw=true)

---

## 🖼️ Example: Output with Detected Entities

![Output Screenshot](https://github.com/arun-nivaas/NER-model-streamlit-002/blob/main/asserts/output_example.png?raw=true)


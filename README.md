# 🖼️ Image Captioning App using Vision Transformer (ViT) and GPT-2

🔗 **Project Repository:**
👉 [https://github.com/diddepavankumar/image-captioning-app]([https://github.com/diddepavankumar/image-captioning-app](https://image-captioningds3-batch17.streamlit.app/))

---

## 📌 Overview

The **Image Captioning App** is an AI-powered application that automatically generates meaningful textual descriptions for images using a combination of **Vision Transformer (ViT)** for image feature extraction and **GPT-2** for natural language generation.

This system is designed to assist users in understanding image content and has potential applications in:

* Accessibility for visually impaired individuals
* Content management systems
* Social media automation
* Image search and indexing
* AI-powered assistants

The model processes an uploaded image, extracts visual features using **ViT**, and generates a natural language caption using **GPT-2**, producing accurate and context-aware descriptions.

---

## 🚀 Features

* Upload an image and generate captions instantly
* Uses **Vision Transformer (ViT)** for feature extraction
* Uses **GPT-2** for natural language caption generation
* Simple and interactive web interface
* Real-time caption generation
* Deployable using **Streamlit**
* Scalable architecture for AI applications
* Supports multilingual captioning (if enabled)

---

## 🧠 Model Architecture

Image → Vision Transformer (ViT) → Feature Embeddings → GPT-2 → Caption Output

### Workflow

1. User uploads an image
2. Image is preprocessed
3. **ViT** extracts image features
4. Features are passed to **GPT-2**
5. GPT-2 generates a caption
6. Caption is displayed to the user

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* PyTorch
* Transformers (Hugging Face)
* Streamlit
* NumPy
* Pillow (PIL)
* Torchvision

### Deep Learning Models

* Vision Transformer (ViT)
* GPT-2

---

## 📂 Project Structure

```
image-captioning-app/

│── app.py
│── model.py
│── utils.py
│── requirements.txt
│── README.md
│── images/
│── models/
│── dataset/
```

---

## 📊 Dataset

The model is trained using image-caption datasets such as:

* COCO Dataset (Common Objects in Context)

Dataset includes:

* Thousands of images
* Multiple captions per image
* Diverse real-world scenes

---

## ⚙️ Installation

### Step 1 — Clone the Repository

```
git clone https://github.com/diddepavankumar/image-captioning-app.git
```

### Step 2 — Navigate to Project Directory

```
cd image-captioning-app
```

### Step 3 — Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit app using:

```
streamlit run app.py
```

The application will start locally at:

```
http://localhost:8501
```

---



## 🔍 Use Cases

* Assistive technology for visually impaired users
* Automated image description generation
* Smart photo management systems
* AI-powered chatbots
* Social media caption automation
* Content moderation systems

---

## 📈 Future Improvements

* Improve caption accuracy using larger datasets
* Add beam search decoding
* Support multiple languages
* Add voice output for accessibility
* Optimize model performance
* Deploy using Docker
* Add real-time camera captioning

---

## 👨‍💻 Author

**Pavan Kumar Didde**
**Gudime Niharika**
**M Lakshmi Narasimha**
**K Surya**
AI / Data Science Enthusiast
Developer | Machine Learning Engineer

GitHub:
[https://github.com/diddepavankumar](https://github.com/diddepavankumar)

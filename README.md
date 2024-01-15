# MedicoChat-a-medical-chatbot



## Problem Statement
Millions lack timely access to accurate medical information, causing anxiety, delayed care, and overburdened healthcare systems. A conversational AI assistant, trained on evidence-based data, is needed to empower individuals with self-service symptom assessment, health guidance, and resource navigation, easing pressure on providers and promoting empowered healthcare.
# Medico Chat / Medical ChatBot

A Medico is an innovative digital tool designed to provide instant and personalized healthcare information and support through natural language conversations. Leveraging artificial intelligence and machine learning, these chatbots interact with users, offering guidance on symptoms, treatment options, medication information, and general health inquiries. They can assess user inputs, ask relevant follow-up questions, and provide accurate and up-to-date medical advice based on established guidelines. Medical chatbots aim to enhance accessibility to healthcare resources, particularly in non-emergency situations, by offering a user-friendly interface for individuals to seek information and assistance. These bots contribute to the efficiency of healthcare delivery by swiftly addressing common queries, mitigating misinformation, and promoting proactive health management. While not a substitute for professional medical advice, medical chatbots serve as valuable tools to empower users with reliable information and support, fostering a more informed and engaged approach to personal well-being.


## Technologies Used

![App Screenshot](https://i.postimg.cc/xTD24jDp/logos2222-page-0001.jpg)


## License

[MIT LICENSE](https://github.com/vikashdwivedi21/MedicoChat-a-medical-chatbot/blob/main/LICENSE)


## Features

- Ability to assess and analyze user-reported symptoms to provide preliminary insights into potential health conditions.
- Deliver reliable and easy-to-understand health information, preventive care tips, and lifestyle advice to promote user awareness and wellness
- Encourage healthy habits through personalized tips, track progress towards goals like weight loss or exercise, and offer motivational guidance.



## Run Locally

Clone the project

```bash
  git clone https://github.com/vikashdwivedi21/MedicoChat-a-medical-chatbot
```

STEP 01- Create a conda environment after opening the repository

```bash
  conda create -p venv python=3.10 -y
```

```bash
  conda activate mchatbot
```

STEP 02- install the requirements

```bash
  pip install -r requirements.txt
```

Create a .env file in the root directory and add your Pinecone credentials as follows:


```bash
  ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
Run the following command

```bash
  python store_index.py
```
Finally run the following command
```bash
  python app.py
```
Now,
```bash
 open up localhost
```


## Authors

- [@Vikash Dwivedi](https://github.com/vikashdwivedi21)
- [@Tushar Nishad](https://github.com/Tusharrr08)

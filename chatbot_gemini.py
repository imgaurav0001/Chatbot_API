import google.generativeai as genai

genai.configure(api_key="AIzaSyDBPXQphC0gb51GqMYdQ86wokvnoz8isNo")

model = genai.GenerativeModel("gemini-1.5-flash")

while True:
    request = input("Enter request : ")
    if request=="exit":
        break
    response = model.generate_content(request)
    print(response.text)
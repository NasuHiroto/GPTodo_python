import openai
from django.shortcuts import render
from django.http import HttpResponse

# ChatGPT APIキーを設定してください
OPENAI_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX" # 取得したAPIkeyをXXXと置き換える

def generate_list(input_text):
    openai.api_key = OPENAI_API_KEY

    # ChatGPT APIを使ってリストを生成する
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        temperature=0.7,
        max_tokens=150
    )

    # APIのレスポンスから生成されたリストを取得する
    generated_list = response.choices[0].text.strip()

    return generated_list

def index(request):
    if request.method == 'POST':
        todo_input = request.POST.get('todo_input', '')
        todo_list = generate_list(todo_input)
        return render(request, 'gptodo/index.html', {'todo_input': todo_input, 'todo_list': todo_list})
    return render(request, 'gptodo/index.html')

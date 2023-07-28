from django.shortcuts import render
from .models import TodoItem

def index(request):
    if request.method == 'POST':
        todo_input = request.POST['todo_input']
        # ここでChatGPTを用いてTodoリストを生成する処理を実装する
        # 生成されたTodoリストをtodo_listに格納する
        todo_list = []

        return render(request, 'gptodo/todo_list.html', {'todo_list': todo_list})
    else:
        return render(request, 'gptodo/index.html')

import streamlit as st
import functions_get_files

todos = functions_get_files.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    """ Armazena valores inseridos pelo utilizador da página."""
    todos.append(todo)
    functions_get_files.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.") # A ordem importa para 
# organização da página na web.


for index, todo in enumerate(todos): #guardando o index, pois enumeramos
    checkbox = st.checkbox(todo, key=todo) #adicionando uma key que é variável,
    # pois receberemos diversos valores, um para cada iteração
    if checkbox: #caso a checkbox esteja marcada:
        todos.pop(index) #remover a tarefa do index indicado
        functions_get_files.write_todos(todos) #reescrever arquivo
        del st.session_state[todo] #remover também do session state (para organização)
        st.experimental_rerun() #correr o código novamente.

st.text_input(label=' ', placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
""" on_change é como o select do powerapps, é o que o enter irá fazer no input,
neste caso, indicamos que ao ser pressionado enter, será executada a função add_todo.
O placeholder indica o que será o texto guia dentro daa inputbox antes do usuário digitar. """


st.session_state
# o session state me dará informação de um dicionário com as keys que foram definidas
# e o valor de retorno de cada item do dicionário vai depender das ações do usuário.
# no caso da inputbox, o dicionário recebe a key, e uma string igual ao que 
# o usuário inserir. No caso das checkboxes, será inserido um dicionário com todas
# as tarefas salvas no arquivo, que estão dispostas no site com as checkboxes,
# cada tarefa com a checkbox desmarcada receberá false, marcada receberá true.
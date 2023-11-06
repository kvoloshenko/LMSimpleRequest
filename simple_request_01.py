import openai

def marketing_text(user_input, temp=0.9):
    openai.api_type = "open_ai"
    openai.api_base = "http://localhost:1234/v1"
    openai.api_key = "no need anymore"


    system_content = """
    Ты старательный помощник.
    """
    print(f'system_content={system_content}')
    user_content = 'Write a Telegram post on ' + user_input + ' Give the result in Russian'
    print(f'user_content={user_content}')

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]


    completion = openai.ChatCompletion.create(
        model='no need anymore',
        messages=messages,
        temperature=temp
    )


    answer = completion.choices[0].message.content
    print(answer)  # query result
    return answer

if __name__ == '__main__':
    topic ="Обучаю безопасному и контраварийному вождению автомобиля"
    ans = marketing_text(topic)
    print(ans)
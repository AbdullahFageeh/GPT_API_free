from openai import OpenAI
import sys

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="YOUR API KEY",
    base_url="https://api.chatanywhere.tech/v1"
)



# 非流式响应
def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        # Performance optimization: cache content in local variable to avoid redundant attribute/index lookups
        content = chunk.choices[0].delta.content
        if content is not None:
            # Performance optimization: use sys.stdout.write for faster output than print()
            sys.stdout.write(content)
    # Ensure final newline for clean terminal output
    print()

if __name__ == '__main__':
    messages = [{'role': 'user','content': '鲁迅和周树人的关系'},]
    # 非流式调用
    # gpt_35_api(messages)
    # 流式调用
    gpt_35_api_stream(messages)

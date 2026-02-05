from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字，简单回答。"
)

# 标准写法：调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张", gender="女儿")
#
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

# 基于Chain链的写法
model = Tongyi(model="qwen-max")
# 生成链
chain = prompt_template | model
# 基于链，调用模型获取结果
res = chain.invoke(input={"lastname": "张", "gender": "女儿"})
print(res)
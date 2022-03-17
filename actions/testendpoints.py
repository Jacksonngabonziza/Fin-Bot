# import requests

# def getAgent(district):
#     url="https://financial-chatbot-basic.herokuapp.com/api/v1/agent/location/"
#     district=district.lower()
#     urlr=url+district
#     x=requests.get(urlr)
#     #print(x.text)
#     result=x.json()
#     return result

# def getbranch(district):
#     url="http://financial-chatbot-basic.herokuapp.com/api/v1/branches/district/"
#     district=district.lower()
#     urlr=url+district
#     x=requests.get(urlr)
#     result=x.json()
#     return result
# d=input("enter district to see agents available: ")
# x=getAgent(d)
# #print(type(x))
# for i in x:
#     print(i)
# x=getbranch(d)
# for j in x:
#     print(j)



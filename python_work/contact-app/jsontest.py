from Contact import Contact
import json

obj = Contact('홍길동', '010-2222-1111', 'hong@naver.com')

d = obj.as_dict()

# 직렬화
json_str = json.dumps(d)
print(json_str)

json_str = json.dumps(d, indent=4)
print(json_str)

# 사전으로 역직렬화
target = json.loads(json_str)
print(type(target))
print(target)

# 사전에서 contact으로 복원
cls = target["__class__"]
cls = eval(cls)
print(cls)
args = target["__arg__"]
print(args)
kw = target["__kw__"]
print(kw)

# contact 인스턴스 복원
print('---------------------------------')
contact = cls(**kw)
print(contact)
contact.print_detail()
print('---------------------------------')

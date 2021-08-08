import re
pattern=re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password='hdjkvnvabc1128%@9'
check=pattern.fullmatch(password)
print(check)
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

sent=[sub+" "+verb+" "+obj for sub in subjects for verb in verbs for obj in objects]

for sentence in sent:
    print(sentence) 
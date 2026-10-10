import json,requests,os,re
items=[json.loads(l) for l in open('sets/translation.jsonl')]
pend=[i for i in items if i['sub']=='perturb-pending']
types=["negation flipped","tense changed","subject/person changed","quantity/number changed","object or key noun replaced by a related but different one","adjective/adverb replaced by its opposite or a clearly different one"]
lines=[]
for n,it in enumerate(pend,1):
    lines.append(f'{n}. type: {types[n%len(types)]} | JP: {it["state"]["japanese"]} | EN: {it["state"]["english"]}')
prompt=("Below are Japanese sentences with correct English translations. For each, write a version of the English that "
"stays fluent and close in wording but is now a WRONG translation, by making exactly the change named in 'type'. The change must "
"clearly alter the meaning so a careful bilingual checker would mark it wrong. Return only a JSON array of {\"n\":..., \"english\":...}.\n\n"+"\n".join(lines))
r=requests.post("https://openrouter.ai/api/v1/chat/completions",headers={"Authorization":"Bearer "+os.environ["OPENROUTER_API_KEY"]},
 json={"model":"google/gemini-3.8-flash","messages":[{"role":"user","content":prompt}],"temperature":0.3,"usage":{"include":True}},timeout=300).json()
txt=r["choices"][0]["message"]["content"]; print(r.get("usage"))
txt=re.sub(r"^```(?:json)?|```$","",txt.strip(),flags=re.M)
arr={a["n"]:a["english"] for a in json.loads(txt[txt.find('['):txt.rfind(']')+1])}
for n,it in enumerate(pend,1):
    new=arr.get(n)
    if new and new.strip()!=it["state"]["english"].strip():
        it["state"]["english"]=new; it["sub"]="perturb:"+types[n%len(types)].split()[0]
    else: print("missing",n)
with open('sets/translation.jsonl','w') as f:
    for it in items:
        if it['sub']!='perturb-pending': f.write(json.dumps(it,ensure_ascii=False)+"\n")
for it in pend[:8]: print(it["state"], it["sub"])

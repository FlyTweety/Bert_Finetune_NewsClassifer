# 读入数据
file = "./data/new_new_test_data.tsv"
with open(file, "r", encoding="utf-8") as f:
    dataset = f.read()
lines = dataset.split("\n")
labels = []
texts = []
for line in lines[1:-1]:
    try:
        label, text_a = line.split("\t")
        labels.append(label)
        texts.append(text_a)
    except:
        continue

# 构造输出
tips = "接下来，我给你多条新闻标题，你需要给它分类，类别是 0: \"news_story\",1: \"news_culture\",2: \"news_entertainment\",3: \"news_entertainment\",4: \"news_sport\",6: \"news_house\",7: \"news_car\",8: \"news_edu\",9: \"news_tech\",10: \"news_military\",12: \"news_travel\",13: \"news_world\",14: \"stock\", 15: \"news_agriculture\",16: \"news_game\"。 请你以一行一个的方式，输出格式为：标题序号：类别数字。\n要分类的多条新闻标题是："

for i in range(90, 100):
    tips = tips + str(i) + ": " + texts[i] + "\n"

print(tips)
    

import re

# 正确答案
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


# 我的输出
result_file = "./BERTresults.txt"
with open(result_file, "r", encoding="utf-8") as f:
    result_dataset = f.read()
result_lines = result_dataset.split("\n")

pattern = r"inputs:\s'(.*?)',\spredict:\s'(.*?)'\s,\slabel:\s'(.*?)'"

trans_number_2_word_dict  = {   
                    0: "news_story",
                    1: "news_culture",
                    2: "news_entertainment",
                    3: "news_entertainment",
                    4: "news_sport",
                    6: "news_house",
                    7: "news_car",
                    8: "news_edu",
                    9: "news_tech",
                    10: "news_military",
                    12: "news_travel",
                    13: "news_world",
                    14: "stock",
                    15: "news_agriculture",
                    16: "news_game"
                }

for i in range(0, len(result_lines)):
    line = result_lines[i]

    match = re.search(pattern, line)
    inputs = match.group(1)
    predict = match.group(2)
    label = match.group(3)

    if label != predict:
        print(f"Answer: {label}, Predict: {predict}, Text:{inputs}")


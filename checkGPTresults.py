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

trans_word_2_number_dict = {
    'news_story': 0,
    'news_culture': 1,
    'news_entertainment': 3,
    'news_sport': 4,
    'news_house': 6,
    'news_car': 7,
    'news_edu': 8,
    'news_tech': 9,
    'news_military': 10,
    'news_travel': 12,
    'news_world': 13,
    'stock': 14,
    'news_agriculture': 15,
    'news_game': 16
}


result_file = "./GPTresults.txt"
with open(result_file, "r", encoding="utf-8") as f:
    result_dataset = f.read()
result_lines = result_dataset.split("\n")
result_labels = []
for line in result_lines:
    try:
        index, label = line.split(": ")
        if label in trans_word_2_number_dict:
            label = str(trans_word_2_number_dict[label])
        result_labels.append(label)
    except:
        continue

# 比较和CHATGPT和答案不一样之处
for i in range(0, len(result_labels)):
    if result_labels[i] != labels[i]:
        print(f"Answer: {trans_number_2_word_dict[int(labels[i])]}, Predict: {trans_number_2_word_dict[int(result_labels[i])]}, Text:{texts[i]}")
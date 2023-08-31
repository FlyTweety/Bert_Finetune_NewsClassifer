with open("test_data.tsv", "r", encoding="utf-8") as f:
    dataset = f.read()
    
lines = dataset.split("\n")
#print(lines[0])

new_lines = []
new_lines.append(lines[0])

for line in lines[1:-1]:
    try:
        label, text_a = line.split("\t")
        
        #if int(label) < 0 or int(label) > 16:
        #    print("!!!!!!", label)
        
        new_lines.append(f"{str(int(label)-100)}\t{text_a}")

    except Exception as e:
        print(e)

        

print(len(new_lines))
    
    

with open("new_new_test_data.tsv", "w", encoding="utf-8") as f:
    for i in range(0, 1000):
        line = new_lines[i]
        f.write(line)
        if line != len(new_lines)-1:
            f.write("\n") 
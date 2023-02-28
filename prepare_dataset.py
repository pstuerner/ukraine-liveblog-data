
with open("ukraine.txt", "r") as f:
    lines = f.readlines()

lines = [eval(line) for line in lines]
sentences = [f"{line['title']}: {line['text']}" for line in lines]

train_sentences = sentences[:int(len(sentences)*.9)]
val_sentences = sentences[int(len(sentences)*.9):]

with open("ukraine_train.txt", "w") as f:
    for sentence in train_sentences:
        f.write(f"{sentence}\n")

with open("ukraine_val.txt", "w") as f:
    for sentence in val_sentences:
        f.write(f"{sentence}\n")
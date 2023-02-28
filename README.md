# ukraine-liveblog

## The dataset

The "ukraine-liveblog" dataset contains a collection of news articles published on the liveblog of the popular German news website, tagesschau.de. The dataset covers the period from February 2022 to February 2023, and includes every news feed published during this time that covers the ongoing war in Ukraine. You can find the dataset on [HuggingFace](https://huggingface.co/datasets/pstuerner/ukraine-liveblog).

## Data collection

Data gathering is handled with the `download_data.py` script. Replace the `url` variable with the most current URL of tagesschau.de's Ukraine liveblog. Run the script using `python3 download_data.py`. Warning: the script sometimes stops as the tagesschau.de website is not entirely consistent. Line 19 (`a = div.find("a", href=re.compile("liveblog"))`) returns `None` from time to time, although the URL to the previous liveblog exists. In my case, I manually opened the most recently fetched URL, clicked on the previous liveblog (URL at the very bottom) and pasted the URL in line 5. It's a bit of a hack, but only happened a couple times and since it's a one-time dump it was too much effort to fix it.

The script writes stringified JSON objects to a file called `ukraine.txt`. As I said, the script stopped a couple times, which is why I chose to append data to a .txt file instead of writing everything to a binary at the end. However, reading the .txt file is not a problem as we will see in the next step.

## Data preparation
Refer to the `prepare_dataset.py`script to see how to read and handle the raw `ukraine.txt` data. The script simply reads the raw data and turns everything into an actual object using `eval()`. I know it's not a recommended approach but I was only looking for a quick-and-dirty solution that worked :). Afterwards, we split the entire dataset into train (90%) and validation (10%) and write everything to separate .txt files.

## The final data
Here's what you're probably interested in: `ukraine.txt` contains the raw stringified JSON objects, while `ukraine_train.txt` and `ukraine_val.txt` contain the sentences as raw text, line by line.
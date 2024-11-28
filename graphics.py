import matplotlib.pyplot as plt
from textblob import TextBlob
import seaborn as sns

def barGraphic(sentiments):
    """
    Generate a bar chart showing the average sentiment of the comments.
    """
    average_sentiment = sum(sentiments) / len(sentiments)
    plt.bar(["Average Sentiment"], [average_sentiment], color="blue")
    plt.title("Average Sentiment of Comments\n(Example: Average sentiment derived from the analyzed comments)")
    plt.ylabel("Sentiment Polarity (-1 to 1)")
    plt.grid(axis="y")
    plt.show()


def dispersionGraphic(sentiments, texts):
    """
    Generate a scatter plot showing the relationship between the sentiment 
    of the comments and the length of the text.
    """
    text_lengths = [len(text) for text in texts]
    plt.scatter(text_lengths, sentiments, alpha=0.7, color="purple")
    plt.title("Sentiment vs. Text Length\n(Example: Short comments like 'Great!' vs. long reviews)")
    plt.xlabel("Text Length")
    plt.ylabel("Sentiment Polarity (-1 to 1)")
    plt.grid(True)
    plt.show()


def pizzaGraphic(sentiments):
    """
    Generate a pie chart showing the proportion of texts with each sentiment value.
    """
    num_positive = len([sentiment for sentiment in sentiments if sentiment > 0])
    num_negative = len([sentiment for sentiment in sentiments if sentiment < 0])
    num_neutral = len([sentiment for sentiment in sentiments if sentiment == 0])
    labels = ["Positive", "Negative", "Neutral"]
    sizes = [num_positive, num_negative, num_neutral]
    colors = ["green", "red", "gray"]
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title("Distribution of Sentiments\n(Example: Comments classified into positive, negative, or neutral)")
    plt.show()


def warmthGraphic(keywords, texts):
    """
    Generate a heatmap of sentiment values in relation to specific keywords.
    """
    sentiment_matrix = []
    for keyword in keywords:
        row = []
        for text in texts:
            if keyword in text.lower():
                blob = TextBlob(text)
                sentiment = blob.sentiment.polarity
                row.append(sentiment)
            else:
                row.append(0.0)
        sentiment_matrix.append(row)

    sns.heatmap(sentiment_matrix, annot=False, xticklabels=False, yticklabels=keywords, cmap="coolwarm")
    plt.title("Sentiment Heatmap by Keyword\n(Example: Sentiments mapped to specific keywords)")
    plt.show()


def histogram(sentiments):
    """
    Generate a histogram of the sentiment values of the comments.
    """
    plt.hist(sentiments, bins=10, color="skyblue", edgecolor="black")
    plt.title("Distribution of Sentiment in Comments\n(Example: How sentiments are distributed across comments)")
    plt.xlabel("Sentiment Polarity (-1 to 1)")
    plt.ylabel("Number of Comments")
    plt.grid(axis="y")
    plt.show()


def lineGraphic(sentiments):
    """
    Generate a line chart of the sentiment values of the comments.
    """
    plt.plot(sentiments, marker="o", linestyle="-", color="blue")
    plt.title("Variation of Sentiment in Comments\n(Example: Sequential sentiment changes across comments)")
    plt.xlabel("Comment Index")
    plt.ylabel("Sentiment Polarity (-1 to 1)")
    plt.grid(True)
    plt.show()

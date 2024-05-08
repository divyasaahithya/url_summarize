import nltk
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def get_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)

def main():
    # Input URL
    url = input("Enter the URL of the website: ")

    # Get article text from the URL
    article_text = get_article_text(url)

    # Summarize the text
    summary = summarize_text(article_text)

    # Display the summary
    print("\nSummary:")
    print(summary)
    print("FOR FURTHER DETAILS PLEASE VISIT THE WEBSITE!!")
    print("THANK YOU :)")

if __name__ == "__main__":
    main()
#https://timesofindia.indiatimes.com/world/china/china-tightens-grip-over-internet-during-key-political-meeting/articleshow/108362819.cms

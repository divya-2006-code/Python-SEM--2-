#1.

class Password:
    def validate(self,password):
        if len(password) < 8:
            print("Invalid:Minimum length of 8 characters.")
        elif not any(i.isupper() for i in password):
            print("Invalid:At least one uppercase letter.")
        elif not any(i.islower() for i in password):
            print("Invaild:At least one lowercase letter.")
        elif not any(i.isdigit() for i in password):
            print("Invalid:At least one digit.")
        elif not any(i in "@#$%^&*()-_=+[]{};:'\",.<>?/|" for i in password):
            print("Invalid:At least one special character.")
        else:
            print("Valid Password!")

p = input("Enter your password:")
validator = Password()
validator.validate(p)

#2.

class TextProcessor:
    def __init__(self,text):
        self.text = text
    def split_into_sentence(self):
        sentences = []
        sentence = ""
        for char in self.text:
            sentence += char
            if char in ".!?":
                sentences.append(sentence.strip())
                sentence = ""
        return sentences
    def process_sentence(self):
        sentences = self.split_into_sentence()
        print("Processed Sentence Data:")
        for sentence in sentences:
            word_count = len(sentence.split())
            print(f"Sentence:{sentence},Word Count:{word_count}")
para = input("Enter your paragraph:")
txt = TextProcessor(para)
print("Split Sentences:")
sentences = txt.split_into_sentence()
for sentence in sentences:
    print(f"{sentence}")
txt.process_sentence()
    

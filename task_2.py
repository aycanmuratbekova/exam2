
text_ = "Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."

def to_upper_case(textt):
    return textt.upper()


def count_letter(letter):
    letter = letter.lower()
    print(len(list(filter(lambda x: x == letter, text_.lower()))))


def find_word(text_, word_):
    text_ = text_.upper()
    word_ = word_.upper()
    results = [word for word in text_.split(' ') if word_ in word]
    return results


count_letter('t')
count_letter('s')
print(find_word(text_, 'pro'))

print(to_upper_case(text_))

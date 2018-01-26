print("{:-^20}".format(" problem 1 "))
import random

random_num = random.randint(1, 100)

trial_cnt = 0
while True:
    user_input = int(input("Insert number:"))
    trial_cnt += 1

    if random_num > user_input:
        print("높습니다.")
    elif random_num < user_input:
        print("낮습니다.")
    else:
        print("맞췄습니다.")
        print("The number of trial ", trial_cnt)
        break


print("{:-^20}".format(" problem 2 "))
news_str = """
upset Germany's Alexander Zverev in the third round and his idol Novak Djokovic in the fourth.
READ: More Melbourne heartbreak for Nadal
READ: Chung ousts Djokovic
If the 21-year-old defeats defending champion Federer on Friday, he will join Japan's Kei Nishikori -- currently recovering from a wrist injury -- as the only men from Asia to make a grand slam final. Federer earned a 20th win over Tomas Berdych 7-6 (7-1) 6-3 6-4 in Wednesday's night session.
"We all Asian players looking (to) Kei and we trying to follow him," Chung told reporters. "He's the pride of Asian player."
Chung's Djokovic-esque game has wowed fans in Melbourne while his interviews have certainly charmed them, even with Chung still coming to terms with English. He is indeed learning the language, aided by shows like "Prison Break" and a friend from Chicago.

 
What was Hyeon Chung thinking on match point?

"If I win one more point, I make history in Korea."#AusOpen

3:33 PM - Jan 24, 2018
 8 8 Replies   203 203 Retweets   707 707 likes
Twitter Ads info and privacy
But he gets his point across.
Chung endeared himself to the spectators when he admitted he started to think ahead in the last game when he led 40-0, only to have to save two break points.
"I think last game many things come together," he said. "If I win one more point, I make history in Korea. Something I thinking like that. I have to think about the ceremony."
Chung introduced his entourage in his on-court interview, which included his parents and new coach Neville Godwin, who guided Kevin Anderson to last year's US Open final.
Tennis is South Korea's fifth most popular sport, Chung speculated -- it's sure to grow now with his success -- and he got his start thanks to his dad. His father played tennis and so does Chung's brother.


"I'm just trying to copy Novak because he is my idol!"@HyeonChung - 
 1 1 Reply   16 16 Retweets   21 21 likes
Twitter Ads info and privacy
Astigmatism
But another reason he took up the sport was because he suffers from astigmatism -- hence the glasses -- and doctors told him looking at the color green would help his eyesight.
In November, Chung won the inaugural Next Gen ATP Finals championship -- an event to showcase tennis' upcoming players -- and he has carried on that form in the season's first grand slam in Melbourne.
Despite losing to Chung, Djokovic came away impressed.
"He definitely has the game to be a top-10 player, without a doubt," the 12-time grand slam winner said. "How far he can go, that depends on him. Obviously I respect him a lot because he's a hard worker, he's disciplined, he's a nice guy, he's quiet.
"You can see that he cares about his career and his performances. So I'm sure that he's going to get some really good results in the future."
Djokovic and Chung's other opponents have seen him deliver a slew of winners and plenty of grit -- he won the second set on Wednesday despite trailing 5-3.

Federer has never faced Chung but was looking forward to it.
"I'm very excited to play Chung," said the Swiss, who is within grasp of a 20th major. "I thought he played an incredible match against Novak. I mean, to beat him here is one of the tough things to do in our sport, I believe. I know that Novak maybe wasn't at 110% but he was all right. He was giving it a fight till the very end. To close it out that was mighty impressive.
"To bounce back from a Novak match and just somehow get it done today...that's tough. That shows that he's had good composure, a great mindset. Also physically he must have recovered because Novak is going to give you a bit of a workout."
The women's semifinals are set in Melbourne after world No. 1 Simona Halep rallied from 0-3 to crush former No. 1 Karolina Pliskova 6-3 6-2 and Angelique Kerber -- another former No. 1 -- swept past an error prone Madison Keys 6-1 6-2.
READ: Halep's great escape
Halep faces Kerber in a battle of undefeated players in 2018. Second-seed Caroline Wozniacki -- yes she is also another former No. 1 -- plays the unseeded Elise Mertens of Belgium.
Who will the Australian Open? Have your say on our Facebook page
Both are in form, too. Wozniacki won the year-end championships and was a finalist in Auckland this month, with Mertens successfully defending her title in Hobart.
"""
word_cnt_dict = {}
for word in news_str.split():
    word = word.strip(".")
    word = word.strip("?")
    word = word.strip(",")
    word = word.strip('."')
    word = word.lower()

    if not word_cnt_dict.get(word):
        word_cnt_dict[word] = 1
    else:
        word_cnt_dict[word] = word_cnt_dict[word] + 1


for word, cnt in word_cnt_dict.items():
    print(word, cnt)

char_list = []

for c in news_str:
    if c not in list("1234567890"):
        char_list.append(c)

print("".join(char_list))



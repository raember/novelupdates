import unittest
from datetime import datetime, timezone

from urllib3.util import parse_url

from lightnovel.wuxiaworld_com import WuxiaWorldComNovel, WuxiaWorldComChapter, WuxiaWorldComApi
from tests.config import Har, prepare_browser
# noinspection SpellCheckingInspection
from wuxiaworld_com.api import Genre


# noinspection SpellCheckingInspection,DuplicatedCode
class WuxiaWorldComApiHjcTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = prepare_browser(Har.WW_HJC_COVER_C1_2)

    def test_parsing_novel(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change'))
        self.assertIsNotNone(novel)
        self.assertTrue(isinstance(novel, WuxiaWorldComNovel))
        self.assertFalse(novel.success)
        self.assertTrue(novel.parse())
        self.assertTrue(novel.success)
        self.assertEqual('https://www.wuxiaworld.com/novel/heavenly-jewel-change', str(novel.alter_url()))
        self.assertEqual('https://www.wuxiaworld.com', str(novel.alter_url('')))
        self.assertEqual('Heavenly Jewel Change', novel.title)
        self.assertIsNone(novel.author)
        self.assertEqual('Stardu5t', novel.translator)
        self.assertEqual('Copyright © 2018 WuxiaWorld. All rights reserved.', novel.rights)
        self.assertEqual(datetime(2015, 11, 7, 4, 3, 42, tzinfo=timezone.utc), novel.release_date)
        self.assertEqual('/novel/heavenly-jewel-change/hjc-book-1-chapter-1-01', novel.first_chapter.path)
        self.assertListEqual(['Chinese', 'Ongoing'], novel.tags)
        self.assertEqual(
            'https://cdn.wuxiaworld.com/images/covers/hjc.jpg?ver=f83790a5f2ff64bb6524c2cfd207845ba1d25ac6',
            str(novel.cover_url))
        self.assertEqual("\n[Zen’s Synopsis]In a world where power means everything, "
                         "and the strong trample the weak; there was a boy born from a "
                         "Heavenly Jewel Master. Born in a small country which had to "
                         "struggle to survive, the boy was expected to do great things. "
                         "Alas he turned out to have blocked meridians and was unable to "
                         "cultivate, ending up the trash of society. His father’s "
                         "tarnished pride… his fianceé’s ultimate dishonour…Being almost "
                         "accidentally killed and left for the dead, heaven finally "
                         "smiles upon him as a miracle descends, awakening his potential "
                         "as a Heavenly Jewel Master. Or… is it truly a gift?Join our "
                         "dear rascally and shameless MC Zhou Weiqing in his exploits to "
                         "reach the peak of the cultivation world, form an army, "
                         "protect those he loves, and improve his country!An all new "
                         "world, an all new power system, unique weaponry & MC! Come "
                         "join me in laughing and crying together with this new "
                         "masterpiece from Tang Jia San Shao![Translated Synopsis]Every "
                         "human has their Personal Jewel of power, when awakened it can "
                         "either be an Elemental Jewel or Physical Jewel. They circle "
                         "the right and left wrists like bracelets of power.Heavenly "
                         "Jewels are like the twins born, meaning when both Elemental "
                         "and Physical Jewels are Awakened for the same person, "
                         "the pair is known as Heavenly Jewels.Those who have the "
                         "Physical Jewels are known as Physical Jewel Masters, "
                         "those with Elemental Jewels are Elemental Jewel Masters, "
                         "and those who train with Heavenly Jewels are naturally called "
                         "Heavenly Jewel Masters.Heavenly Jewel Masters have a highest "
                         "level of 12 pairs of jewels, as such their training progress "
                         "is known as Heavenly Jewels 12 Changes.Our MC here is an "
                         "archer who has such a pair of Heavenly Jewels.\n",
                         novel.description.text
                         )
        self.assertEqual(7, len(novel.books))
        book = novel.books[0]
        self.assertEqual('Volume 1', book.title)
        self.assertEqual(27, len(book.chapter_entries))
        chapter = book.chapter_entries[0]
        self.assertEqual('Chapter 1 Big Sis, Im afraid this is a misunderstanding! (1)', chapter.title)
        self.assertEqual('/novel/heavenly-jewel-change/hjc-book-1-chapter-1-01', chapter.url.path)
        book = novel.books[1]
        self.assertEqual('Volume 2', book.title)
        self.assertEqual(29, len(book.chapter_entries))
        book = novel.books[2]
        self.assertEqual('Volume 3', book.title)
        self.assertEqual(28, len(book.chapter_entries))
        book = novel.books[3]
        self.assertEqual('Volume 4', book.title)
        self.assertEqual(13, len(book.chapter_entries))
        book = novel.books[4]
        self.assertEqual('Volume 5', book.title)
        self.assertEqual(31, len(book.chapter_entries))
        book = novel.books[5]
        self.assertEqual('Volume 6', book.title)
        self.assertEqual(55, len(book.chapter_entries))
        book = novel.books[6]
        self.assertEqual('Remaining Chapters (To be sorted)', book.title)
        self.assertEqual(697, len(book.chapter_entries))

    def test_parsing_chapter_1(self):
        api = WuxiaWorldComApi(self.browser)
        chapter = api.get_chapter(
            parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-1-chapter-1-01'))
        self.assertIsNotNone(chapter)
        self.assertTrue(isinstance(chapter, WuxiaWorldComChapter))
        self.assertFalse(chapter.success)
        self.assertTrue(chapter.parse())
        self.assertTrue(chapter.success)
        self.assertEqual('https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-1-chapter-1-01',
                         str(chapter.url))
        self.assertEqual('https://www.wuxiaworld.com', str(chapter.alter_url('')))
        self.assertEqual("Chapter 1 – Big Sis, I’m afraid this is a misunderstanding! (1)", chapter.title)
        self.assertEqual('Stardu5t', chapter.translator)
        self.assertEqual(25687, chapter.chapter_id)
        self.assertFalse(chapter.is_teaser)
        self.assertIsNone(chapter.previous_chapter)
        self.assertEqual('/novel/heavenly-jewel-change/hjc-book-1-chapter-1-02', chapter.next_chapter.path)
        self.maxDiff = None
        chapter.clean_content()
        self.assertEqual("""
Heavenly Bow Empire Capital City, Heavenly Bow City, Official Roads.
Heavenly Bow Empire is a small country in the western regions of Boundless Mainland (Hao Miao Da Lu). It isn’t bound to any larger countries, and its environment and climate are extremely suitable for humans to live in.
The weather was great today, the vast expanse of the sky seemed like a large blue crystal, with nary a blemish in sight. The only issue one might find would be that the clarity of the air caused the sunshine to be rather glaring on the eyes. Luckily, the official roads were lined with 100-year or older Sycamore Trees, their thick branches massed with leaves sheltering the wide roadways. This formed the famous boulevard which everyone in Heavenly Bow Empire knew about, stretching for nearly 100 li (50km) into a forest.
Heavenly Bow City had a very unique geographical location, in fact it could be almost described as second-to-none. This was because this capital city was totally surrounded by huge forests, and Heavenly Bow City was just like a brilliant jewel in the midst of the forest. Although Heavenly Bow Empire wasn’t particularly strong, its capital city was still quite famous. The surrounding forests were called Stars Forest, because this was the only place in the whole continent where the Stars Trees grew. The heart of the Stars Trees were extremely valuable materials in making top end bows. As such, with such an important natural resource, one could imagine the prosperity that Heavenly Bow City enjoyed.
Currently, a youth who looked around 15-16 years old was walking along the boulevard, muttering to himself.
“To be a playboy is to train the mind, to have an affair is to train the heart, chasing after girls will prevent old age, flirting is therapeutic, having a crush on someone means your heart will always be young, being lovesick is the cure for insomnia!
They often say that Heroes are unable to cross the beautiful maiden barrier [1. It's a chinese saying that means heroes are often susceptible to a pretty face, causing them to be fallen.], but what hero will think like this? Should the hero leave the beauty to some useless fellow? And what would the beauty think, wouldn’t she prefer to have the hero instead as well?
Another saying is that Rabbits don’t eat the grass near their nests [2. Literal translation of another Chinese idiom, it means that even villains won’t commit sins close to home. However his rant here is talking on the literal meaning of it.], but why would rabbits do that? Should they let other rabbits eat the grass? Even the grass won’t think like that, after all being eaten is being eaten, does it matter by whom? Why not let someone familiar eat them!
Yet another saying is that if you have money, you can make the devil push the millstone for you [3. Money makes the world go round], but the devil would think that it’s a given thing – after all shouldn’t labour of pushing the millstone be rewarded? Even money would think differently, after all, being given to the devil will not harm the devil, but if given to humans the scenario might be different! Hahahaha…”
The youth was tall, with broad shoulders, with a healthy strong look. He had black eyes and hair, and was dressed in a cloth shirt with its sleeves rolled up, showing off his arms. His skin colour was a healthy sheen of bronze, and his features had a heroic spirit within. He might not be very handsome, but was overall pleasing to the eye. Just judging by outward appearance, the words simple and honest would be an apt description. However, the words that streamed out from his mouth were the total opposite of simple and honest. Of course, he only revealed his true colours when there was nobody else around.
“Sigh… not being able to cultivate heavenly energy is such a tragedy. In today’s day and age, looking good is useless, only heavenly energy and heavenly jewels are king. Ahhhh… Heavens! Earth! Gods! Why do you play me like this, letting I, Zhou Weiqing, be born with such a body with blocked meridians yet such a handsome face? Not letting me be a Heavenly Jewel Master is such a waste of great talent ah!” Of course, the handsome face he referred to was only of his own belief, and as he spoke the youth rudely gave the sky the finger.
Of course, he wasn’t the sort to just blame heaven, after pointing the middle finger he said comfortingly to himself: “Oh well, not being able to cultivate Heavenly Energy has its good side as well. That old geezer is already so strict, if I really awakened a Heavenly Jewel, maybe my life would be worse now by a hundred times? At least now the old geezer has given up on me, and leading the decadent life of a rich official’s son seems not a bad choice. I’ll go take a bath now!” As he spoke, his face revealed his trademark honest smile. Of course, those who really knew him, Zhou Weiqing’s honest smile hid his true rascally nature.
Even though Zhou Weiqing was unable to cultivate heavenly energy, his youthful body was still extremely healthy and strong. He was only 13 years old this year, and yet he looked like a youth of 15 – 16. At least in this, he was following in his father’s footsteps.
After walking about 5 li along the boulevard to the Stars Forest, Zhou Weiqing suddenly swerved into the woods. He had grown up in the woods, especially ever since he was 8 years old when he had tested out to have his meridians blocked and unable to cultivate heavenly energy. Zhou Weiqing’s father no longer forced him to train, so his favourite thing to do was to run alone into the forest to play. There were no Heavenly Beasts in the Stars Forest, and it was one of the safest forests on the continent.
After entering the Stars Forest, Zhou Weiqing could practically navigate his way around with his eyes closed, after all he knew the place like the back of his hand. After walking for about an hour, he finally heard sounds of running water as he neared his destination. Thinking about the sweet, clear lakewater, Zhou Weiqing hastened his steps. It was a hot day and he was eager to relax in the cooling waters of the lake.
Not far from the path in the Stars Forest there lay a lake, and its waters originated from an underground ice spring. It was only about 100m in diameter, and was surrounded by large thick trees. As a result, not many people knew about this lake, but Zhou Weiqing had came across it by accident in the past. He had a natural liking for water and since he had no friends, he spent a lot of time bathing and relaxing in the lake.
Moving around a large tree, the Ice Spring Lake was right ahead. Zhou Weiqing did not rush to dive into the waters, but first took off his clothes and laid them at the side, before squatting down at the edge of the waters to look at his reflection, muttering to himself: “Damn! I’ve become more handsome again!”
Just as he was reflecting on his own looks narcissistically, he suddenly heard a splash, causing him to look up, and the sight that greeted him caused him to gape in surprise.
From the other end of the lake, someone else had just jumped into the water, causing the waters to splash out. As the rays of sunshine shone upon the lake, the refraction of light causing the area to seem to be bathed in gold. In the midst of the water ripples, a head of pink hair captured Zhou Weiqing’s attention.
The Ice Spring Lake’s water was pretty shallow, only a metre or so deep, and the young girl who had leapt into the lake had her back facing Zhou Weiqing, and the lake waters just covered her buttocks. Still, Zhou Weiqing was able to see her slim waist and alluring figure.
“This… this…”
With a light *pooh* sound, 2 lines of blood streamed down from Zhou Weiqing’s nostrils. Even though this fellow often had sexual fantasies, he was after all still a 13 year old virgin boy, no matter how precocious. Seeing a naked young girl at such close proximity for the first time was so exciting to him that his nose started bleeding.
“Wow, this is so awesome!” Zhou Weiqing quickly held his nose, but his eyes kept staring at the girl, completely forgetting how exposed he was to being found, he could only chant in his mind Turn around! Turn around!
As if the pink haired girl had heard his internal prayers, she actually slowly turned around, she seemed excited and her hands were on the top of the water as she turned towards Zhou Weiqing.
""".replace('\n', ''),
                         chapter.content.text)

    def test_parsing_chapter_2(self):
        api = WuxiaWorldComApi(self.browser)
        chapter = api.get_chapter(
            parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-1-chapter-1-02'))
        self.assertIsNotNone(chapter)
        self.assertTrue(isinstance(chapter, WuxiaWorldComChapter))
        self.assertFalse(chapter.success)
        self.assertTrue(chapter.parse())
        self.assertTrue(chapter.success)
        self.assertEqual('https://www.wuxiaworld.com/novel/heavenly-jewel-change/hjc-book-1-chapter-1-02',
                         str(chapter.url))
        self.assertEqual('https://www.wuxiaworld.com', str(chapter.alter_url('')))
        self.assertEqual("Chapter 1 – Big Sis, I’m afraid this is a misunderstanding! (2)", chapter.title)
        self.assertEqual('Stardu5t', chapter.translator)
        self.assertEqual(25689, chapter.chapter_id)
        self.assertFalse(chapter.is_teaser)
        self.assertEqual('/novel/heavenly-jewel-change/hjc-book-1-chapter-1-01', chapter.previous_chapter.path)
        self.assertEqual('/novel/heavenly-jewel-change/hjc-book-1-chapter-1-03', chapter.next_chapter.path)
        self.maxDiff = None
        chapter.clean_content()
        self.assertEqual("""
Zhou Weiqing’s eyes widened as his dreams were about to come true. Just at that moment, a feminine voice shouted out “Your highness, be careful! There’s someone here!”
Upon hearing the shout, the pink haired girl acted like a startled little bird, quickly ducking into the water up to her neck, as she looked around in panic.
Before Zhou Weiqing could react, he felt his body lighten, and the world spin around him. With a plopping sound, he landed on the ground.
“What happened?” Although Zhou Weiqing was unable to cultivate heavenly energy, but he had been training under his strict father since young, and his body was in a fit condition, definitely stronger and more agile than any commoner, and he executed a roll on the ground before standing up.
About 3 metres in front of him, a young lady of about 20 years of age stood glaring at him. She seemed rather plain looking, and was dressed in leather armor with a sword in hand, with a bow made of Star Wood holstered on her back.
Zhou Weiqing immediately recognized the symbols of Star Flowers etched upon her leather armor, it was reserved only for the Royal household – could this young lady in front of him be a Royal Guard?
What really drew Zhou Weiqing’s attention was the 3 Jewels surrounding the lady’s right wrist. The 3 jewels were a type of jade, and with Zhou Weiqing’s good vision and the radiance of the jade, he could see clearly that it was about 30% Waxy Jade, 30% Ice Jade and 40% Dragonstone Jade.
Even though Zhou Weiqing personally could not cultivate, but he knew that those 3 jewels on her right wrist were no mere ornaments, but a sign of power.
In the Boundless Mainland, a person’s actual strength could be determined in 3 ways, and if you stood out in any particular way, you could be considered a strong person. The 3 ways were Heavenly Energy, Physical Jewels and Elemental Jewels.
Humans believed that they were the highest ranked species in the world that the gods have created, and that the human body was truly a gift from the gods. There were many different types of cultivating methods, and the strength achieved from that was known as heavenly energy. Heavenly energy was divided into 4 large hierarchies, Heavenly Jing Energy, Heavenly Xu Energy, Heavenly God Energy, and Heavenly Dao Energy.
Each of those hierarchies were further divided into 12 levels. It was rumoured that someone who had reached the highest level of the Heavenly Dao Energy was able to harness the energies of the universe, able to destroy and create and be extremely long lived. In any case, no matter Physical Jewel Masters or Elemental Jewel Masters, the basics of everything was Heavenly Energy. Without sufficient Heavenly Energy, it did not matter how good the quality of the Power Jewels were.
In the huge Boundless Mainland, when humans were born, they all had their own inborn Power Jewel. However, nobody could tell in advance what their Jewel was, and only when Heavenly Energy had been cultivated till the 3rd level of Heavenly Jing Energy, would their Power Jewels be Awakened.
The cultivation of Heavenly Jing Energy was extremely difficult, especially the introductory stages, one had to have the talent to communicate with their own Power Jewels to be able to cultivate successfully. The first 3 levels of Heavenly Jing Energy was tantamount to being reborn 3 times, and less than 1% of the population could actually complete it.
Once someone could complete the first 3 levels of Heavenly Jing Energy cultivation and Awaken their Power Jewels, then they would finally break out of being a commoner and take the first step into being a powerhouse. As Zhou Weiqing had blocked meridians and could not cultivate, thus he was doomed to be unable to complete the first 3 levels and Awaken his Power Jewels, and could only be an ordinary person.
Power Jewels had 2 forms after Awakening. Those that appeared around the right wrist were known as Physical Jewels. Those that appeared around the left wrist were known as Elemental Jewels. Physical Jewels and Elemental Jewels were inherently different. In general those with Physical Jewels were strong warriors, and each Physical Jewel could not only strengthen the physical attributes of the Physical Jewel Master, but also coalesce into a weapon or armor piece, which greatly strengthened the Physical Jewel Master. On the other hand, those with Elemental Jewels were gifted with greater brain energy, and they could make use of their Elemental Jewels to control the various elements they were aligned to, and they could also seal skills into their Elemental Jewels.
For both Physical Jewel Masters and Elemental Jewel Masters, the basic way to tell their strength was the number of jewels. For them, there was a max of 9 Power Jewels, those who had 1-3 Jewels were known as Shi Stage, 4-6 Jewels were known as Zun Stage, and 7-9 Jewels were known as Zong Stage. Each Stage also had an lower, middle and upper level. As such, the lady Royal Guard in front of Zhou Weiqing now was a upper level Shi Stage Physical Jewel Master.
Although Shi Stage was only the first stage, it would be a big mistake to underestimate the 3 Jewelled upper level Shi Stage Physical Jewel Master in front of him. After all, for a small country like Heavenly Bow Empire, the number of Jewel Masters numbered less than a hundred! This lady Royal Guard in front of Zhou Weiqing was probably ranked within the top 50 strongest in the whole country! As such, you can see how rare a Jewel Master was. Having 3 Physical Jewels also meant that her Heavenly Jing Energy was cultivated to at least 10th Level, possibly even already break-through to the Tian Xu Energy hierarchy. With her power, it would be easy for her to defeat a hundred skilled normal soldiers.
Physical Jewels and Elemental Jewels were formed by different types of jewels. For Physical Jewels, they were all formed by different types of Jade, which also meant different types of physical enhancements. There were 6 different type of jade and enhancements, namely: Ice Jade which boosted strength, Waxy Jade which boosted flexibility, Yellow Jade which boosted toughness, Dragonstone Jade which boosted agility, Red Jade which boosted coordination, and Black Jade which boosted stamina.
All Physical Jewel Masters’ jade were a mixture of the different type of jades. With reference to the lady Royal Guard, with 30% Waxy Jade, 30% Ice Jade and 40% Dragonstone Jade, it meant that if the physical enhancement from one Jewel was 100, she would get boosted 30 flexibility, 30 strength and 40 agility. It was quite a good mixture indeed.
Feeling the anger in her eyes with some killing intent, Zhou Weiqing felt his back covered in cold sweat, and he exclaimed quickly: “Big Sis, I’m afraid this is a misunderstanding!”
“Misunderstanding?” The lady Royal Guard shook her wrist and drew her sword . Although she did not activate her 3 Physical Jewels, but her sword shone bright with Heavenly Energy. Her heavenly energy was still unable to be released from the sword, so she was likely still in the Heavenly Jing Energy Hierarchy, as those who had broken through to Heavenly Xu Energy would be able to release heavenly energy from their weapons. Of course, she had not even used her Physical Jewels as they would increase the amount of Heavenly Energy expended. Of course, facing Zhou Weiqing who was an unarmed commoner, it was definitely unnecessary to do so.
With a cold flash, the tip of the sword was resting on Zhou Weiqing’s throat, just a small movement forward would end his life.
“Physical Jewel Master Big Sis, this is really a misunderstanding! Besides, I really didn’t see anything! Please let me go” Zhou Weiqing looked pitifully at the lady Royal Guard, and with his honest looking features, it did seem very convincing.
""".replace('\n', ''),
                         chapter.content.text)


# noinspection SpellCheckingInspection
class WuxiaWorldComApiWmwTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = prepare_browser(Har.WW_WMW_COVER_C1)

    def test_parsing_novel(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/warlock-of-the-magus-world'))
        self.assertIsNotNone(novel)
        self.assertFalse(novel.success)
        self.assertTrue(novel.parse())
        self.assertTrue(novel.success)
        self.assertTrue(isinstance(novel, WuxiaWorldComNovel))
        self.assertEqual('https://www.wuxiaworld.com/novel/warlock-of-the-magus-world', str(novel.url))
        self.assertEqual('https://www.wuxiaworld.com', str(novel.alter_url('')))
        self.assertEqual('Warlock of the Magus World', novel.title)
        self.assertEqual('The Plagiarist', novel.author)
        self.assertEqual('OMA', novel.translator)
        self.assertEqual('Copyright © 2018 WuxiaWorld. All rights reserved.', novel.rights)
        self.assertEqual(datetime(2016, 6, 8), novel.release_date)
        self.assertEqual('/novel/warlock-of-the-magus-world/wmw-chapter-1', novel.first_chapter.path)
        self.assertListEqual(['Chinese', 'Completed', 'Completed Recs'], novel.tags)
        self.assertEqual(
            'https://cdn.wuxiaworld.com/images/covers/wmw.jpg?ver=2839cf223fce0da2ff6da6ae32ab0c4e705eee1a',
            str(novel.cover_url))
        self.assertEqual('\nWhat happens when a scientist from a futuristic world reincarnates in a World of Magic '
                         'and Knights?An awesome MC — that’s what happens!A scientist’s goal is to explore the '
                         'secrets of the universe, and this is exactly what Leylin sets out to do when he is '
                         'reincarnated. Dark, cold and calculating, he makes use of all his resources as he sets off '
                         'on his adventures to meet his goal.Face? Who needs that… Hmmm… that guy seems too powerful '
                         'for me to take on now… I better keep a low profile for now.You want me to help you? Sure… '
                         'but what benefit can I get out of it? Nothing? Bye.Hmmm… that guy looks like he might cause '
                         'me problems in the future. Should I let him off for now and let him grow into someone that '
                         'can threaten me….. Nahhh. *kill*\n',
                         novel.description.text
                         )
        self.assertEqual(6, len(novel.books))
        book = novel.books[0]
        self.assertEqual('Transmigration', book.title)
        self.assertEqual(287, len(book.chapter_entries))
        chapter = book.chapter_entries[0]
        self.assertEqual('Chapter 1', chapter.title)
        self.assertEqual('/novel/warlock-of-the-magus-world/wmw-chapter-1', chapter.url.path)
        book = novel.books[1]
        self.assertEqual('Twilight Zone', book.title)
        self.assertEqual(104, len(book.chapter_entries))
        book = novel.books[2]
        self.assertEqual('Morning Star Chronicles', book.title)
        self.assertEqual(237, len(book.chapter_entries))
        book = novel.books[3]
        self.assertEqual('Passage of Bloodlines', book.title)
        self.assertEqual(158, len(book.chapter_entries))
        book = novel.books[4]
        self.assertEqual('World of Gods', book.title)
        self.assertEqual(257, len(book.chapter_entries))
        book = novel.books[5]
        self.assertEqual('Final War', book.title)
        self.assertEqual(157, len(book.chapter_entries))

    def test_parsing_chapter_1(self):
        api = WuxiaWorldComApi(self.browser)
        chapter = api.get_chapter(
            parse_url('https://www.wuxiaworld.com/novel/warlock-of-the-magus-world/wmw-chapter-1'))
        self.assertIsNotNone(chapter)
        self.assertTrue(isinstance(chapter, WuxiaWorldComChapter))
        self.assertFalse(chapter.success)
        self.assertTrue(chapter.parse())
        self.assertTrue(chapter.success)
        self.assertEqual('https://www.wuxiaworld.com/novel/warlock-of-the-magus-world/wmw-chapter-1',
                         str(chapter.url))
        self.assertEqual('https://www.wuxiaworld.com', str(chapter.alter_url('')))
        self.assertEqual("Chapter 1", chapter.title)
        self.assertEqual('/novel/warlock-of-the-magus-world/wmw-chapter-1', chapter.url.path)
        self.assertEqual('OMA', chapter.translator)
        self.assertEqual(9107, chapter.chapter_id)
        self.assertFalse(chapter.is_teaser)
        self.assertIsNone(chapter.previous_chapter)
        self.assertEqual('/novel/warlock-of-the-magus-world/wmw-chapter-2', chapter.next_chapter.path)
        self.maxDiff = None
        chapter.clean_content()
        self.assertEqual("""
Reincarnation
‘My head really hurts….’
This was Fang Ming’s first thought upon waking up. It felt as if there was a cut on his head, hurting so badly that it seemed as if his skull was about to crack apart.
As his consciousness cleared, he realised he was riding on what seemed like a horse carriage. His body bounced along to the rhythm of the moving carriage, sending shockwaves through the wound. The pain was so great that he had to suck in several sharp breaths.
Opening his eyes, he surveyed his surroundings.
What filled his vision were walls formed from hollowed planks. Sharing this carriage with him were quite a few fair-haired and blue-eyed youths, their eyes closed in their reverie. Not one of them bothered to spare a glance in his direction.
He seemed to be lying down on the floor of the carriage. Feeling the biting cold from the wood, Fang Ming realised that his body would not be able to bear lying down much longer. To avoid catching a cold, he struggled hard to get up in a hurry.
At that moment, he felt a sharp pain lancing through his head.
The pain was sudden, and brought with it a flood of strange memories. Fang Ming’s eyes rolled back as he fainted.
“Leylin... Leylin! Wake up…” Fang Ming heard in his daze, and couldn’t help but open his eyes.
‘Is this… reincarnation?’ He still clearly remembered the dazzling flames from the energy reactor’s explosion, one that was impossible to survive with his lack of protection. On top of that, this type of carriage made of wooden planks was considered an ancient antique in his old world, and would definitely not be used.
After organising the new memories in his mind, Fang Ming gained some insight about his body and this world.
This realm was in an era that was similar to the European Middle Ages. But there was something more to this world than that, the presence of a mysterious force. The presence… of magic.
The original owner of his current body was called Leylin Farlier, and he was the son of a minor noble. He had been tested to be gifted with the talent to become a Magus and as such his father, Viscount John Farlier, had pulled strings to allow him to become a magician-in-training, an acolyte. The horse carriage he was currently on was travelling towards a magic academy.
The one who had woken him up was a large, male youth.
His large eyes were surrounded by his thick eyebrows which complemented his long, straight nose and sparkling gold hair. Although his face was somewhat tender, showing his youth, he had a sturdy, muscular body. He looked extremely manly.
Seeing that Fang Ming had awoken, the boy laughed happily, “Haha… Leylin, you’re finally awake! If you had been even a few minutes late, you probably wouldn’t have made it to dinner. You don’t want to starve, do you?”
Fang Ming lowered his eyes. After some thought, he figured out this person’s identity, “Thanks, George!”
All the youths on this carriage had been tested to be gifted with magic. George was a Count’s legitimate son, and a favoured one at that. When his gift was revealed, the Count spent a lot of resources and pulled many strings in order to enter a magic academy.
‘A Count?’ Fang Ming inwardly thought.
His memories returned to Leylin’s father, Viscount John Farlier. His lands were about as large as a single city from Fang Ming’s previous life, and he had thousands of soldiers under his command.
In this world, noble rankings were inexorably tied to personal strength. George’s father being a count meant that his holdings were likely the size of at least several cities, and his annual income was a few thousand gold coins. And even with such finances and power at his disposal, it had taken a lot of effort for him to get George on this carriage. Fang Ming couldn’t help but wonder how Leylin’s father managed to do the same for him.
Even as he began to ponder the question, another sharp pain jolted through his head, and another scene appeared in his mind’s eye.
He was in a dark room, with the musty old shelves lining the sides filled with a sense of antiquity. The surroundings were chock full of dust.
Under dim light, John Farlier solemnly passed him a ring, saying, “Leylin, my dear son, this is our Farlier Family’s heirloom, a promise from a Magus. Your grandfather had once helped an injured Magus out, and in return, he gifted him this ring.
“This ring is a promise. If any of your grandfather’s descendants had the gift of magic, they could use this ring to enter a magic academy for free! I give this to you, now, in hopes that you can be the pride of the Farlier Family and uphold our legacy…”
‘The ring!’ Fang Ming’s eyes narrowed, and his right hand subconsciously moved to his chest.
As his hand touched his clothing, he could feel a solid underneath, the metal ring was still there.
Heaving a sigh of relief in his heart, he thought to himself, ‘Phew! Either those guys didn’t recognise this as a treasure, or there’s a restriction of sorts. Either way, thank goodness this wasn’t snatched away.’
Fang Ming was a scientist in his former life, and the very mention of such a mysterious force as magic filled him with a desire to conduct some research about it.
Furthermore, he didn’t want to be chased back home because he had lost such an important proof of entry.
Although he had taken over this body and even its memories, he was still very different from the original Leylin. His family members, who had spent years with him, would easily be able to tell the difference. If they mistook him as being possessed by a demon and perhaps begged one of those mysterious Magi to investigate, it was extremely likely that he would be found out.
‘However, if I can enter a magic academy, I probably won’t return for at least several years. By that time, any changes in behaviour will be written off as par for the course. Magi are known to be strange and eccentric. At that point, it would be strange if I hadn’t changed at all, not if I had!’
Just as he was in deep thought, a pair of strong large hands suddenly assisted him to his feet.
“What are you thinking about?” George asked.
“No– Nothing!” Fang Ming quickly shook his head, but then held onto it once more, still in pain.
He suddenly spun his head around and looked at George, causing the boy’s heart to stop in its tracks. He felt as if he was being stared at by a venomous snake.
Fang Ming rolled his eyes and asked, “Dearest George, why didn’t you wake me up earlier, instead letting me just lie on the floor like that for so long?”
“Heh heh! I saw you having such a nice sleep, and thought you liked lying down there!” George scratched his head abashedly. However, his eyes sparked with a cunning gleam.
Under Fang Ming’s murderous glare, he finally raised his hands in surrender, “Fine! Fine! Who asked you to offend my goddess. Offending her is still fine; as your bro, I am not such a petty person. Alas, the entire carriage is now treating you like an enemy, and I don’t want to be isolated too!”
‘Offend? Goddess?’ Fang Ming scratched his head, but then he suddenly remembered why he was beaten up.
It was a girl named Bessita. Although she was only 15 years of age, her body was already well-developed and voluptuous. In addition to her big watery eyes, it was a huge draw to the lecherous Leylin.
The original Leylin was no gentleman. He had lost his virginity at the age of twelve, and after that, he had either seduced or forced his way with many others, and had by now slept with more than a hundred women! He had been known as the scourge of his father’s holdings.
As Fang Ming finished exploring the memories, he rolled his eyes once again in disdain. No wonder this body was so weak and frail, it wasn’t just because of the injuries.
Thinking back, it was clear that Leylin had been too used to causing trouble in his own territory, and hadn’t been able to control himself when he saw Bessita.
The first few times it was still rather normal; flirting and making passes at her. Near the end, however, he had resorted to violent means. When Fang Ming saw these memories, he couldn’t help but label the original as an idiot.
That Bessita was the princess of a small country! And Leylin still wanted to rape her. Was there a brain in his skull or was it just dirt? Sheesh!
What happened after went without saying– Leylin was taught a savage lesson by a bunch of ‘Flower Guardians’, eventually succumbing to the injuries. This had eventually benefitted Fang Ming.
‘Heh, this Bessita isn’t as simple as she appears. Such a scheming mind!’ Fang Ming laughed coldly at this thought.
‘Fine. No matter what, I have taken over your body. If I get the chance, I’ll avenge you. After all, I’m now Leylin Farlier!’ Fang Ming swore in his heart.
Leylin found no mention of anything resembling Asians in his memories, nor had he heard anything about China. In this new western world, using his own Chinese name would be too dangerous!
Leylin looked around to find that there was nobody else inside the spacious carriage. It was no wonder that George had come to call him over.
“No matter what, I still have to thank you! George, do you have any medicine?” Fang Ming stood up and stretched his body. Although it still hurt in a few places, it did not impede his movements, and the wound at the back of his head had already become a scab.
“Heh heh…I knew that you’d need this!” George laughed as he tossed a small bottle over, “This is my family’s secret product. I heard that it’s usually used during Knight training, and is extremely effective against any bodily injuries!”
As George spoke, he looked around furtively, “Alright! Dinner is about to start. I’m going to head there first, you should apply the medicine quickly and hurry over too. Remember, do not tell anyone else about our friendship!”
After he finished speaking, he had run off like a gust of wind!
Looking at George’s figure disappearing into the distance, Leylin couldn’t help but massage his forehead. It looked like this Leylin had truly stirred up a hornet’s nest. Was it such a big deal? His memories told him that the people of this world were rather open about sex…
At this point, he couldn’t do anything to remedy the situation. Swiftly taking off his clothes, Leylin quickly rubbed the medicine all over the injuries on his body.
“Hss… This damned George. Couldn’t he help me apply the medicine before leaving?” Leylin drew several sharp cold breaths as he applied the medicine.
The medicine was extremely effective. As soon as he applied it, there was a cooling sensation and the pain vanished.
After he had dealt with the wounds on his body, Leylin put on his clothes and opened the carriage door.
*Whoosh!* A gentle breeze blew over. The sun was setting on the horizon, painting everything a golden red.
Leylin’s eyes moistened as he muttered, “No matter what, it feels good to be alive!”
Looking at the surroundings, he noticed several large carriages forming a circle to make a crude temporary campsite. There was a large fire in the middle.
There were many youths around the fire, sitting and resting on cloth mats laid on the ground. They were laughing and playing with each other while eating the bread in their hands.
Leylin walked towards a table that had quite a few breads and juices placed on it. According to his memories, this was where food was distributed.
When he approached the area, he saw that there were a few people queuing up. As they spotted Leylin, their gazes turned to ones of derision.Although Leylin thought of himself as thick-skinned, he still found it somewhat difficult to endure.
Still, he did not leave. No matter what, he still had to eat.
“Hurry up!” A hoarse voice rang out.
“So… Sorry, Lady Angelia!” A freckled boy quickly apologised and took his share of the food before running away.
[Beep! Danger Alert! Danger Alert! Host body is extremely close to a source of danger. It is recommended to move at least 1000 metres away!]
""".replace('\n', ''),
                         chapter.content.text)


# noinspection SpellCheckingInspection,DuplicatedCode
class WuxiaWorldComApiSFFTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = prepare_browser(Har.WW_SFF_Cover_C1_78F)

    def test_parsing_novel(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/stop-friendly-fire'))
        self.assertIsNotNone(novel)
        self.assertTrue(isinstance(novel, WuxiaWorldComNovel))
        self.assertFalse(novel.success)
        self.assertTrue(novel.parse())
        self.assertTrue(novel.success)
        self.assertFalse(novel.karma_active)
        self.assertEqual('https://www.wuxiaworld.com', str(novel.alter_url('')))
        self.assertEqual('/novel/stop-friendly-fire', novel.url.path)
        self.assertEqual('https://www.wuxiaworld.com/novel/stop-friendly-fire', str(novel.alter_url()))
        self.assertEqual('Stop, Friendly Fire!', novel.title)
        self.assertEqual('Toy Car (토이카)', novel.author)
        self.assertEqual('Boko', novel.translator)
        self.assertEqual('Copyright © 2018 WuxiaWorld. All rights reserved.', novel.rights)
        self.assertEqual(datetime(2018, 9, 17), novel.release_date)
        self.assertEqual('/novel/stop-friendly-fire/sff-chapter-1', novel.first_chapter.path)
        self.assertListEqual(['Completed', 'Korean'], novel.tags)
        self.assertEqual(
            'https://cdn.wuxiaworld.com/images/covers/sff.jpg?ver=071937f5ef5b2d5c24cf1ae552850cd19f4b837d',
            str(novel.cover_url))
        self.assertEqual('\nThe empire has turned into the land of the undead due to a spell gone wrong. God summoned '
                         'heroes from countless worlds to purify the empire and plant new hope. Lee Shin Woo, '
                         'an ordinary earthling, was also summoned. As an undead, that is.\xa0\n',
                         novel.description.text
                         )
        self.assertEqual(13, len(novel.books))
        book = novel.books[0]
        self.assertEqual('Volume 1', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        chapter = book.chapter_entries[0]
        self.assertEqual('Prologue. This Trade is a Draw', chapter.title)
        self.assertEqual('/novel/stop-friendly-fire/sff-chapter-1', chapter.url.path)
        book = novel.books[1]
        self.assertEqual('Volume 2', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[2]
        self.assertEqual('Volume 3', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[3]
        self.assertEqual('Volume 4', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[4]
        self.assertEqual('Volume 5', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[5]
        self.assertEqual('Volume 6', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[6]
        self.assertEqual('Volume 7', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[7]
        self.assertEqual('Volume 8', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[8]
        self.assertEqual('Volume 9', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[9]
        self.assertEqual('Volume 10', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[10]
        self.assertEqual('Volume 11', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[11]
        self.assertEqual('Volume 12', book.title)
        self.assertEqual(23, len(book.chapter_entries))
        book = novel.books[12]
        self.assertEqual('Volume 13', book.title)
        self.assertEqual(26, len(book.chapter_entries))

    def test_parsing_chapter_1(self):
        api = WuxiaWorldComApi(self.browser)
        chapter = api.get_chapter(parse_url('https://www.wuxiaworld.com/novel/stop-friendly-fire/sff-chapter-1'))
        self.assertIsNotNone(chapter)
        self.assertTrue(isinstance(chapter, WuxiaWorldComChapter))
        self.assertFalse(chapter.success)
        self.assertTrue(chapter.parse())
        self.assertTrue(chapter.success)
        self.assertEqual('https://www.wuxiaworld.com/novel/stop-friendly-fire/sff-chapter-1', str(chapter.url))
        self.assertEqual('https://www.wuxiaworld.com', str(chapter.alter_url('')))
        self.assertEqual("Prologue. This Trade is a Draw", chapter.title)
        self.assertEqual('/novel/stop-friendly-fire/sff-chapter-1', chapter.url.path)
        self.assertEqual('Boko', chapter.translator)
        self.assertEqual(63263, chapter.chapter_id)
        self.assertFalse(chapter.is_teaser)
        self.assertIsNone(chapter.previous_chapter)
        self.assertEqual('/novel/stop-friendly-fire/sff-chapter-2', chapter.next_chapter.path)
        self.maxDiff = None
        chapter.clean_content()
        self.assertEqual("""
"Now, let's clear things up."
The woman put down the tobacco pipe she had been gently biting down on, puffed out the smoke, and licked her lips. She was a beautiful woman with striking red, wavy hair, but more importantly was the fact that she was a 'god'.\xA0
"So, what you desire is... an immortal body and infinite growth potential?"
"Yes!"
"Nope, not possible. Go back."
"Aw, don't be like that."
The man, a 27-year-old man called Lee Shin Woo, sat opposite from the woman, separated by an antique desk. He was an ordinary office worker who liked fantasy novels and games. Well, at least until he died.\xA0
And now that he'd died, he was a hero that had been chosen by a god. Probably.\xA0
"I heard that I still had a long life ahead of me, yet I died prematurely. Shouldn’t I receive at least this much from a god since I died so unfairly?"
"Jeez, the novels these days have really spoilt these kids' backbone. Before, if I told them they were getting a second chance, they would go 'yippee' or yell 'call'."
"Well, people change as the times go by."
Though God wanted to hit Lee Shin Woo, who had nonchalantly nodded his head and replied to her, she restrained herself. After all, it was none other than her who had gathered the souls of those who had died unfairly, because she needed their help.\xA0
'If he was from my world, then I would've just...'
She was certainly a god, but she wasn't the god of Earth. She was the god who reigned over Heguroa, which differed in culture, history, size, and every other aspect from Earth.\xA0
Then why was she in a situation where she had to bring souls from another world? There was a truly sad, tear-jerking reason behind that.\xA0
"Anyhow, those guys sure are cold-hearted. Their god is saying that she'll get herself involved and clean up their mess, but they're just avoiding it since they don't want to die."
"There were a lot of heroes who accepted my revelation, you know!? ...They all just died in Heita."
Lee Shin Woo instinctively gulped and asked God.
"... Is the place that dangerous?"
"Of course, it is."
God couldn't hide her bitterness, and responded for a second time, putting the tobacco pipe back into her mouth. If she didn't at least do that, she felt like she would've sighed in front of a human.
This was a story that happened several decades ago. Heita, a great empire that thrived in the undergrounds of Heguroa, was met with tragedy. Their emperor, Jissehanu, dreamt of immortality and researched forbidden black magic, but as a consequence of his recklessness... the entire underground empire received an undead curse.
What's worse, the curse would spread gradually, and if left unchecked, would devour the entire world.\xA0
God, recognizing the severity of the situation, passed down a divine revelation to all humans and promised that she would grant a wish to the savior of the Empire.\xA0
There were many heroic men who came forward. But all of them failed. The curse deeply rooted in the Empire was strong, and the heroes who headed underground in order to save the Empire couldn't overcome the curse, degenerating into the undead, and becoming a part of the undead empire.\xA0
Only after did God decide to exhibit her power more extensively. She scattered and planted her power across the Empire, encouraging the heroes, but it didn't help. The influence of the Empire, which sought to lead all life to undeath, gradually increased, and devoured half of the continent...
And that's when God, unable to endure any further, decided that she had to stop the Empire, even if it meant dragging heroes from other worlds. Lee Shin Woo was also one of them.\xA0
"Still, an immortal body is impossible. Ask for something else."
"Then please give me something similar."
"Listen, kid."
God raised her tobacco pipe and pointed at Lee Shin Woo's shabby soul as she explained.\xA0
"Tremendous power burdens the owner. An immortal body? Infinite growth potential? You won't be able to handle such power, and you'll just explode and die. So, go on and offer more realistic, and fitting conditions."
"But with a realistic and fitting power, I'll probably end up like my seniors, dying without being able to do anything."
"..."
At that moment, the human's words thrust deep into the god's heart. Right now, Lee Shin Woo was practically declaring to the god that her 'struggles were meaningless'. Why should I hear this from a mere hero candidate? Should I just kill him? God momentarily felt the impulse to do just that, but... changed her mind upon seeing the human's challenging expression.\xA0
This kid would have to go through hell before he could even understand her a little.
"Alright, I'll do as you ask."
"Yeah!"
"Of course, a perfect immortal body is impossible. You won't die ordinarily, but you'll still die in deadly situations."
"What about the infinite growth potential?"
"That's also up to you, but I'll make it so it's theoretically possible."
"Oh!"
"In exchange."
God flicked her tobacco pipe, and ash flew through the air.\xA0
"You'll lose something very important. Your normal, physical body can't accept that power."
"What exactly is that important thing? I'm not going to become impotent, or become bald, am I?"
"This is the best I can do. Now... Lee Shin Woo. Are you going to do it, or not?"
She didn't answer his question. He faced God's spiteful, cold eyes, and he briefly felt conflicted, but.... he ultimately nodded his head and spoke. Even if he were to become impotent, or become bald, there's a time when a man needs to take the risk!
"Alright, I'll do it!"
"Fine, then our contract has been established."
God put the pipe into her mouth again, and simultaneously, Lee Shin Woo's body was enveloped in a bright light. Transmission magic that would transport his soul to the Heita Empire had been activated.\xA0
"You'll be sent to the entrance of the Empire. Once you arrive there, I won't be able to help you directly, but I'll send you quests instead. You know what quests are, right?"
"Yes."
"Good, and when you arrive, remember to check your status first. It's really important that you know who 'you' are."
"Ok...?"
It seemed as though God had grinned and laughed wickedly when she put the tobacco pipe into her mouth, but... he was soon shrouded by a bright light and was unable to see anything.\xA0
In the next moment, the light disappeared, and Lee Shin Woo's body was dumped onto the cold floor. The transfer was done in the blink of an eye.\xA0
"Oof! She could have let me down a little more gently... hoo."
Lee Shin Woo grumbled softly and stood up. He had been dumped into an enormous underground cave, as expected of an underground empire.\xA0
There was a passageway on both of his sides, and it felt eerie as if mummies would pop out at any minute from all sides. At least there weren't any enemies nearby.\xA0
"I was ready for this, but... this feels really serious... it's cold, too."
He felt cold, perhaps because he didn't have any clothes on. He stroked his skin in order to soothe the cold, but he soon realized that something was off.
"Huh?"
His body was hard. The hand that had touched his body was also really hard. When he raised his hand to see what was going on, there were bones, rather than a human hand.\xA0
"...Huh?"
Shin Woo was so shocked that he went stiff for a while. He somehow got a hold of himself, and when he moved his hand, the bones naturally bobbed. The five fingers composed of bone truly began to dance rhythmically in the air.\xA0
"Hahaha... no way. Haha, this guy."
It was such an unrealistic sight that he laughed automatically. For the first time, Lee Shin Woo bowed his head and observed his body, but his entire body was obviously all bone.\xA0
"..."
The moment he saw that his mind blanked.\xA0
What do I do? Is this by any chance God's mistake? Did I perhaps receive the Empire's curse as soon as I arrived, and became an undead? Then, he remembered what God had said before their sudden parting.
"That's it. Status... She told me to check my status as soon as I arrived."
The moment Shin Woo said the word status, as though he had just grabbed onto a final strand of hope, a strange row of text was engraved in the air in front of him. It was similar to what he had often seen in the games when he was alive. Yeah, even the contents written within...
[Lee Shin Woo]
[Normal Skeleton Blessed by God]
[Lv - 1]
[Strength - 13, Agility - 13, Health - 13, Magic - 3]
[Passive skills - Invisible Heart Lv1]
[Active skills - Bone Reinforcement Lv1]
"..."
The wind passed by his smooth (bald) skull, and his empty (impotent) crotch.\xA0
It only took around... 10 minutes before Lee Shin Woo figured out that this was neither God's mistake, nor the Empire's curse.
""".replace('\n', ''),
                         chapter.content.text)


# noinspection SpellCheckingInspection
class WuxiaWorldComApiASTTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = prepare_browser(Har.WW_AST_Cover_C1_102)

    def test_parsing_novel(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/ancient-strengthening-technique'))
        self.assertIsNotNone(novel)
        self.assertTrue(isinstance(novel, WuxiaWorldComNovel))
        self.assertFalse(novel.success)
        self.assertTrue(novel.parse())
        self.assertTrue(novel.success)
        self.assertTrue(novel.karma_active)
        self.assertEqual('https://www.wuxiaworld.com', str(novel.alter_url('')))
        self.assertEqual('/novel/ancient-strengthening-technique', novel.url.path)
        self.assertEqual('https://www.wuxiaworld.com/novel/ancient-strengthening-technique', str(novel.alter_url()))
        self.assertEqual('Ancient Strengthening Technique', novel.title)
        self.assertEqual('I Am Superfluous', novel.author)
        self.assertEqual('lordbluefire_98448380', novel.translator)
        self.assertEqual('Copyright © 2018 WuxiaWorld. All rights reserved.', novel.rights)
        self.assertEqual(datetime(2016, 11, 30, 0, 0), novel.release_date)
        self.assertEqual('/novel/ancient-strengthening-technique/ast-chapter-1', novel.first_chapter.path)
        self.assertListEqual(['Chinese', 'Completed', 'Completed Recs'], novel.tags)
        self.assertEqual(
            'https://cdn.wuxiaworld.com/images/covers/ast.jpg?ver=3113ede98eb17afea8006f0024b2290aecd68c05',
            str(novel.cover_url))
        self.maxDiff = None
        self.assertEqual("\nSynopsis:"
                         "A human warrior cultivating the Ancient Strengthening Technique has transcended dimensions "
                         "and arrived on Kyushu. Together with twelve ravishing beauties with looks that were "
                         "unmatched in their generation, will he be able to stand on the summit of this world?"
                         "This novel is about the main character, named Qing Shui, who transcended dimensions and "
                         "arrived in the world of nine continents. Storms of blood and wind, resulting in corpses and "
                         "bones strewn about are extremely common here. The young warrior Qing Shui forged ahead in "
                         "his path to cultivate, using 10 years to train himself, only to seek vengeance for the one "
                         "who had forsaken his mother! On the road, he had a chance encounter with the cold beauty ("
                         "ice princess) Shi Qing Zhuang, incurring hatred and vengeance from her fiancée – Situ Bu "
                         "Fan. After entering the Hundred Miles City, Qing Shui got acquainted with a dignified and "
                         "beautiful lady named Yu He and other Xian Tian Realm cultivators – After which, "
                         "he willingly invited tribulation on himself, after killing the young master of the Gong "
                         "Yang Clan because of Yu He, and was forced into a corner. Luckily for Qing Shui, "
                         "a lady as beautiful as a celestial maiden named Yi Ye Jian Ge rushed back to save him from "
                         "afar, following which a bloody battle ensued. Can Qing Shui turn danger into safety, "
                         "averting disaster? And his relationships with the various beautiful ladies, what will it "
                         "develop into?\n",
                         novel.description.text
                         )
        self.assertEqual(16, len(novel.books))
        book = novel.books[0]
        self.assertEqual('Vol 1: Divine Strength Awakened, Mysteries of his birth', book.title)
        self.assertEqual(113, len(book.chapter_entries))
        chapter = book.chapter_entries[0]
        self.assertEqual('Chapter 1 - Qing Clan, Qing Shui', chapter.title)
        self.assertEqual('/novel/ancient-strengthening-technique/ast-chapter-1', chapter.url.path)
        book = novel.books[1]
        self.assertEqual('Vol 2: Legend of the Hundred Miles City, Peerless and Independent', book.title)
        self.assertEqual(46, len(book.chapter_entries))
        book = novel.books[2]
        self.assertEqual('Vol 3: The Resplendent Fireworks, Mountains and Sea as a Portrait', book.title)
        self.assertEqual(83, len(book.chapter_entries))
        book = novel.books[3]
        self.assertEqual('Vol 4: Tears of a Beauty destroying the kingdom, the Twelve Portraits of Beauties',
                         book.title)
        self.assertEqual(98, len(book.chapter_entries))
        book = novel.books[4]
        self.assertEqual('Vol 5: Greencloud Continent of the Nine Continents, Stepping into the Yan Clan', book.title)
        self.assertEqual(101, len(book.chapter_entries))
        book = novel.books[5]
        self.assertEqual('Vol 6: Aura of a King, Sword pointing to the Dome of Heavens', book.title)
        self.assertEqual(65, len(book.chapter_entries))
        book = novel.books[6]
        self.assertEqual('Vol 7: Path of a Martial Saint, Heart of the Strong', book.title)
        self.assertEqual(86, len(book.chapter_entries))
        book = novel.books[7]
        self.assertEqual('Vol 8: The Prosperous Central Continent, The Journey Across It', book.title)
        self.assertEqual(150, len(book.chapter_entries))
        book = novel.books[8]
        self.assertEqual('Vol 9: Southern Viewing Continent, Hatred of the Previous Years', book.title)
        self.assertEqual(80, len(book.chapter_entries))
        book = novel.books[9]
        self.assertEqual('Vol 10: Eastern Victory Divine Continent, Exquisite Bell Spirit', book.title)
        self.assertEqual(110, len(book.chapter_entries))
        book = novel.books[10]
        self.assertEqual('Vol 11: Storm in the Fifth Continent, The Northern Sacred Lu Continent', book.title)
        self.assertEqual(125, len(book.chapter_entries))
        book = novel.books[11]
        self.assertEqual(
            'Vol 12: Stepping on Lion King Ridge, Trampling with such force until the mountains and rivers crumble',
            book.title)
        self.assertEqual(74, len(book.chapter_entries))
        book = novel.books[12]
        self.assertEqual(
            'Vol 13: Arriving at the Four Continents, Hundred Dynasties, Hundred States. The path of a State Master',
            book.title)
        self.assertEqual(178, len(book.chapter_entries))
        book = novel.books[13]
        self.assertEqual('Vol 14: Soaring Dragon, Dancing Phoenix, Haohan Continent', book.title)
        self.assertEqual(280, len(book.chapter_entries))
        book = novel.books[14]
        self.assertEqual('Vol 15: Demons & Monsters Dancing In Riotous Reverly, Beautiful Women Are Like Poetry',
                         book.title)
        self.assertEqual(200, len(book.chapter_entries))
        book = novel.books[15]
        self.assertEqual('Vol 16 (Final): Oceanic Grand World, Legend of the Nine Continents!', book.title)
        self.assertEqual(700, len(book.chapter_entries))

    def test_parsing_chapter_1(self):
        api = WuxiaWorldComApi(self.browser)
        chapter = api.get_chapter(
            parse_url('https://www.wuxiaworld.com/novel/ancient-strengthening-technique/ast-chapter-1'))
        self.assertIsNotNone(chapter)
        self.assertTrue(isinstance(chapter, WuxiaWorldComChapter))
        self.assertFalse(chapter.success)
        self.assertTrue(chapter.parse())
        self.assertTrue(chapter.success)
        self.assertEqual('https://www.wuxiaworld.com/novel/ancient-strengthening-technique/ast-chapter-1',
                         str(chapter.url))
        self.assertEqual('https://www.wuxiaworld.com', str(chapter.alter_url('')))
        self.assertEqual("Chapter 1 - Qing Clan, Qing Shui", chapter.title)
        self.assertEqual('/novel/ancient-strengthening-technique/ast-chapter-1', chapter.url.path)
        self.assertEqual('lordbluefire_98448380', chapter.translator)
        self.assertEqual(14875, chapter.chapter_id)
        self.assertFalse(chapter.is_teaser)
        self.assertFalse(chapter.karma_locked)
        self.assertIsNone(chapter.previous_chapter)
        self.assertEqual('/novel/ancient-strengthening-technique/ast-chapter-2', chapter.next_chapter.path)
        self.maxDiff = None
        chapter.clean_content()
        self.assertEqual("""
This is a small village surrounded by hills and mountains, the scenery is breathtaking. The village’s surroundings are filled with the abundance of flora and fauna. Even the quality of the air here is fragrant beyond comparison.

Sitting atop of a hillside, was a little boy, roughly about five years old. The little boy was frail and weak, with a very thin physique. Currently, the little boy was in a daze. If anyone was to look at the little boy at this moment, they would be flabbergasted! He could be considered considerably good looking, with that delicate small face and a pair of beautiful black eyes, but in this instance, the sorrowful expression in his eyes was not fitting for his age. It was a look that no ordinary five years old should be able to emulate.

“It has been five years.. Why did I appear in this world? This world and my original world are drastically different, I’m even unsure of what era of history this place belongs to, the only thing I know is that this continent is called Kyushuu.

“Everyone in my current family has the capability to practice martial arts. Why is it that I am a useless trash that is unable to cultivate?” Qing Shui mumbled. The moment there were any hints of strenuous exercise, he would get exhausted, have to gasp for air, palpitations in his heart and even fall unconscious!

“I was originally playing Western Fantasy [1] with my classmates. How on earth did I suddenly end up in this world!?”

“Qing Shui! Qing Shui!” The voice of a woman sounded. Upon hearing it, Qing Shui gradually recovered from his melancholy and regained the bright-eyed naive look of a 5 year old child.

“Mum, I am here!” After he said that he waved his hands and quickly ran towards a woman who excluded a charm that was distinctively different from any ordinary village women.

“Child, why did you travel so far to play? If you want to go that far in the future, let me accompany you, alright?” Holding his hands, the woman smiled with a tender look in her eyes as she gently berated Qing Shui.

Qing Shui felt warmth in his heart. When he came to this world, he was still a fetus developing inside the woman’s body. Now that five years had passed, Qing Shui was uncertain of the exact reason, but he no longer thought of things as before. He knows that this woman really feels affection for him, other people treats him as trash, but she’s the only one in this world that treats him like a treasure!

Since his birth, Qing Shui had not seen his father. From infancy till now, it had always been this gentle and graceful woman before him that was responsible for his upbringing.

As a result, Qing Shui followed the surname of his mother. His mother is named Qing Yi, belonging to the Qing Clan. The Qing Clan in the Qing village, in this remote region, was considered the absolute authority. The Qing Clan was the most influential family within a 100 li radius because of their connections, as well as their secret family martial arts techniques that were passed down generation after generation. The Qing Clan could be considered as the only family that could rival the top three great families in Hundred Miles City!

As a result, in this remote region, no one could afford to make an enemy out of the Qing Clan. Qing Shui knew all of this because, in these five years, while the other kids in the family practiced martial arts, Qing Shui was the exception. Therefore, he had plenty of free time on his hand and thus, paid more attention to the information flowing around.

Even the commoner kids would practice some form of inferior martial arts. Even in his past life, Qing Shui also had the mentality and wish to become a top-tier expert that possessed heaven shaking and earth shattering strength, able to sweep humanity off its feet.

The chance had finally come, he was reincarnated into a different world. However, he turned out to be a trash that could not cultivate! As he thought of this, he covertly glanced at the beautiful lady by his side. Qing Yi was also gazing at Qing Shui compassionately but there were hints of doting, hope, and a sense of unfairness for Qing Shui in her eyes…

As he glanced at the hope in her eyes, Qing Shui lowered his head. He was afraid that Qing Yi would be disappointed. All parents in this world would want their child to achieve something outstanding in life, it goes without saying, no parents would ever want their child to be a trash! However, looking at the current circumstances, Qing Shui was afraid that he would have no choice but to disappoint his mother.

In the last five years, the one that fed and clothed him was this woman. This woman whom which he calls mother, Qing Shui was very afraid that she would one day leave his side.

“Qing Shui, are you hungry? Even if you go out to play, you still have to remember to eat your meals!” This woman had always been intellectual and caring, possessing a demeanor akin to an angel. This made Qing Shui feel that his mother was not ordinary, initially, he thought that people respected her because she is the daughter of the Qing Clan’s grandmaster, but it seems that this was not the case.

“Mother, am I useless? Other children can practice martial arts, but I am unable to.. Will you eventually become the same as them and think of me as trash?” Qing Shui whispered, his expression somewhat holding back tears.

Qing Yi felt her heart shuddered with pain, the weight of her hope was pinned onto this child’s shoulder. However, this child was unable to cultivate, her hope was destined to be extinguished. One cannot have everything they want in life. Forget about Qing Shui accomplishing anything outstanding, as long as he can live a carefree and happy life, she would be extremely satisfied!

“Shui’er, no matter what, you will always be close to my heart. No matter what, I will always love you, you will always be my pride and joy, in my heart, you will always be the most excellent and outstanding person, only when you are happy Will I be happy!” Qing Yi chastely kissed his cheeks.

Such heartwarming and affectionate actions were quite common between them, Qing Shui was quite used to it. He felt extremely blessed, no matter what, there is still someone who love him. With regards to those who calls him trash or looks down on him with contempt, what does that matter? He just could not help but feel sorry that he had not met Qing Yi’s expectations.

Qing Clan was located at the most northern site of the Qing Village. Over there, everywhere within a radius of about 10 Li [3] was all populated by the Qing Clan main and branch families. Currently, the clan master of the Qing Clan, Qing Luo was already a hundred years old, but due to him being at the peak of Houtian Stage, he still looked like a middle aged man. Humans at the peak of Houtian Stage had a life expectancy of two hundred years, as compared to normal humans who only had a life expectancy of a hundred and thirty years.

Qing Yi is the youngest daughter of the Qing Clan’s clan master. The clan master had a total of four sons and a single daughter. Qing Yi was the only daughter, not only that, she was also the youngest child. Needless to say, she was the apple of his eyes. The Qing Clan, currently collectively had about twenty plus grandchildren, one could say that Qing Luo was very contented. He would always smile genuinely from his heart even when he interacted with Qing Shui. There were countless talented geniuses within the two later generations, so even if there was an addition of one more genius or one more trash, it didn’t really matter much in his eyes. Furthermore, Qing Shui was the son of his precious daughter Qing Yi, even if he could not cultivate, as long as he could peacefully live out his life, Qing Yi would also feel reassured. And as such, Qing Luo was very protective of Qing Shui.

Located within the Qing Clan, there was an enormous courtyard. This courtyard an extremely important place in the Qing Clan. As both Qing Yi and Qing Shui entered, they could see the grandsons and granddaughters of the Qing clan boisterously practice their martial arts, every one of them was akin to a ferocious tiger cub!

Qing Yi could see the sadness in Qing Shui’s eyes so she silently sighed. This child at such a young age had such an unyielding personality that seeks strength, it may be a curse instead of a blessing..

She gently guided Qing Shui into her embrace, unwilling to let him see the children that were currently practicing martial arts!

But all her actions were futile\xa0because, at this moment, sounds of ridicule and contemptible laughter targeted at Qing Shui rang out. This sensation was even worst than being directly called trash!

[1] a video game in Qing Shui’s previous world.

[2] Shui`er (adding a er behind a person’s name makes it more endearing, it is usually between parent and child or between lovers)

[3] a metric system used by chinese to measure distance

TL: Bluefire

Editor: Ziltch
""".replace('\n', ''),
                         chapter.content.text)

    def test_parsing_chapter_101(self):
        api = WuxiaWorldComApi(self.browser)
        chapter = api.get_chapter(
            parse_url('https://www.wuxiaworld.com/novel/ancient-strengthening-technique/ast-chapter-101'))
        self.assertIsNotNone(chapter)
        self.assertTrue(isinstance(chapter, WuxiaWorldComChapter))
        self.assertFalse(chapter.success)
        self.assertTrue(chapter.parse())
        self.assertTrue(chapter.success)
        self.assertEqual('https://www.wuxiaworld.com/novel/ancient-strengthening-technique/ast-chapter-101',
                         str(chapter.url))
        self.assertEqual('https://www.wuxiaworld.com', str(chapter.alter_url('')))
        self.assertEqual("Chapter 101 - A Quiet Beauty", chapter.title)
        self.assertEqual('/novel/ancient-strengthening-technique/ast-chapter-101', chapter.url.path)
        self.assertEqual('lordbluefire_98448380', chapter.translator)
        self.assertEqual(14974, chapter.chapter_id)
        self.assertFalse(chapter.is_teaser)
        self.assertTrue(chapter.karma_locked)
        self.assertEqual('/novel/ancient-strengthening-technique/ast-chapter-100', chapter.previous_chapter.path)
        self.assertEqual('/novel/ancient-strengthening-technique/ast-chapter-102', chapter.next_chapter.path)


# noinspection SpellCheckingInspection
class WuxiaWorldComApiSearchTest(unittest.TestCase):
    def test_search_default(self):
        browser = prepare_browser(Har.WW_SEARCH_DEFAULT)
        api = WuxiaWorldComApi(browser)
        results, n = api.search()
        self.assertEqual(15, len(results))
        self.assertEqual(59, n)

    def test_search_modern(self):
        browser = prepare_browser(Har.WW_SEARCH_MODERN)
        api = WuxiaWorldComApi(browser)
        results, n = api.search(genres=(Genre.MODERN_SETTING,))
        self.assertEqual(7, len(results))
        self.assertEqual(7, n)

import unittest

from urllib3.util import parse_url

import lightnovel.util as util
from lightnovel.wuxiaworld_com import WuxiaWorldComApi
from tests.config import Har, prepare_browser


# noinspection SpellCheckingInspection,DuplicatedCode
class HJCSinkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = prepare_browser(Har.WW_HJC_COVER_C1_2)

    def test_parsing_hjc_description_as_string(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change'))
        novel.parse()
        self.assertTrue(novel.parse())
        description = util.StringHtmlSink().parse(novel.description)
        self.assertEqual("""[Zen’s Synopsis]
In a world where power means everything, and the strong trample the weak; there was a boy born from a Heavenly Jewel Master. Born in a small country which had to struggle to survive, the boy was expected to do great things. Alas he turned out to have blocked meridians and was unable to cultivate, ending up the trash of society. His father’s tarnished pride… his fianceé’s ultimate dishonour…
Being almost accidentally killed and left for the dead, heaven finally smiles upon him as a miracle descends, awakening his potential as a Heavenly Jewel Master. Or… is it truly a gift?
Join our dear rascally and shameless MC Zhou Weiqing in his exploits to reach the peak of the cultivation world, form an army, protect those he loves, and improve his country!
An all new world, an all new power system, unique weaponry & MC! Come join me in laughing and crying together with this new masterpiece from Tang Jia San Shao!

[Translated Synopsis]
Every human has their Personal Jewel of power, when awakened it can either be an Elemental Jewel or Physical Jewel. They circle the right and left wrists like bracelets of power.
Heavenly Jewels are like the twins born, meaning when both Elemental and Physical Jewels are Awakened for the same person, the pair is known as Heavenly Jewels.
Those who have the Physical Jewels are known as Physical Jewel Masters, those with Elemental Jewels are Elemental Jewel Masters, and those who train with Heavenly Jewels are naturally called Heavenly Jewel Masters.
Heavenly Jewel Masters have a highest level of 12 pairs of jewels, as such their training progress is known as Heavenly Jewels 12 Changes.
Our MC here is an archer who has such a pair of Heavenly Jewels.""",
                         description)

    def test_parsing_hjc_description_as_markdown(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change'))
        self.assertTrue(novel.parse())
        description = util.MarkdownHtmlSink().parse(novel.description)
        self.assertEqual("""_[Zen’s Synopsis]_

In a world where power means everything, and the strong trample the weak; there was a boy born from a Heavenly Jewel Master. Born in a small country which had to struggle to survive, the boy was expected to do great things. Alas he turned out to have blocked meridians and was unable to cultivate, ending up the trash of society. His father’s tarnished pride… his fianceé’s ultimate dishonour…

Being almost accidentally killed and left for the dead, heaven finally smiles upon him as a miracle descends, awakening his potential as a Heavenly Jewel Master. Or… is it truly a gift?

Join our dear rascally and shameless MC Zhou Weiqing in his exploits to reach the peak of the cultivation world, form an army, protect those he loves, and improve his country!

An all new world, an all new power system, unique weaponry & MC! Come join me in laughing and crying together with this new masterpiece from Tang Jia San Shao!

---

_[Translated Synopsis]_

Every human has their Personal Jewel of power, when awakened it can either be an Elemental Jewel or Physical Jewel. They circle the right and left wrists like bracelets of power.

Heavenly Jewels are like the twins born, meaning when both Elemental and Physical Jewels are Awakened for the same person, the pair is known as Heavenly Jewels.

Those who have the Physical Jewels are known as Physical Jewel Masters, those with Elemental Jewels are Elemental Jewel Masters, and those who train with Heavenly Jewels are naturally called Heavenly Jewel Masters.

Heavenly Jewel Masters have a highest level of 12 pairs of jewels, as such their training progress is known as Heavenly Jewels 12 Changes.

Our MC here is an archer who has such a pair of Heavenly Jewels.""",
                         description)

    def test_parsing_hjc_description_as_latex(self):
        api = WuxiaWorldComApi(self.browser)
        novel = api.get_novel(parse_url('https://www.wuxiaworld.com/novel/heavenly-jewel-change'))
        novel.parse()
        self.assertTrue(novel.parse())
        description = util.LatexHtmlSink().parse(novel.description)
        self.assertEqual("""\\textit{[Zen’s Synopsis]}\\\\ \\relax
In a world where power means everything, and the strong trample the weak; there was a boy born from a Heavenly Jewel Master. Born in a small country which had to struggle to survive, the boy was expected to do great things. Alas he turned out to have blocked meridians and was unable to cultivate, ending up the trash of society. His father’s tarnished pride... his fianceé’s ultimate dishonour...\\\\ \\relax
Being almost accidentally killed and left for the dead, heaven finally smiles upon him as a miracle descends, awakening his potential as a Heavenly Jewel Master. Or... is it truly a gift?\\\\ \\relax
Join our dear rascally and shameless MC Zhou Weiqing in his exploits to reach the peak of the cultivation world, form an army, protect those he loves, and improve his country!\\\\ \\relax
An all new world, an all new power system, unique weaponry \\& MC! Come join me in laughing and crying together with this new masterpiece from Tang Jia San Shao!\\\\ \\relax
\\hrule
\\textit{[Translated Synopsis]}\\\\ \\relax
Every human has their Personal Jewel of power, when awakened it can either be an Elemental Jewel or Physical Jewel. They circle the right and left wrists like bracelets of power.\\\\ \\relax
Heavenly Jewels are like the twins born, meaning when both Elemental and Physical Jewels are Awakened for the same person, the pair is known as Heavenly Jewels.\\\\ \\relax
Those who have the Physical Jewels are known as Physical Jewel Masters, those with Elemental Jewels are Elemental Jewel Masters, and those who train with Heavenly Jewels are naturally called Heavenly Jewel Masters.\\\\ \\relax
Heavenly Jewel Masters have a highest level of 12 pairs of jewels, as such their training progress is known as Heavenly Jewels 12 Changes.\\\\ \\relax
Our MC here is an archer who has such a pair of Heavenly Jewels.\\\\ \\relax""",
                         description)

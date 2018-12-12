import json
from .api import NovelApiBase
from .log_class import LogBase
from typing import List
from bs4 import BeautifulSoup, Tag, NavigableString


class WuxiaWorldChapterLink:
    title = ''
    url = ''


class WuxiaWorldBook:
    title = ''
    chapters: List[WuxiaWorldChapterLink] = []


class WuxiaWorldNovel(LogBase):
    title = ''
    translator = ''
    tags: List[str] = []
    description_html: Tag = None
    books: List[WuxiaWorldBook] = []
    first_chapter_url = ''
    img_url = 'https://cdn.wuxiaworld.com/images/covers/'
    url = 'https://www.wuxiaworld.com/novel/'

    def __init__(self, bs: BeautifulSoup):
        super().__init__()
        self.log.debug('Extracting data from html.')
        head = bs.select_one('head')
        json_str = head.select_one('script[type=application/ld+json]').text
        json_data = json.loads(json_str)
        self.title = json_data['name']
        self.log.debug("Novel title is: {}".format(self.title))
        self.first_chapter_url = json_data['potentialAction']['target']['urlTemplate']
        self.translator = json_data['author']['name']
        self.img_url = head.select_one('meta[property=og:image]').get('content')
        self.url = head.select_one('meta[property=og:url]').get('content')
        p15 = bs.select_one('div.p-15')
        self.tags = self.__extract_tags(p15)
        self.description_html = p15.select('div.fr-view')[1]
        self.books = self.__extract_books(p15)

    def __extract_tags(self, p15: Tag) -> List[str]:
        tags = []
        for tag_html in p15.select('div.media.media-novel-index div.media-body div.tags a'):
            tag = tag_html.text.strip()
            tags.append(tag)
        self.log.debug("Tags found: {}".format(tags))
        return tags

    def __extract_books(self, p15: Tag) -> List[WuxiaWorldBook]:
        books = []
        for book_html in p15.select('div#accordion div.panel.panel-default'):
            book = WuxiaWorldBook()
            book.title = book_html.select_one('a.collapsed').text.strip()
            self.log.debug("Book: {}".format(book.title))
            book.chapters = self.__extract_chapters(book_html)
            books.append(book)
        return books

    def __extract_chapters(self, book_html: Tag) -> List[WuxiaWorldChapterLink]:
        chapters = []
        for chapter_html in book_html.select('div div li a'):
            chapter = WuxiaWorldChapterLink()
            chapter.title = chapter_html.text.strip()
            chapter.url = 'https://www.wuxiaworld.com' + chapter_html.get('href')
            chapters.append(chapter)
        self.log.debug("Chapters found: {}".format(len(chapters)))
        return chapters

    def description_str(self) -> str:
        strings = []
        for paragraph in self.description_html.select('p'):
            strings.append(paragraph.text.strip())
        return str.join('\n', strings).strip()

    def description_md(self):
        strings = []
        for tag in self.description_html.children:
            if not tag == '\n':
                strings.append(self.__recurse_html_for_md(tag))
        return str.join('\n\n', strings)

    def __recurse_html_for_md(self, el) -> str:
        if type(el) == NavigableString:
            return el.__str__()
        elif not type(el) == Tag:
            self.log.error(type(el))
            return el.__str__()
        tag: Tag = el
        string = ''
        if tag.name == 'p':
            for child in tag.children:
                string += self.__recurse_html_for_md(child)
            return string
        elif tag.name == 'em':
            for child in tag.children:
                string += self.__recurse_html_for_md(child)
            return "*{}*".format(string)
        elif tag.name == 'hr':
            return '---'
        else:
            self.log.warning(tag)
            return tag.__str__()


class WuxiaWorldApi(NovelApiBase):

    def get_novel(self, novel_path: str) -> WuxiaWorldNovel:
        url = "https://www.wuxiaworld.com/novel/{}".format(novel_path.lower())
        response = self._request('GET', url)
        response.raise_for_status()
        bs = BeautifulSoup(response.text, features="html5lib")
        return WuxiaWorldNovel(bs)
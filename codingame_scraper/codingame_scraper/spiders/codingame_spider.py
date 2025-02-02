import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.selector import Selector


class CodingameSpider(scrapy.Spider):
    name = "codingame_selenium"
    start_urls = ["https://www.codingame.com/training/expert"]

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def parse(self, response):
        self.driver.get(response.url)

        try:
            # Attendre que les éléments `cg-puzzle` apparaissent (10 secondes maximum)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@id="games"]/div/div/div/cg-puzzles-section[1]/div/div[3]/cg-puzzle')
                )
            )
        except Exception as e:
            self.logger.error(f"Les puzzles n'ont pas pu être chargés : {e}")
            self.driver.quit()
            return

        # Extraire le contenu de la page après le chargement de JavaScript
        html = self.driver.page_source
        sel = Selector(text=html)

        # Extraction des puzzles
        puzzles = sel.xpath('//*[@id="games"]/div/div/div/cg-puzzles-section[1]/div/div[3]/cg-puzzle')

        extracted_data = []
        for puzzle in puzzles:
            # Extraire le nombre de participants
            participants_text = puzzle.xpath(".//div/div/a/div/div/div[1]/div/div[3]/span/text()").get()
            participants = participants_text.strip() if participants_text else "Unknown"

            # Extraire le titre du puzzle
            title_text = puzzle.xpath(".//div/div/a/div/div/div[1]/div/div[1]/text()").get()
            title = title_text.strip() if title_text else "No Title"

            extracted_data.append({"title": title, "participants": participants})

        self.driver.quit()
        yield {"puzzles_data": extracted_data}

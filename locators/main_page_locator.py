from selenium.webdriver.common.by import By


class MainPageLocators:

    @staticmethod
    def question_locator(question: str):  # Вопрос о важном
        return [By.XPATH, f'//*[@id="accordion__heading-{question}"]']

    @staticmethod
    def answer_locator(answer: str):  # Ответ на вопрос о важном
        return [By.XPATH, f'//*[@id="accordion__panel-{answer}"]']
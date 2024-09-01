import allure
import pytest

from data import Urls, QuestionData
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage


class TestHeaders:

    @allure.title('Проверка кликабельности вопросов о важном и наличия в них ответов')
    @allure.description(
        'На странице ищем вопросы о важном и смотрим ответы"')
    @pytest.mark.parametrize(QuestionData.param, QuestionData.value)
    def test_question_and_answer(self, driver, number, expected_answer):
        question_input = MainPage(driver)
        question_input.open_page(Urls.MAIN_PAGE)
        question_input.scroll_to_element(MainPageLocators.question_locator(number))
        question_input.wait_and_find_element(MainPageLocators.question_locator(number)).click()
        answer = question_input.wait_and_find_element(MainPageLocators.answer_locator(expected_answer))
        assert answer.is_displayed

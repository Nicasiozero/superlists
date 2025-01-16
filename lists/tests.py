from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from lists.models import Item

# class NewVisitorTest(unittest.TestCase):
#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     def tearDown(self):
#         self.browser.quit()

#     def test_can_start_a_todo_list(self):
#         # Edith has heard about a cool new online to-do app.
#         # She goes to check out its homepage
#         self.browser.get("http://localhost:8000")

#         # She notices the page title and header mention to-do lists
#         self.assertIn("To-Do", self.browser.title)
#         header_text = self.browser.find_element(By.TAG_NAME, "h1").text  
#         self.assertIn("To-Do", header_text)

#         # She is invited to enter a to-do item straight away
#         inputbox = self.browser.find_element(By.ID, "id_new_item")  
#         self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

#         # She types "Buy peacock feathers" into a text box
#         # (Edith's hobby is tying fly-fishing lures)
#         inputbox.send_keys("Buy peacock feathers")  

#         # When she hits enter, the page updates, and now the page lists
#         # "1: Buy peacock feathers" as an item in a to-do list table
#         inputbox.send_keys(Keys.ENTER)  
#         time.sleep(1)  

#         table = self.browser.find_element(By.ID, "id_list_table")
#         rows = table.find_elements(By.TAG_NAME, "tr")  
#         # self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows))

#         self.assertTrue(
#         any(row.text == "1: Buy peacock feathers" for row in rows),
#         "New to-do item did not appear in table",
#     )

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        # self.fail("Finish the test!")

        # The page updates again, and now shows both items on her list
        # [...]
        
class HomePageTest(TestCase):
    
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do lists</title>")  
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")
        self.assertTemplateUsed(response, "home.html")  

    def test_home_page_returns_correct_html_2(self):
        response = self.client.get("/")  
        self.assertContains(response, "<title>To-Do lists</title>")  

    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_displays_all_list_items(self):
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")
        response = self.client.get("/")
        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")

    def test_can_save_a_POST_request(self):
        self.client.post("/", data={"item_text": "A new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertRedirects(response, "/")

# class ItemModelTest(TestCase):
#     def test_saving_and_retrieving_items(self):
#         first_item = Item()
#         first_item.text = "The first (ever) list item"
#         first_item.save()

#         second_item = Item()
#         second_item.text = "Item the second"
#         second_item.save()

#         saved_items = Item.objects.all()
#         self.assertEqual(saved_items.count(), 2)

#         first_saved_item = saved_items[0]
#         second_saved_item = saved_items[1]
#         self.assertEqual(first_saved_item.text, "The first (ever) list item")
#         self.assertEqual(second_saved_item.text, "Item the second")
        
if __name__ == "__main__":  
    unittest.main()  
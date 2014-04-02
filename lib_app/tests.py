from django.test import TestCase
  
class BookListView_Test(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) 

class Book_Detail_Test(TestCase):                                                            
    def test_book_detail(self):                                                                      
        response = self.client.get('/book/1/') 
        self.assertEqual(response.status_code, 200) 

class Book_Edit_Test(TestCase):                                                                                
    def test_book_edit(self):                                               
        response = self.client.post('/book_edit/10/',{'title': 'Hamlet',
                                                      'author': 'William Shakespeare'})
        self.assertEqual(response.status_code,200)

                                         
def test_save_document(self):
    doc = {"UUID": "test-uuid", "name": "test"}
    save_document(doc)
    self.assertTrue(collection.find_one({"UUID": "test-uuid"}))
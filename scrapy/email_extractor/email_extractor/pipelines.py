# email_extractor/pipelines.py

import pandas as pd

class ExcelExportPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.items)
        df.to_excel('output.xlsx', index=False)

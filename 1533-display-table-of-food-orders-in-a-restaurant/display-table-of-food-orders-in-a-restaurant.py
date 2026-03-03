class Solution:
    def displayTable(self, orders):
        from collections import defaultdict
        
        food_items = set()
        table_map = defaultdict(lambda: defaultdict(int))
        
        # Collect data
        for customer, table, food in orders:
            food_items.add(food)
            table_map[int(table)][food] += 1
        
        # Sort food items alphabetically
        food_items = sorted(food_items)
        
        # Header row
        result = [["Table"] + food_items]
        
        # Sort tables numerically
        for table in sorted(table_map.keys()):
            row = [str(table)]
            for food in food_items:
                row.append(str(table_map[table][food]))
            result.append(row)
        
        return result
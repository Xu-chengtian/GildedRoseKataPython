# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(5, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    # Logical Error 1
    def test_aged_brie_increase_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        self.assertEqual(items[0].sell_in, 4)

    # Logical Error 2
    def test_backstage_passes_increase_in_10_days(self):
        items = [Item("Backstage passes", 8, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 42)
        self.assertEqual(items[0].sell_in, 7)

    # Logical Error 3
    def test_backstage_passes_increase_in_5_days(self):
        items = [Item("Backstage passes", 2, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)
        self.assertEqual(items[0].sell_in, 1)

    # Syntax Error 1
    def test_update_function(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 10)
        
    # Syntax Error 5
    def test_get_money(self):
        items = [Item("Backstage passes", 2, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        qualities = gilded_rose.get_qualities()
        self.assertEqual(50, qualities)


if __name__ == '__main__':
    unittest.main()

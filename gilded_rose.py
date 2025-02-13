# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = QualityStrategyFactory.get_strategy(item)
            strategy.update_quality(item)

    def get_items(self):
        items_list = []
        for item in self.items:
            items_list.append(item.name)
        return items_list
    
    def get_qualities(self):
        total_qualities = 0
        for item in self.items:
            total_qualities += item.quality
        return total_qualities
    
    def update(self):
        self.update_quality()

class QualityStrategy:
    def update_quality(self, item):
        self.decrease_sell_in(item)
        self.decrease_quality(item)
    
    def decrease_quality(self, item):
        pass
    
    def decrease_sell_in(self, item):
        pass


# Strategy for Normal Items
class NormalItemStrategy(QualityStrategy):
    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
            if item.sell_in < 0:
                item.quality -= 1
                item.quality = max(0, item.quality)
    def decrease_sell_in(self, item):
        item.sell_in -= 1


# Strategy for Aged Brie
class AgedBrieStrategy(QualityStrategy):
    def decrease_quality(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0:
                item.quality += 1
                item.quality = min(50, item.quality)
    def decrease_sell_in(self, item):
        item.sell_in -= 1


# Strategy for Backstage Passes
class BackstagePassStrategy(QualityStrategy):
    def decrease_quality(self, item):
        if item.sell_in < 0:
            item.quality = 0
        else:
            if item.quality < 50:
                item.quality += 1
                if item.sell_in < 10:
                    item.quality += 1
                    if item.sell_in < 5:
                        item.quality += 1
                    item.quality = min(50, item.quality)
    def decrease_sell_in(self, item):
        item.sell_in -= 1


# Strategy for Sulfuras
class SulfurasStrategy(QualityStrategy):
    def decrease_quality(self, item):
        pass
    def decrease_sell_in(self, item):
        pass


# Factory to assign strategy
class QualityStrategyFactory:
    @staticmethod
    def get_strategy(item):
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name in "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassStrategy()
        elif item.name in "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        else:
            return NormalItemStrategy()
from typing import Union


class LuxuryWatch:
    __watches_created = 0

    def __init__(self):
        LuxuryWatch.__watches_created += 1
        self.__engraved = ''

    @property
    def engraved(self) -> str:
        return f'Engraved: "{self.__engraved}"'

    @classmethod
    def create_engraved_watch(cls, engrave: str) -> Union['LuxuryWatch', None]:
        if cls.engraving_allowed(engrave):
            watch = LuxuryWatch()
            watch._LuxuryWatch__engraved = engrave
            return watch

    @classmethod
    def get_number_of_watches_created(cls) -> int:
        return f"Created watches: {cls.__watches_created}"

    @staticmethod
    def engraving_allowed(engrave: str) -> bool:
        if len(engrave) > 40:
            raise ValueError("The number of letters for engraved can be more "
                             f"than 40 (received {len(engrave)})")
        elif str.isspace(engrave):
            raise ValueError("The engraving received have only spaces")
        elif not str.isalnum(engrave):
            raise ValueError(f"The engraving ({engrave}) received isn't alphanumeric")
        return True

print("Create a watch with no engraving".center(80, '*'))
no_engraved_watch = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())
print(no_engraved_watch.engraved)
print("Create a watch with correct text for engraving".center(80, '*'))
engraved_watch_1 = LuxuryWatch.create_engraved_watch('hi')
print(LuxuryWatch.get_number_of_watches_created())
print(engraved_watch_1.engraved)
print("Try to create a watch with incorrect text, like 'foo@baz.com'.".center(80, '*'))
try:
    engraved_watch_2 = LuxuryWatch.create_engraved_watch('foo@baz.com')
except ValueError:
    pass
print(LuxuryWatch.get_number_of_watches_created())

from django.db import models
from django.utils import timezone
import random

class GuessNumbers(models.Model):
    # 로또 번호 리스트의 이름
    name = models.CharField(max_length=24)
    # 로또 번호 리스트에 대한 설명
    text = models.CharField(max_length=255)
    # generate함수를 통해 생성되는 로또 번호 리스트
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]')
    # generate함수를 통해 생성할 로또 번호 set의 수
    num_lottos = models.IntegerField(default=5)
    # 로또 번호 리스트 생성 일시
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1, 46)) # 1~45 까지의 숫자들이 들어있는 리스트

        for _ in range(0, self.num_lottos): # range(0, 5) -> 0, 1, 2, 3, 4
            random.shuffle(origin) # 1~45 숫자를 뒤섞음
            guess = origin[:6] # 뒤섞인 상태에서 앞의 6개 추출
            guess.sort()
            self.lottos += str(guess) + '\n'

        self.update_date = timezone.now()
        self.save() # GuessNumbers의 Object를 DB에 저장


    def __str__(self):
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)

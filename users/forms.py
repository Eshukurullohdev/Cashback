from django import forms
from .models import User


CAR_MODELS = [
    # 🇺🇿 UzAuto
    
    ('AITO M5', 'AITO M5'),
    ('AITO M7', 'AITO M7'),
    ('AITO M9', 'AITO M9'),

    ('BYD Atto 3', 'BYD Atto 3'),
    ('BYD Dolphin', 'BYD Dolphin'),
    ('BYD Han', 'BYD Han'),
    ('BYD Seal', 'BYD Seal'),
    ('BYD Song Plus EV', 'BYD Song Plus EV'),

    ('Chevrolet Bolt EV', 'Chevrolet Bolt EV'),
    ('Chevrolet Captiva', 'Chevrolet Captiva'),
    ('Chevrolet Cobalt', 'Chevrolet Cobalt'),
    ('Chevrolet Equinox', 'Chevrolet Equinox'),
    ('Chevrolet Malibu 1', 'Chevrolet Malibu 1'),
    ('Chevrolet Malibu 2', 'Chevrolet Malibu 2'),
    ('Chevrolet Onix', 'Chevrolet Onix'),
    ('Chevrolet Orlando', 'Chevrolet Orlando'),
    ('Chevrolet Spark', 'Chevrolet Spark'),
    ('Chevrolet Spark EV', 'Chevrolet Spark EV'),
    ('Chevrolet Tahoe', 'Chevrolet Tahoe'),
    ('Chevrolet Tracker', 'Chevrolet Tracker'),
    ('Chevrolet Trailblazer', 'Chevrolet Trailblazer'),
    ('Chevrolet Traverse', 'Chevrolet Traverse'),
    ('Chevrolet Volt', 'Chevrolet Volt'),

    ('Daewoo Damas', 'Daewoo Damas'),
    ('Daewoo Jentra', 'Daewoo Jentra'),
    ('Daewoo Lacetti', 'Daewoo Lacetti'),
    ('Daewoo Matiz', 'Daewoo Matiz'),
    ('Daewoo Nexia 1', 'Daewoo Nexia 1'),
    ('Daewoo Nexia 2', 'Daewoo Nexia 2'),
    ('Daewoo Nexia 3', 'Daewoo Nexia 3'),
    ('Daewoo Tico', 'Daewoo Tico'),

    ('Hyundai Ioniq 5', 'Hyundai Ioniq 5'),
    ('Hyundai Ioniq 6', 'Hyundai Ioniq 6'),
    ('Hyundai Kona Electric', 'Hyundai Kona Electric'),

    ('Kia EV3', 'Kia EV3'),
    ('Kia EV5', 'Kia EV5'),
    ('Kia EV6', 'Kia EV6'),
    ('Kia EV9', 'Kia EV9'),

    ('Li Auto Mega', 'Li Auto Mega'),

    ('Nissan Leaf', 'Nissan Leaf'),

    ('Tesla Model 3', 'Tesla Model 3'),
    ('Tesla Model S', 'Tesla Model S'),
    ('Tesla Model X', 'Tesla Model X'),
    ('Tesla Model Y', 'Tesla Model Y'),

    ('Volkswagen ID.3', 'Volkswagen ID.3'),
    ('Volkswagen ID.4', 'Volkswagen ID.4'),
    ('Volkswagen ID.7', 'Volkswagen ID.7'),

    ('XPeng G6', 'XPeng G6'),
    ('XPeng P7', 'XPeng P7'),

    ('Zeekr 001', 'Zeekr 001'),
    ('Zeekr 7X', 'Zeekr 7X'),
    ('Zeekr X', 'Zeekr X'),

    ('Dongfeng Box', 'Dongfeng Box'),
    ('Dongfeng E70', 'Dongfeng E70'),
    ('Dongfeng eπ 007', 'Dongfeng eπ 007'),
    ('Dongfeng eπ 008', 'Dongfeng eπ 008'),
    ('Dongfeng M-Hero 917', 'Dongfeng M-Hero 917'),
    ('Dongfeng Nammi 01', 'Dongfeng Nammi 01'),
    ('Dongfeng Rich 6 EV', 'Dongfeng Rich 6 EV'),
    ('Dongfeng T5 EVO', 'Dongfeng T5 EVO'),
    ('Dongfeng Voyah Dream', 'Dongfeng Voyah Dream'),
    ('Dongfeng Voyah Free', 'Dongfeng Voyah Free'),
    ('Dongfeng Voyah Passion', 'Dongfeng Voyah Passion'),

    ('Avatr 11', 'Avatr 11'),
    ('Avatr 12', 'Avatr 12'),

    ('Changan Deepal S07', 'Changan Deepal S07'),
    ('Changan Deepal SL03', 'Changan Deepal SL03'),

    ('Geely Galaxy E5', 'Geely Galaxy E5'),
    ('Geely Geometry C', 'Geely Geometry C'),

    ('Leapmotor C10', 'Leapmotor C10'),
    ('Leapmotor T03', 'Leapmotor T03'),

    ('NIO ES6', 'NIO ES6'),
    ('NIO ET5', 'NIO ET5'),
    ('NIO ET7', 'NIO ET7'),

    ('Xiaomi SU7', 'Xiaomi SU7'),
    ('Xiaomi YU7', 'Xiaomi YU7'),

    ('Yangwang U8', 'Yangwang U8'),
    ('Yangwang U9', 'Yangwang U9'),

]
YEAR_CHOICES = [
    (year, year) for year in range(2036, 1999, -1)
]

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "••••••••"
        })
    )

    car_model = forms.ChoiceField(
    choices=[('', 'Mashina modelini tanlang')] + CAR_MODELS,
    widget=forms.Select(attrs={
        'class': 'input'
    })
)

    car_year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        label="Yili",
        widget=forms.Select(attrs={
            "placeholder": "2020"
        })
    )

    plate_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "placeholder": "01 A 777 AA"
        })
    )

    class Meta:
        model = User
        fields = ['phone', 'password']
        widgets = {
            "phone": forms.TextInput(attrs={
                "placeholder": "+998 90 123 45 67"
            })
        }

from .models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'profile_image']  # foydalanuvchi o‘z profilini yangilashi uchun kerakli maydonlar
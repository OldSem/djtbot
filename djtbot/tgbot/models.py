from django.db import models


class CategoryClothe(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CategoryPrice(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_user_in_telegram = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Male(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ClotheMale(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClotheCountry(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClothePartner(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Clothe(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    article_id = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300)
    img_center = models.ImageField(upload_to='bot_media')
    img_inline = models.ImageField(upload_to='bot_media')
    img_bottom = models.ImageField(upload_to='bot_media')
    created = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField()
    markup = models.PositiveSmallIntegerField()

    currency = models.ForeignKey(CategoryPrice, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryClothe, on_delete=models.CASCADE)
    partner = models.ForeignKey(ClothePartner, on_delete=models.CASCADE)
    male = models.ForeignKey(ClotheMale, on_delete=models.CASCADE)
    country = models.ForeignKey(ClotheCountry, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_id

    @property
    def img_inline_path(self):
        return '{}'.format(self.img_inline.path)

    @property
    def img_center_path(self):
        return '{}'.format(self.img_center.path)


class Basket(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_user_in_telegram = models.CharField(max_length=30)
    product_id = models.CharField(max_length=30)

    def __str__(self):
        return self.product_id


class SystemPhoto(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='bot_media')

    def __str__(self):
        return self.name

    @property
    def img_path(self):
        return '{}'.format(self.img.path)

    @property
    def img_url(self):
        return '{}'.format(self.img.url)


class Order(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, models.CASCADE)
    article = models.ForeignKey(Clothe, models.CASCADE)
    quantity_of_goods = models.PositiveSmallIntegerField(default=1)
    first_name = models.CharField(max_length=150)
    markup = models.PositiveSmallIntegerField(null=True, default=0)
    price = models.PositiveSmallIntegerField(null=True, default=0)
    name = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=50, null=True)
    post_office = models.CharField(max_length=150, null=True)
    department = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=30, null=True)
    size = models.CharField(max_length=30, null=True)
    tnt = models.CharField(max_length=30, null=True)
    have_ordered = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


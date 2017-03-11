from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField("名称", max_length=50)
    slug = models.SlugField(
        "Slug",
        max_length=50, unique=True,
        help_text='根据name生成的，用于生成页面URL,必须唯一')
    description = models.TextField("描述")
    is_active = models.BooleanField("是否激活", default=True)
    meta_Keywords = models.CharField(
        "关键词", max_length=255,
        default='水果', ##########遗漏字段，添加时要添加默认值
        help_text='meta关键词 有利于SEO 用逗号分割')
    meta_description = models.CharField(
        "Meta 描述", max_length=255,
    help_text='meta描述')
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_category', args=(self.slug,))


class Product(models.Model):
    name = models.CharField("名称", max_length=255, unique=True)
    slug = models.SlugField(
        "Slug",
        max_length=255, unique=True,
        help_text='根据name生成的, 用于生成URL, 必须唯一')
    brand = models.CharField("品牌", max_length=50)
    sku = models.CharField("计量单位", max_length=50)
    price = models.DecimalField("价格", max_digits=9, decimal_places=2)
    old_price = models.DecimalField(
        "就价格",
        max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.ImageField("图片", max_length=50)
    is_active = models.BooleanField("设为激活", default=True)
    is_bestseller = models.BooleanField("标为畅销", default=False)
    is_featured = models.BooleanField("标为推荐", default=False)
    quantity = models.IntegerField("数量")
    description = models.TextField("描述")
    meta_keywords = models.CharField(
        "Meta描述",
        max_length=255, help_text='Meta 描述标签')
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args=(self.slug,))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
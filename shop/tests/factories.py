import factory

from shop.models import Category, Product, Brand



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.faker.Faker('name')
    slug = factory.faker.Faker('slug')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    title = factory.faker.Faker('name')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.faker.Faker('name')
    brand = factory.SubFactory(BrandFactory)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.append(category)


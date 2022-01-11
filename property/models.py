from agent.models import Agent
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("property:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class PropertyFeature(models.Model):
    name = models.CharField(verbose_name=_("Feature Group Title"), help_text=_("Required"), max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Property Features")
        verbose_name_plural = _("Property Features")

    def __str__(self):
        return self.name


class PropertySpecification(models.Model):

    property_features = models.ForeignKey(PropertyFeature, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

    def __str__(self):
        return self.name


class Property(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.CharField(
        verbose_name=_("description"), help_text=_("Not Required"), blank=True, max_length=255
    )
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(
        verbose_name=_("Property Price"),
        help_text=_("Maximum 99999999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 a and 99999999.99"),
            },
        },
        max_digits=12,
        decimal_places=2,
    )

    is_active = models.BooleanField(
        verbose_name=_("Property for sale"),
        help_text=_("Change property visibility"),
        default=True,
    )
    property_location = models.CharField(max_length=255)
    location_link = models.URLField(max_length=200)
    document_file = models.FileField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Property")
        verbose_name_plural = _("Property")

    def get_absolute_url(self):
        return reverse("store:property_detail", args=[self.slug])

    def __str__(self):
        return self.title


class PropertySpecificationValue(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    specification = models.ForeignKey(PropertySpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Property specification value (maximum of 255 words)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Property specification Value")
        verbose_name_plural = _("Property Specification Value")

    def __str__(self):
        return self.value


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="property_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a property image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Property Image")
        verbose_name_plural = _("Property Images")

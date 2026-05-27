from django.contrib import admin
from main.models import Module, Topic, Presentation, TopicImage, Product, AssistantMessage


class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1
    fields = ('title', 'description', 'order', 'info')


class PresentationInline(admin.TabularInline):
    model = Presentation
    extra = 1
    fields = ('title', 'file', 'order')


class TopicImageInline(admin.TabularInline):
    model = TopicImage
    extra = 1
    fields = ('image', 'caption', 'order')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    inlines = [TopicInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order')
    list_filter = ('module',)
    search_fields = ('title', 'description')
    inlines = [PresentationInline, TopicImageInline]


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'order')
    list_filter = ('topic',)
    search_fields = ('title',)


@admin.register(TopicImage)
class TopicImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'topic', 'order')
    list_filter = ('topic',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')


@admin.register(AssistantMessage)
class AssistantMessageAdmin(admin.ModelAdmin):
    list_display = ('role', 'created_at', 'short_text')
    list_filter = ('role', 'created_at')
    search_fields = ('text',)
    ordering = ('-created_at',)

    def short_text(self, obj):
        return obj.text[:80]
    short_text.short_description = 'Текст'

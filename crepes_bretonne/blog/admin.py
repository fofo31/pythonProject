from django.contrib import admin
from .models import Categorie, Article
from django.utils.text import Truncator

def apercu_contenu(self, article):
    """     Retourne les 40 premiers caractères du contenu del'article,
    suivi de points de suspension si le texte est pluslong.
    On pourrait le coder nous même, mais Django fournitdéjà la
    fonction qui le fait pour nous !    """

    return Truncator(article.contenu).chars(40, truncate='...')



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date','apercu_contenu')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur...)
        ('Général', {'classes': ['collapse', ],'fields': ('titre', 'auteur', 'categorie')}),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !','fields': ('contenu', )
        }),
    )

    def apercu_contenu(self, article):
        """     Retourne les 40 premiers caractères du contenu del'article,
        suivi de points de suspension si le texte est pluslong.
        On pourrait le coder nous même, mais Django fournitdéjà la
        fonction qui le fait pour nous !    """

        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description='Aperçu du contenu'







admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
